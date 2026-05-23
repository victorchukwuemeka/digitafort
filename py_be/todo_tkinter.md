# To-Do List App with Tkinter
A simple, function-based To-Do List application using Python's built-in `tkinter` library.

**Prerequisites:** Python 3.x (tkinter is included — no pip install needed)

---

## Full Code

```python
import tkinter as tk
from tkinter import messagebox


# tasks is a plain list of dictionaries.
# Each dict holds the task text and whether it is done.
# Example: [{"text": "Buy groceries", "done": False}]
tasks = []


# --- 1. Helper: Refresh the Listbox ---
# This function redraws the entire Listbox from scratch
# every time the tasks list changes (add, delete, toggle).
def refresh_list():
    listbox.delete(0, tk.END)                        # clear every item in the Listbox

    for task in tasks:
        prefix = "[Done]  " if task["done"] else "[ ]      "
        listbox.insert(tk.END, prefix + task["text"]) # append item to the end of the list

        if task["done"]:
            # itemconfig styles the item we just inserted (tk.END = last item).
            # Setting fg to grey signals visually that the task is complete.
            listbox.itemconfig(tk.END, fg="#aaaaaa")

    done_count = sum(1 for t in tasks if t["done"])  # count completed tasks
    status_var.set(f"{len(tasks)} task(s)   |   {done_count} done") # update status bar


# --- 2. Callback: Add a New Task ---
# event=None lets this function work both as a button command
# AND as a keyboard binding (the Enter key passes an event object).
def add_task(event=None):
    text = entry_var.get().strip()                   # read and trim whitespace from the Entry

    if not text:                                     # do nothing if the field is empty
        messagebox.showwarning("Empty Task", "Please type a task before adding.")
        return

    tasks.append({"text": text, "done": False})      # add new task dict to the list
    entry_var.set("")                                # clear the Entry field
    refresh_list()                                   # redraw the Listbox


# --- 3. Callback: Toggle a Task Done / Undone ---
def toggle_done():
    selection = listbox.curselection()               # returns a tuple of selected row indexes

    if not selection:
        messagebox.showinfo("No Selection", "Click a task first, then press Mark Done.")
        return

    index = selection[0]                             # grab the first selected index
    tasks[index]["done"] = not tasks[index]["done"]  # flip True -> False or False -> True
    refresh_list()


# --- 4. Callback: Delete the Selected Task ---
def delete_task():
    selection = listbox.curselection()

    if not selection:
        messagebox.showinfo("No Selection", "Click a task first, then press Delete.")
        return

    tasks.pop(selection[0])                          # remove the item at the selected index
    refresh_list()


# --- 5. Callback: Clear Every Task ---
def clear_all():
    if not tasks:                                    # nothing to clear
        return

    # askyesno shows a Yes/No dialog and returns True if the user clicks Yes.
    if messagebox.askyesno("Confirm", "Delete ALL tasks? This cannot be undone."):
        tasks.clear()                                # empty the Python list
        refresh_list()


# --- 6. Build the Main Window ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("480x560")
root.configure(bg="#f0f4f8")                         # light grey-blue background
root.resizable(False, False)                         # lock window size


# --- 7. Header ---
header = tk.Frame(root, bg="#2d6a4f", pady=14)       # dark green frame
header.pack(fill=tk.X)                               # stretch across the full width

tk.Label(
    header,
    text="To-Do List",
    font=("Helvetica", 18, "bold"),
    bg="#2d6a4f",
    fg="white"
).pack()


# --- 8. Input Row (Entry + Add Button) ---
input_frame = tk.Frame(root, bg="#f0f4f8", pady=10)
input_frame.pack(fill=tk.X, padx=15)

# StringVar keeps the Entry value in sync with a Python variable.
entry_var = tk.StringVar()

entry = tk.Entry(
    input_frame,
    textvariable=entry_var,
    font=("Helvetica", 12),
    relief=tk.FLAT,
    bg="white"
)
# expand=True makes the Entry stretch to fill all leftover horizontal space.
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 8))

tk.Button(
    input_frame,
    text="Add Task",
    bg="#2d6a4f",
    fg="white",
    relief=tk.FLAT,
    font=("Helvetica", 11),
    cursor="hand2",                                  # show a pointer cursor on hover
    command=add_task
).pack(side=tk.LEFT, ipady=8)

# Pressing Enter anywhere in the window also calls add_task.
# The lambda absorbs the event argument that bind passes automatically.
root.bind("<Return>", lambda event: add_task())


# --- 9. Listbox + Scrollbar ---
list_frame = tk.Frame(root, bg="#f0f4f8")
list_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)             # attach scrollbar to the right edge

listbox = tk.Listbox(
    list_frame,
    font=("Helvetica", 12),
    relief=tk.FLAT,
    bg="white",
    selectbackground="#b7e4c7",                      # green highlight for selected item
    selectforeground="black",
    yscrollcommand=scrollbar.set,                    # link scroll position to the scrollbar
    height=14
)
listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)              # scrollbar controls the listbox scroll


# --- 10. Action Buttons ---
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(fill=tk.X, padx=15, pady=8)

tk.Button(
    btn_frame,
    text="Mark Done",
    bg="#52b788",                                    # green
    fg="white",
    relief=tk.FLAT,
    padx=10, pady=6,
    cursor="hand2",
    command=toggle_done
).pack(side=tk.LEFT, padx=(0, 6))

tk.Button(
    btn_frame,
    text="Delete",
    bg="#e63946",                                    # red
    fg="white",
    relief=tk.FLAT,
    padx=10, pady=6,
    cursor="hand2",
    command=delete_task
).pack(side=tk.LEFT, padx=(0, 6))

tk.Button(
    btn_frame,
    text="Clear All",
    bg="#adb5bd",                                    # grey
    fg="white",
    relief=tk.FLAT,
    padx=10, pady=6,
    cursor="hand2",
    command=clear_all
).pack(side=tk.LEFT)


# --- 11. Status Bar ---
# StringVar means the Label text updates automatically whenever status_var changes.
status_var = tk.StringVar(value="0 task(s)   |   0 done")

tk.Label(
    root,
    textvariable=status_var,
    bg="#f0f4f8",
    fg="#6c757d",
    font=("Helvetica", 9)
).pack(pady=(0, 8))


# --- 12. Start the Event Loop ---
# mainloop() listens for events (clicks, key presses) and keeps the window open.
# It must always be the very last line of the script.
root.mainloop()
```

---

## How It Works

| Function | What it does |
|---|---|
| `refresh_list()` | Clears and redraws the Listbox from the `tasks` list |
| `add_task()` | Reads the Entry, appends to `tasks`, clears the field |
| `toggle_done()` | Flips the `done` flag and refreshes the list |
| `delete_task()` | Removes the selected task from `tasks` |
| `clear_all()` | Confirms with a dialog, then empties `tasks` |

## Key Tkinter Concepts Used

- **`StringVar`** — links the Entry widget to a Python variable so `.get()` and `.set()` stay in sync
- **`textvariable=`** — binds a widget's displayed text to a `StringVar`; updates automatically
- **`listbox.itemconfig(tk.END, fg=...)`** — changes the text colour of the last inserted item
- **`listbox.curselection()`** — returns a tuple of selected row indexes; empty tuple if nothing is selected
- **`root.bind("<Return>", ...)`** — fires a function when the Enter key is pressed anywhere in the window
- **`messagebox.askyesno()`** — shows a Yes/No dialog and returns `True` or `False`
