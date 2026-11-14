# SQL Injection & Database Hardening Lab

This project demonstrates the mechanics of a SQL Injection vulnerability and provides the secure coding remediation for it. 

## The Problem (`vulnerable_login.py`)
In the vulnerable script, user input is directly concatenated into the SQL query using f-strings. This allows an attacker to input a payload like `' OR '1'='1` to bypass authentication and gain unauthorized access to the database.

## The Remediation (`secure_login.py`)
In the secure script, **Parameterized Queries** (Prepared Statements) are used. The database engine parses the query first, and then safely binds the user input as data, not executable code. This completely neutralizes SQL Injection.

## How to Run Locally
1. Clone this repository.
2. Run the vulnerable version: `python vulnerable_login.py`
3. Run the secure version: `python secure_login.py`

*Author: Yeboah Prince Kwabena | VAPT Professional (CSA Ghana)*
