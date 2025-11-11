"""
# Python GUI Development with CustomTkinter

This file provides an introduction to creating modern graphical user interfaces (GUIs)
in Python using the CustomTkinter library.

**What is CustomTkinter?**
CustomTkinter is a Python UI-library based on Tkinter that provides modern, fully
customizable widgets. It allows for a more visually appealing user interface than
standard Tkinter and has built-in support for light and dark modes.

**Prerequisites:**
You must install the library first. You can do this by running the following
command in your terminal:
`pip install customtkinter`
"""

import customtkinter

# --- 1. Setting up the Main Application Window ---

# Set the appearance mode and default color theme.
# "System" will follow the OS's theme. Other options: "Light", "Dark".
customtkinter.set_appearance_mode("System")
# Themes: "blue" (default), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

# Create the main application window object
app = customtkinter.CTk()
app.title("My First CustomTkinter App")
app.geometry("400x300") # Set window size


# --- 2. Creating and Placing Widgets ---
# Widgets are the building blocks of your GUI (e.g., labels, buttons, entry fields).
# We will place them inside a frame for better organization.

# Create a frame to hold the widgets
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Create a Label widget
label = customtkinter.CTkLabel(master=frame, text="Enter Your Name")
# .pack() is a simple way to place widgets in the window.
label.pack(pady=12, padx=10)

# Create an Entry widget (for text input)
entry = customtkinter.CTkEntry(master=frame, placeholder_text="Your name...")
entry.pack(pady=12, padx=10)


# --- 3. Handling Events (Button Clicks) ---
# We can define a function that gets called when an event, like a button press, occurs.

def button_callback():
    """This function is called when the button is pressed."""
    user_name = entry.get()
    if user_name:
        print(f"Button clicked! Hello, {user_name}")
        label.configure(text=f"Hello, {user_name}!")
    else:
        print("Button clicked, but no name was entered.")
        label.configure(text="Please enter a name.")

# Create a Button widget
# The `command` parameter is set to the function we want to execute on click.
button = customtkinter.CTkButton(master=frame, text="Greet Me", command=button_callback)
button.pack(pady=12, padx=10)


# --- 4. Running the Application ---
# The `app.mainloop()` call starts the Tkinter event loop. It listens for events
# (like button clicks or key presses) and keeps the window open until it is closed.
# This line should always be at the end of your script.

print("Starting the CustomTkinter application...")
app.mainloop()
print("Application closed.")

print("\n--- End of CustomTkinter Explanation ---")
