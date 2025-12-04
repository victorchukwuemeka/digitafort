import sqlite3
import os



DB_FIlE = "example.db"

if os.path.exists(DB_FIlE):
    os.remove(DB_FIlE)
    print("removed")
else:
    print("nothing their")


try:
    conn = sqlite3.connect(DB_FIlE)
    print("connected")
except sqlite3.SQLITE_ERROR as e:
    print({e})





try:
    cursor = conn.cursor()

    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE 
    );
    """

    cursor.execute(create_table_query)
    print("Create the table")
    conn.commit()


except sqlite3.Error as e:

    print(f"table failed{e}")



try:
    
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
    print("Inserted one row for Alice.")

    
    users_to_insert = [
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com")
    ]
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users_to_insert)
    print("Inserted multiple rows for Bob and Charlie.")

    conn.commit() 
except sqlite3.Error as e:
    print(f"Error inserting data: {e}")


num = [4,5]
(a,b) = num