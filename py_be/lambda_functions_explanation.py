
"""
# A Deeper Dive into Python Lambda Functions

This file provides a focused and detailed explanation of lambda functions in Python,
exploring their syntax, use cases, and comparison with regular functions.
"""

# --- 1. What is a Lambda Function? ---
# A lambda function is a small, anonymous function defined with the `lambda` keyword.
# It's also known as an "anonymous function" because it doesn't have a name like
# functions defined with `def`.

# The syntax is: lambda arguments: expression

# - `lambda`: The keyword that declares a lambda function.
# - `arguments`: One or more arguments, separated by commas (e.g., x, y, z).
# - `expression`: A single expression that is evaluated and returned.

print("---\n1. Syntax and Basic Usage ---")

# A regular function to add two numbers
def add_regular(a, b):
    return a + b

# The equivalent lambda function
add_lambda = lambda a, b: a + b

print(f"Result from regular function: {add_regular(3, 4)}")
print(f"Result from lambda function: {add_lambda(3, 4)}")
print("Note: While you can assign a lambda to a variable, it's often not the primary use case.")
print()


# --- 2. Key Characteristics ---
# - Anonymous: They don't have a formal name.
# - Single Expression: They can only contain one expression, not a block of statements.
#   (e.g., no `if`, `for`, or `while` statements, and no `print()` calls inside).
# - Implicit Return: The result of the expression is automatically returned.

print("---\n2. Key Characteristics ---")
# Example: A lambda to check if a number is even
is_even = lambda x: x % 2 == 0
print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")
print()


# --- 3. Practical Use Cases: Where Lambdas Shine ---
# The real power of lambda functions is their use as a quick, one-time function
# passed as an argument to higher-order functions (functions that take other functions as arguments).

print("---\n3. Practical Use Cases ---")

# --- Use Case A: Sorting with `sorted()` ---
# `sorted()` can take a `key` argument, which is a function that tells it how to sort.
# Lambdas are perfect for this.

print("--- A. Sorting with `sorted()` ---")
# A list of tuples (student_name, grade)
students = [("Alice", 92), ("Bob", 85), ("Charlie", 95)]

# Sort by grade (the second element of the tuple)
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(f"Students sorted by grade: {sorted_by_grade}")

# A list of dictionaries
employees = [
    {'name': 'John', 'age': 35},
    {'name': 'Jane', 'age': 28},
    {'name': 'Dave', 'age': 42}
]

# Sort by age
sorted_by_age = sorted(employees, key=lambda employee: employee['age'])
print(f"Employees sorted by age: {sorted_by_age}")
print()


# --- Use Case B: Transforming with `map()` ---
# `map()` applies a function to every item in an iterable.

print("--- B. Transforming with `map()` ---")
numbers = [1, 2, 3, 4, 5]

# Square every number in the list
squared_numbers = map(lambda x: x ** 2, numbers)
print(f"Squared numbers (map object): {squared_numbers}")
print(f"Squared numbers (as a list): {list(squared_numbers)}")
print()


# --- Use Case C: Filtering with `filter()` ---
# `filter()` creates an iterator from elements of an iterable for which a function returns true.

print("--- C. Filtering with `filter()` ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out only the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"Even numbers (filter object): {even_numbers}")
print(f"Even numbers (as a list): {list(even_numbers)}")
print()


# --- 4. Limitations of Lambda Functions ---
# - They are restricted to a single expression. You cannot have multiple lines of logic.
# - They cannot contain statements like assignments (`x = 5`), loops (`for`), or conditionals (`if`).
#   (Though a ternary operator `val_if_true if condition else val_if_false` is an expression and is allowed).
# - They are not ideal for complex logic where a named `def` function with comments and a clear
#   structure would be more readable.

print("---\n4. Limitations ---")
# Example of using a ternary operator inside a lambda
check_age = lambda age: "Adult" if age >= 18 else "Minor"
print(f"A 25-year-old is an: {check_age(25)}")
print(f"A 15-year-old is a: {check_age(15)}")
print()

print("\n--- End of Lambda Functions Deeper Dive ---")
