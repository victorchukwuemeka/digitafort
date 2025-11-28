"""
# Python Loops: for and while

This file provides a beginner-friendly explanation of loops in Python,
focusing on `for` and `while` loops with simple, easy-to-understand examples.
"""

# --- What are Loops? ---
# In programming, a loop is a control structure that allows you to execute a
# block of code repeatedly. This is useful when you need to perform the same
# action multiple times, such as processing items in a list or counting.

print("---"What are Loops?"---")
print("Loops help us repeat a set of actions without writing the same code over and over.")
print()


# --- 1. The `for` Loop ---
# A `for` loop is used for iterating over a sequence (that is either a list,
# a tuple, a dictionary, a set, or a string) or other iterable objects.

print("---"1. The `for` Loop"---")

# Example 1: Looping through a list of fruits
print("Example 1: Looping through a list of fruits")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I have a {fruit}.")
print()

# Example 2: Looping through a string
print("Example 2: Looping through the letters of a word")
for letter in "Python":
    print(f"Letter: {letter}")
print()

# Example 3: Using the range() function to loop a specific number of times
print("Example 3: Counting from 0 to 4")
for i in range(5):  # range(5) generates numbers from 0 up to (but not including) 5
    print(f"Number: {i}")
print()


# --- 2. The `while` Loop ---
# A `while` loop executes a block of code as long as a specified condition is true.
# It's important to make sure the condition will eventually become false,
# otherwise, you'll create an infinite loop!

print("---"2. The `while` Loop"---")

# Example 1: A simple counter
print("Example 1: A simple counter from 1 to 3")
count = 1
while count <= 3:
    print(f"The count is: {count}")
    count = count + 1  # Increment the counter to eventually end the loop
print("Loop finished!")
print()

# Example 2: A guessing game
# In a real game, you might get input from the user. Here, we'll simulate it.
print("Example 2: A simple guessing game")
secret_number = 7
guess = 0
while guess != secret_number:
    print(f"You guessed {guess}. That's not it!")
    # In a real game, you'd ask for a new guess. Here we'll just increment.
    guess += 1
print(f"You guessed {guess}. You got it! It was {secret_number}.")
print()


# --- Loop Control Statements: `break` and `continue` ---
# You can control the flow of a loop using `break` and `continue`.

print("---"Loop Control: `break` and `continue`"---")

# `break`: Exits the loop entirely.
print("Using `break` to stop at the number 2:")
for i in range(5):
    if i == 2:
        break  # Stop the loop when i is 2
    print(i)
print()

# `continue`: Skips the rest of the current iteration and moves to the next one.
print("Using `continue` to skip the number 2:")
for i in range(5):
    if i == 2:
        continue  # Skip this iteration when i is 2
    print(i)
print()

print("\n---"End of Loops Explanation"---")