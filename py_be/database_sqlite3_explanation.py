"""
# Python with Databases: Interacting with SQLite using `sqlite3`

This file provides a guide to using Python's built-in `sqlite3` module to work
with SQLite databases. SQLite is a lightweight, serverless, file-based database,
which makes it incredibly easy to get started with databases in Python.
"""

import sqlite3
import os

DB_FILE = "example.db"

# --- 0. Cleanup previous database file for a clean run ---
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"Removed old database file: {DB_FILE}")


# --- 1. Connecting to a Database ---
# To interact with a SQLite database, you first need to establish a connection.
# The `sqlite3.connect()` function will open a connection to the database file.
# If the file does not exist, it will be created automatically.

print("\n--- 1. Connecting to the database ---")
try:
    # `conn` is the connection object
    conn = sqlite3.connect(DB_FILE)
    print(f"Successfully connected to database: {DB_FILE}")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    # Exit if connection fails
    exit()


# --- 2. Creating a Cursor and Executing SQL ---
# A "cursor" is an object that allows you to execute SQL commands and fetch results.
# We will use it to create a table in our database.

print("\n--- 2. Creating a table ---")
try:
    # `cursor` is the cursor object
    cursor = conn.cursor()

    # SQL statement to create a table named 'users'
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """
    cursor.execute(create_table_query)
    print("Table 'users' created successfully (if it didn't exist).")

    # To save the changes (like creating a table), you must "commit" them.
    conn.commit()
except sqlite3.Error as e:
    print(f"Error creating table: {e}")


# --- 3. Inserting Data ---
# To insert data, we use the `INSERT` SQL statement.
# IMPORTANT: Always use parameter substitution (the `?` placeholder) to prevent
# SQL injection vulnerabilities.

print("\n--- 3. Inserting data ---")
try:
    # Insert a single row
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
    print("Inserted one row for Alice.")

    # Insert multiple rows
    users_to_insert = [
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com")
    ]
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users_to_insert)
    print("Inserted multiple rows for Bob and Charlie.")

    conn.commit() # Commit the insertions
except sqlite3.Error as e:
    print(f"Error inserting data: {e}")


# --- 4. Querying (Selecting) Data ---
# To retrieve data, we use the `SELECT` statement. After executing the query,
# you can use `fetchone()`, `fetchall()`, or `fetchmany()` to get the results.

print("\n--- 4. Querying data ---")
try:
    # Select all users
    cursor.execute("SELECT * FROM users")

    # --- Method A: `fetchall()` ---
    # Fetches all remaining rows of a query result, returning a list of tuples.
    print("\n--- A. Using fetchall() ---")
    all_users = cursor.fetchall()
    print("All users in the database:")
    for user in all_users:
        print(f"  ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    # --- Method B: `fetchone()` ---
    # Fetches the next row of a query result set, returning a single tuple, or None.
    print("\n--- B. Using fetchone() ---")
    cursor.execute("SELECT * FROM users WHERE name = ?", ("Bob",))
    bob = cursor.fetchone()
    if bob:
        print(f"Found Bob: {bob}")
    else:
        print("Bob not found.")

except sqlite3.Error as e:
    print(f"Error querying data: {e}")


# --- 5. Updating Data ---
# To modify existing records, use the `UPDATE` statement.

print("\n--- 5. Updating data ---")
try:
    # Update Alice's email
    update_query = "UPDATE users SET email = ? WHERE name = ?"
    cursor.execute(update_query, ("alice.smith@newdomain.com", "Alice"))
    conn.commit()
    print("Updated Alice's email.")

    # Verify the update
    cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
    updated_alice = cursor.fetchone()
    print(f"Alice's updated info: {updated_alice}")

except sqlite3.Error as e:
    print(f"Error updating data: {e}")


# --- 6. Deleting Data ---
# To remove records, use the `DELETE` statement.

print("\n--- 6. Deleting data ---")
try:
    # Delete Charlie
    delete_query = "DELETE FROM users WHERE name = ?"
    cursor.execute(delete_query, ("Charlie",))
    conn.commit()
    print("Deleted Charlie from the database.")

    # Verify the deletion
    cursor.execute("SELECT * FROM users")
    remaining_users = cursor.fetchall()
    print("Remaining users:")
    for user in remaining_users:
        print(f"  - {user}")

except sqlite3.Error as e:
    print(f"Error deleting data: {e}")


# --- 7. Closing the Connection ---
# It's important to close the connection when you're done with it to free up resources.
# A `finally` block is a good place to ensure this happens.

print("\n--- 7. Closing the connection ---")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")

print("\n--- End of SQLite3 Explanation ---")
