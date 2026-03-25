# Tkinter Notebook Course: Building Tabs

The `ttk.Notebook` widget is used to create a tabbed interface (like a web browser or modern application settings). 

### Step 1: Basic Imports
You need both `tkinter` and `ttk`.
```python
import tkinter as tk
from tkinter import ttk
```

### Step 2: Main Window
Start by setting up your `Tk` instance.
```python
root = tk.Tk()
root.geometry("400x300")
```

### Step 3: Create the Notebook
The `Notebook` is the container for all the tabs.
```python
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")
```

### Step 4: Add Tabs (Frames)
Each tab is just a `ttk.Frame`. You add them using the `.add()` method.
```python
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1 Name")

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2 Name")
```

### Step 5: Put Widgets inside Tabs
When creating a label, button, or entry, set its parent to the specific **tab frame** you created in Step 4.
```python
# Put a label in Tab 1
label1 = tk.Label(tab1, text="This is inside the first tab!")
label1.pack(padx=20, pady=20)

# Put a button in Tab 2
button2 = tk.Button(tab2, text="Click Me in Tab 2")
button2.pack(padx=20, pady=20)
```

### Step 6: Start the App
```python
root.mainloop()
```

---

### Tips for Fast Development:
1. **Dynamic Tab Creation**: You can use a loop if you have many tabs.
2. **Tab Selection**: Use `notebook.select(tab_index)` to switch tabs programmatically.
3. **Closing Tabs**: Use `notebook.forget(tab_index)` to remove a tab.
