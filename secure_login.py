import sqlite3

def setup_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'SuperSecret123')")
    cursor.execute("INSERT INTO users VALUES ('prince', 'CyberGhana2026!')")
    conn.commit()
    return conn

def secure_login(conn, username, password):
    cursor = conn.cursor()
    # REMEDIATION: Using parameterized queries (?) prevents SQL Injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Executing Parameterized Query with inputs: {username}, {password}")
    
    try:
        # The inputs are passed safely as a tuple
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        if user:
            print("[+] Login Successful!")
        else:
            print("[-] Login Failed.")
    except Exception as e:
        print(f"[!] Database Error: {e}")

if __name__ == "__main__":
    print("--- Secure SQL Injection Lab ---")
    conn = setup_database()
    
    # 1. Normal Login (Should work)
    print("\n[Test 1: Normal Login]")
    secure_login(conn, "admin", "SuperSecret123")
    
    # 2. SQL Injection Attack (Should FAIL now)
    print("\n[Test 2: SQL Injection Attack]")
    secure_login(conn, "admin' OR '1'='1", "anything")
