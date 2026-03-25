import tkinter as tk
from tkinter import ttk

def create_notebook_app():
    # 1. Create the main window
    root = tk.Tk()
    root.title("Tkinter Notebook Tutorial")
    root.geometry("400x300")

    # 2. Create the Notebook widget (it belongs to the ttk module)
    # The Notebook is the container for all your tabs.
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True, fill="both")

    # 3. Create Frames for each tab
    # Think of a Frame as a blank canvas for each page of your notebook.
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)

    # 4. Add the tabs to the Notebook
    notebook.add(tab1, text="General")
    notebook.add(tab2, text="Settings")
    notebook.add(tab3, text="Help")

    # 5. Add content to Tab 1 (General)
    label1 = tk.Label(tab1, text="Welcome to the General Tab!", font=("Arial", 12))
    label1.pack(padx=20, pady=20)
    
    entry1 = tk.Entry(tab1)
    entry1.pack(pady=10)
    entry1.insert(0, "Type something here...")

    # 6. Add content to Tab 2 (Settings)
    label2 = tk.Label(tab2, text="Adjust your settings here.")
    label2.pack(padx=20, pady=20)
    
    check_var = tk.BooleanVar()
    check_button = tk.Checkbutton(tab2, text="Enable Notifications", variable=check_var)
    check_button.pack()

    # 7. Add content to Tab 3 (Help)
    label3 = tk.Label(tab3, text="Need help?\nVisit our documentation.", justify="center")
    label3.pack(padx=20, pady=20)
    
    exit_button = tk.Button(tab3, text="Close App", command=root.destroy)
    exit_button.pack(pady=10)

    # 8. Start the application
    root.mainloop()

if __name__ == "__main__":
    create_notebook_app()
