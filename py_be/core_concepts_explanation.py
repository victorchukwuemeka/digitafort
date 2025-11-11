
# Python Core Concepts: print(), Comments, Variables, and Input


# --- 1. The print() function ---
# The print() function is used to output messages, variables, or results to the console.
# It's essential for debugging and providing feedback to the user.

print("--- The print() function ---")

# Basic usage: printing a string literal
print("Hello, Python!")

# Printing a variable
message = "This is a variable."
print(message)

# Printing multiple items, separated by a comma (defaults to space separation)
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

# Using f-strings (formatted string literals) for more readable output (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# Changing the separator and end character
print("One", "Two", "Three", sep="-") # Separates items with a hyphen
print("This is the first line.", end=" ") # Prevents newline at the end
print("This is on the same line.")
print() # Prints an empty line

# --- 2. Code Comments ---
# Comments are crucial for making your code understandable to others and your future self.
# The Python interpreter ignores them.

print("--- Code Comments ---")

# This is a single-line comment. It starts with a hash symbol (#).
x = 10 # You can also add comments at the end of a line of code.

# Multi-line comments (docstrings) are typically used for documentation of modules,
# functions, classes, or methods. They are enclosed in triple quotes.
"""
This is a multi-line comment, also known as a docstring.
It can span multiple lines and is often used to explain
the purpose of a block of code or a function.
"""
print("Comments make code easier to understand.")

# --- 3. Variables ---
# Variables are containers for storing data values.
# In Python, you don't need to declare a variable with a specific type;
# the type is inferred when you assign a value to it.

print("--- Variables ---")

# Integer variable
quantity = 5
print(f"Quantity: {quantity}, Type: {type(quantity)}")

# String variable
product_name = "Laptop"
print(f"Product Name: {product_name}, Type: {type(product_name)}")

# Float variable
price = 1200.50
print(f"Price: {price}, Type: {type(price)}")

# Boolean variable
is_available = True
print(f"Is Available: {is_available}, Type: {type(is_available)}")

# Reassigning a variable (Python is dynamically typed)
quantity = "five" # Now 'quantity' holds a string
print(f"New Quantity: {quantity}, Type: {type(quantity)}")

# --- 4. Handling User Input ---
# The input() function allows your program to interact with the user
# by prompting them for information and capturing their response.

print("--- Handling User Input ---")

# Basic input: The input() function always returns a string.
# user_name = input("Please enter your name: ")
# print(f"Hello, {user_name}!")

# Converting input to other types:
# If you need numerical input, you must explicitly convert the string to an int or float.
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = float(input("Enter the second number (can be decimal): "))
#     sum_numbers = num1 + num2
#     print(f"The sum of {num1} and {num2} is {sum_numbers}")
# except ValueError:
#     print("Invalid input. Please enter valid numbers.")

print("\n--- End of Core Concepts Explanation ---")
