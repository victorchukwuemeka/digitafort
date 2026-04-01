import tkinter as tk 
from tkinter import ttk 
import sqlite3




def create_notebook_db():
    #creating the db file 
    conn = sqlite3.connect("note_book.db")
    cursor = conn.cursor()
    #create the table .
    cursor.execute(""" CREAT TABLE IF NOT EXIST notes(id INTEGER PRIMARY KEY, content TEXT)""")
    cursor.execute("SELECT COUNT(*) FROM notes")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO notes (content) VALUES ('')")
    conn.commit()
    conn.close()




def save_db(text):
    #connect to the db 
    conn = sqlite3.connect("note_book.db")
    #control of the db
    cursor = conn.cursor()
    #execution of query 
    cursor.execute(""" UPDATE notes SET content =? WHERE id = 1""", (text))
    #to commit our query
    conn.commit()
    conn.close()



def laod_db():
    #connect to db 
    conn = sqlite3.connect("note_book.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT content FROM notes WWHERE  id = 1""")
    row  = cursor.fetchone()
    #conn.commit()
    conn.close()
    return row[0] if  row else""


def create_notebook_app():
    create_notebook_db()

    
    root = tk.Tk()
    root.title("Note Pad")
    root.geometry("400x300")

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True, fill="both")

    #create the frame 
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)


    #add the tabs 
    notebook.add(tab1, text="General")
    notebook.add(tab2, text="settings")
    notebook.add(tab3 , text="Help")

    #label of the entry 
    label1 = tk.Label(tab1, text="welcome to the general tab",font=("Arail", 12))
    label1.pack(padx=20, pady=20)
    
    #the form it self
    entry1 = tk.Entry(tab1)
    entry1.pack(pady=10)


    #tab for setting 
    settings  = tk.Label(tab2, text="adjust settings here")
    settings.pack(padx=20, pady=20)


    check_var = tk.BooleanVar()
    check_button = tk.Checkbutton(tab2, text="Enable notifications", variable=check_var)
    check_button.pack()


    #tab help 
    label3 = tk.Label(tab3, text="Need help?\nVisit our documentation.", justify="center")
    label3.pack(pady=20, padx=20)


    close_app = tk.Button(tab3, text="Close App", command=root.destroy)
    close_app.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_notebook_app()



