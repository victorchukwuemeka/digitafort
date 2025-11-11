"""
# Python Functions: Defining and Using Reusable Code

This file provides a detailed explanation of how to define and use functions in Python.
Functions are a fundamental concept in programming that allow you to bundle a set of
instructions into a reusable block.
"""

# --- 1. What is a Function? ---
# A function is a named, reusable block of code that performs a specific task.
# Functions help break our program into smaller, modular chunks, making it more
# organized, readable, and manageable.

print("--- 1. Basic Function Definition and Calling ---")

# Defining a simple function
def greet():
    """This is a docstring. It explains what the function does."""
    print("Hello! Welcome to the world of functions.")

# Calling the function
# To execute the code inside a function, you must "call" it.
greet()
print()


# --- 2. Parameters and Arguments ---
# Functions can accept inputs, called "parameters," to work with.
# When you call a function, you provide values for these parameters, called "arguments."

print("--- 2. Functions with Parameters ---")

def greet_user(name): # 'name' is a parameter
    """Greets a user by their name."""
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_user("Alice") # "Alice" is an argument
greet_user("Bob")
print()


# --- 3. Return Values ---
# Functions can also send a result back to the caller using the 'return' statement.
# This is useful for calculations or operations where you need a result.

print("--- 3. Functions with Return Values ---")

def add_numbers(a, b):
    """Takes two numbers and returns their sum."""
    return a + b

# Calling the function and storing the result in a variable
sum_result = add_numbers(5, 3)
print(f"The sum is: {sum_result}")

# You can also use the result directly
print(f"The sum of 10 and 20 is: {add_numbers(10, 20)}")
print()


# --- 4. Default Arguments ---
# You can provide a default value for a parameter. If the caller doesn't provide
# an argument for it, the default value is used.

print("--- 4. Functions with Default Arguments ---")

def get_power(number, exponent=2):
    """Returns the number raised to the given exponent (defaults to 2)."""
    return number ** exponent

# Calling without providing the 'exponent' argument (uses default value 2)
print(f"5 squared is: {get_power(5)}")

# Calling and providing a specific 'exponent' argument
print(f"2 to the power of 3 is: {get_power(2, 3)}")
print()


# --- 5. Keyword Arguments ---
# You can specify which parameter an argument corresponds to by using the parameter's name.
# This can make your code more readable, and the order of arguments no longer matters.

print("--- 5. Using Keyword Arguments ---")

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type} named {pet_name}.")

# Calling with keyword arguments (order is flexible)
describe_pet(pet_name="Whiskers", animal_type="cat")
describe_pet(animal_type="dog", pet_name="Buddy")
print()


# --- 6. Arbitrary Arguments: *args and **kwargs ---
# Sometimes you don't know in advance how many arguments a function will receive.

print("--- 6. Arbitrary Arguments: *args and **kwargs ---")

# *args: for a variable number of non-keyword arguments (they are passed as a tuple)
def sum_all(*numbers):
    """Sums all the numbers passed as arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_all(10, 20, 30, 40)}")

# **kwargs: for a variable number of keyword arguments (they are passed as a dictionary)
def display_user_info(**user):
    """Displays user information from keyword arguments."""
    print("User Information:")
    for key, value in user.items():
        print(f"- {key.title()}: {value}")

display_user_info(name="Jane", age=29, city="London")
print()


# --- 7. Lambda Functions ---
# A lambda function is a small, anonymous function defined with the 'lambda' keyword.
# It can take any number of arguments, but can only have one expression.

print("--- 7. Lambda Functions ---")

# A lambda function that adds 10 to a number
add_ten = lambda x: x + 10
print(f"Using lambda: 5 + 10 = {add_ten(5)}")

# A lambda function that multiplies two numbers
multiply = lambda a, b: a * b
print(f"Using lambda: 3 * 4 = {multiply(3, 4)}")

# Lambdas are often used where a simple function is needed for a short period,
# for example, as an argument to another function like sorted() or map().
points = [(1, 2), (4, 1), (5, -1)]
# Sort the points based on the second element (y-coordinate)
points.sort(key=lambda point: point[1])
print(f"Points sorted by y-coordinate: {points}")
print()

print("\n--- End of Functions Explanation ---")
