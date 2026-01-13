"""
# Python with Databases: Interacting with SQLite using `sqlite3`

This file provides a guide to using Python's built-in `sqlite3` module to work
with SQLite databases. SQLite is a lightweight, serverless, file-based database,
which makes it incredibly easy to get started with databases in Python.
"""

import sqlite3
import os


DB_FILE = "example.db"


#todo
# check if file exist 
# clean the old db 
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

#erro check 
#connect 
try:
    connect_db = sqlite3.connect(DB_FILE)
except sqlite3.DatabaseError as e:
    print(f"failed{e}")