"""
# Python User Input: Interacting with Your Program

This file provides a focused explanation of how to get input from the user in Python
using the `input()` function. User input is essential for creating interactive programs.
"""

# --- 1. Basic `input()` Usage ---
# The `input()` function pauses your program and waits for the user to type something
# and press Enter. Whatever the user types is returned as a string.
# You can provide a prompt message as an argument to `input()`.

print("--- 1. Basic Input ---")

# Get a simple string input
# user_name = input("Please enter your name: ")
# print(f"Hello, {user_name}!")
# print("Type of user_name:", type(user_name))
# print()

# --- 2. `input()` Always Returns a String ---
# It's crucial to remember that `input()` always returns the user's entry as a string,
# even if they type numbers. If you need to perform numerical operations, you must
# explicitly convert the input string to the desired numeric type (e.g., `int()` or `float()`).

print("--- 2. Input is Always a String (and Type Conversion) ---")

# Attempting to do arithmetic directly with string input will cause an error
# num1_str = input("Enter a number: ")
# num2_str = input("Enter another number: ")
# # print(f"Concatenated result (string): {num1_str + num2_str}") # This concatenates strings, not adds numbers

# Correct way: Convert to integer
# try:
#     num1_int = int(num1_str)
#     num2_int = int(num2_str)
#     sum_int = num1_int + num2_int
#     print(f"Sum of integers: {sum_int}")
# except ValueError:
#     print("Invalid input for integer conversion. Please enter whole numbers.")

# Convert to float
# try:
#     num_float_str = input("Enter a decimal number: ")
#     num_float = float(num_float_str)
#     print(f"You entered: {num_float}, Type: {type(num_float)}")
# except ValueError:
#     print("Invalid input for float conversion. Please enter a valid decimal number.")
# print()


# --- 3. Handling Potential Errors with `try-except` ---
# When converting user input, it's good practice to use `try-except` blocks
# to gracefully handle cases where the user might enter invalid data (e.g., text
# when a number is expected).

print("--- 3. Error Handling for Input Conversion ---")

# while True:
#     age_str = input("Please enter your age: ")
#     try:
#         age = int(age_str)
#         if age < 0:
#             print("Age cannot be negative. Please try again.")
#         else:
#             print(f"You are {age} years old.")
#             break # Exit the loop if input is valid
#     except ValueError:
#         print("Invalid input. Please enter a whole number for your age.")
# print()


# --- 4. Getting Multiple Inputs ---
# You can prompt for multiple inputs sequentially or even on a single line (though
# single-line multiple inputs often require string splitting).

print("--- 4. Getting Multiple Inputs ---")

# Sequential inputs
# city = input("What city do you live in? ")
# country = input("What country is that in? ")
# print(f"So, you live in {city}, {country}.")

# Multiple inputs on one line (using .split())
# This is more advanced and assumes a specific separator (like space)
# print("Enter two numbers separated by a space (e.g., 10 20):")
# numbers_str = input()
# try:
#     num_str_list = numbers_str.split()
#     n1 = int(num_str_list[0])
#     n2 = int(num_str_list[1])
#     print(f"The numbers you entered are {n1} and {n2}.")
# except (ValueError, IndexError):
#     print("Invalid input. Please enter two numbers separated by a space.")
# print()


# --- 5. Practical Example: Simple Calculator ---

print("--- 5. Practical Example: Simple Calculator ---")

# print("Simple Calculator")
# try:
#     num1 = float(input("Enter the first number: "))
#     operator = input("Enter an operator (+, -, *, /): ")
#     num2 = float(input("Enter the second number: "))

#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#             result = "Undefined"
#         else:
#             result = num1 / num2
#     else:
#         print("Invalid operator.")
#         result = "N/A"

#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid number input. Please enter valid numbers.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# print()

print("\n--- End of Input Explanation ---")
