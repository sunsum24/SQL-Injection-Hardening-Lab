import sqlite3

def setup_database():
    # Creates an in-memory database for testing
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    # Insert dummy users
    cursor.execute("INSERT INTO users VALUES ('admin', 'SuperSecret123')")
    cursor.execute("INSERT INTO users VALUES ('prince', 'CyberGhana2026!')")
    conn.commit()
    return conn

def vulnerable_login(conn, username, password):
    cursor = conn.cursor()
    # VULNERABILITY: Using string formatting (f-strings) allows SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing Query: {query}")
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            print("[+] Login Successful!")
        else:
            print("[-] Login Failed.")
    except Exception as e:
        print(f"[!] Database Error: {e}")

if __name__ == "__main__":
    print("--- Vulnerable SQL Injection Lab ---")
    conn = setup_database()
    
    # 1. Normal Login (Should work)
    print("\n[Test 1: Normal Login]")
    vulnerable_login(conn, "admin", "SuperSecret123")
    
    # 2. SQL Injection Attack (Bypass login without knowing password)
    print("\n[Test 2: SQL Injection Attack]")
    # The payload ' OR '1'='1 makes the query return true
    vulnerable_login(conn, "admin' OR '1'='1", "anything")
