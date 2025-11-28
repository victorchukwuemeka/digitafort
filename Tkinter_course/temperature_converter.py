import tkinter as tk
from tkinter import messagebox
import sqlite3


# --- Functions for the buttons ---

def convert_temperature():
    """
    This function is called when the 'Convert' button is clicked.
    It converts temperature between Celsius and Fahrenheit.
    """
    # Get the text from the input fields
    celsius_text = celsius_entry.get()
    fahrenheit_text = fahrenheit_entry.get()

    try:
        if celsius_text:
            # If the Celsius field has text, convert it to Fahrenheit
            celsius_value = float(celsius_text)
            fahrenheit_result = (celsius_value * 9/5) + 32
            
            # Clear the Fahrenheit field and insert the new result
            fahrenheit_entry.delete(0, tk.END)
            fahrenheit_entry.insert(0, f"{fahrenheit_result:.2f}") # Format to 2 decimal places

        elif fahrenheit_text:
            # If the Fahrenheit field has text, convert it to Celsius
            fahrenheit_value = float(fahrenheit_text)
            celsius_result = (fahrenheit_value - 32) * 5/9

            # Clear the Celsius field and insert the new result
            celsius_entry.delete(0, tk.END)
            celsius_entry.insert(0, f"{celsius_result:.2f}") # Format to 2 decimal places
        
        else:
            # If both fields are empty, show a warning message
            messagebox.showwarning("Input Error", "Please enter a temperature in one of the fields.")

    except ValueError:
        # If the user enters text that is not a number, show an error message
        messagebox.showerror("Input Error", "Invalid temperature. Please enter only numbers.")

def clear_fields():
    """
    This function is called when the 'Clear' button is clicked.
    It removes all text from both input fields.
    """
    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)


# --- Create the main application window ---
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x150") # Set a fixed size for the window


# --- Create the widgets (labels, entry fields, buttons) ---

# Celsius label and entry field
celsius_label = tk.Label(root, text="Celsius:")
celsius_entry = tk.Entry(root, width=20)

# Fahrenheit label and entry field
fahrenheit_label = tk.Label(root, text="Fahrenheit:")
fahrenheit_entry = tk.Entry(root, width=20)

# Convert and Clear buttons
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
clear_button = tk.Button(root, text="Clear", command=clear_fields)


# --- Arrange the widgets in the window using the grid layout ---
celsius_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
celsius_entry.grid(row=0, column=1, padx=10, pady=5)

fahrenheit_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
fahrenheit_entry.grid(row=1, column=1, padx=10, pady=5)

convert_button.grid(row=2, column=0, columnspan=2, pady=10)
clear_button.grid(row=3, column=0, columnspan=2, pady=5)


# --- Start the application's main event loop ---
# This line keeps the window open and responsive to user actions.
root.mainloop()
