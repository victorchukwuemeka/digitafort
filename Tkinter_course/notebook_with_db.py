import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- Database Functions ---

def init_db():
    """Create the database and table if they don't exist."""
    conn = sqlite3.connect("notes_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY,
            content TEXT
        )
    """)
    # Insert a default row if empty
    cursor.execute("SELECT COUNT(*) FROM notes")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO notes (content) VALUES ('')")
    conn.commit()
    conn.close()

def save_to_db(text):
    """Save the text to the database."""
    try:
        conn = sqlite3.connect("notes_data.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET content = ? WHERE id = 1", (text,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Note saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save: {e}")

def load_from_db():
    """Load the saved text from the database."""
    conn = sqlite3.connect("notes_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM notes WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else ""

# --- GUI Functions ---

def create_notebook_app():
    init_db()  # Initialize the database on startup
    
    root = tk.Tk()
    root.title("Tkinter Notebook with Database")
    root.geometry("400x350")

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True, fill="both")

    # Tab 1: Notes
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="My Notes")

    label1 = tk.Label(tab1, text="Write your notes here:", font=("Arial", 10, "bold"))
    label1.pack(pady=5)

    # Text widget for multi-line notes
    text_area = tk.Text(tab1, height=10, width=40)
    text_area.pack(padx=10, pady=5)
    
    # Load existing content from DB
    saved_text = load_from_db()
    text_area.insert("1.0", saved_text)

    # Save Button
    save_btn = tk.Button(tab1, text="Save Note to DB", 
                         command=lambda: save_to_db(text_area.get("1.0", tk.END).strip()))
    save_btn.pack(pady=10)

    # Tab 2: Settings
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Settings")
    tk.Label(tab2, text="App Settings (Placeholder)").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_notebook_app()
