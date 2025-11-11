"""
# Python Flow Control: if Statements, try...except, and Loops

This file provides a detailed explanation and examples for Python's flow control mechanisms.
"""

# --- 1. if Statements ---
# 'if' statements are used for conditional execution. They allow your program
# to make decisions and execute different blocks of code based on whether a condition is true or false.

print("---""- 1. if Statements ---""" ) 

temperature = 25

# Basic if statement
if temperature > 20:
    print("It's a warm day.")

# if-else statement
if temperature < 10:
    print("It's cold.")
else:
    print("It's not cold.")

# if-elif-else chain
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Nested if statements
age = 18
has_license = True
if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You are old enough, but need a license to drive.")
else:
    print("You are too young to drive.")
print()


# --- 2. try...except for Error Handling ---
# The 'try...except' block is used to handle potential errors (exceptions)
# that might occur during the execution of a program. This prevents the program
# from crashing and allows for graceful error recovery.

print("---""- 2. try...except for Error Handling ---""" ) 

# Example 1: Handling a ValueError (e.g., converting non-numeric string to int)
try:
    num_str = "abc"
    num = int(num_str)
    print(f"Converted number: {num}")
except ValueError:
    print(f"Error: Could not convert '{num_str}' to an integer.")

# Example 2: Handling a ZeroDivisionError
try:
    result = 10 / 0
    print(f"Result of division: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Example 3: Handling multiple exceptions and using 'finally'
try:
    value = int(input("Enter a number: ")) # This line will be commented out for non-interactive execution
    # value = 5 # Uncomment this for non-interactive testing
    result = 100 / value
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e: # Catch any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
else:
    # This block executes if no exception occurs in the try block
    print(f"Division successful. Result: {result}")
finally:
    # This block always executes, regardless of whether an exception occurred or not
    print("Execution of try-except block finished.")
print()


# --- 3. Loops: for and while ---
# Loops are used to execute a block of code repeatedly.

print("---""- 3. Loops: for and while ---""" ) 

# --- for loop ---
# Used for iterating over a sequence (like a list, tuple, string, or range)
# or other iterable objects.

print("---"" for loop examples ---""" ) 

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Looping through a string
for char in "Python":
    print(char)

# Looping using range()
print("Counting from 0 to 4:")
for i in range(5): # range(5) generates numbers 0, 1, 2, 3, 4
    print(i)

print("Counting from 2 to 9 (step of 2):")
for i in range(2, 10, 2): # range(start, stop, step)
    print(i)

# Looping with enumerate (to get index and value)
for index, fruit in enumerate(fruits):
    print(f"Fruit at index {index}: {fruit}")

# --- while loop ---
# Executes a block of code as long as a specified condition is true.

print("---"" while loop examples ---""" ) 

count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1 # Important: remember to change the condition to avoid infinite loops

# Using 'break' to exit a loop prematurely
print("Using 'break':")
i = 0
while True: # Infinite loop
    print(i)
    if i >= 2:
        break # Exit the loop when i is 2
    i += 1

# Using 'continue' to skip the rest of the current iteration
print("Using 'continue':")
for i in range(5):
    if i == 2:
        continue # Skip printing 2
    print(i)

print("\n---"" End of Flow Control Explanation ---""" ) 
