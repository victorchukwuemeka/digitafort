# Python Operators

"""
# --- What are Operators? ---
# Operators are special symbols in Python that carry out arithmetic or logical computation.
# The value that the operator operates on is called the operand.
# For example, in `a + b`, `+` is the operator and `a` and `b` are the operands.
"""

# --- 1. Arithmetic Operators ---
# Arithmetic operators are used to perform mathematical calculations.

print("--- 1. Arithmetic Operators ---")

# Addition (+)
# Adds two operands.
a = 10
b = 3
result_add = a + b
print(f"Addition ({a} + {b}): {result_add}") # Output: 13

# Subtraction (-)
# Subtracts the right operand from the left operand.
result_sub = a - b
print(f"Subtraction ({a} - {b}): {result_sub}") # Output: 7

# Multiplication (*)
# Multiplies two operands.
result_mul = a * b
print(f"Multiplication ({a} * {b}): {result_mul}") # Output: 30

# Division (/)
# Divides the left operand by the right operand. Always returns a float.
result_div = a / b
print(f"Division ({a} / {b}): {result_div}") # Output: 3.333...

# Modulus (%)
# Returns the remainder of the division.
result_mod = a % b
print(f"Modulus ({a} % {b}): {result_mod}") # Output: 1 (10 divided by 3 is 3 with a remainder of 1)

# Exponentiation (**)
# Raises the left operand to the power of the right operand.
result_exp = a ** b # 10 to the power of 3 (10*10*10)
print(f"Exponentiation ({a} ** {b}): {result_exp}") # Output: 1000

# Floor Division (//)
# Divides the left operand by the right operand and returns the integer part of the quotient.
result_floor_div = a // b
print(f"Floor Division ({a} // {b}): {result_floor_div}") # Output: 3
print()


# --- 2. Logical Operators ---
# Logical operators are used to combine conditional statements.
# They return boolean values (True or False).

print("--- 2. Logical Operators ---")

x = True
y = False
p = 5
q = 10

# and (Logical AND)
# Returns True if both statements are true.
result_and_1 = x and y
print(f"True and False: {result_and_1}") # Output: False

result_and_2 = (p < q) and (q > 5)
print(f"({p} < {q}) and ({q} > 5): {result_and_2}") # Output: True (True and True)

# or (Logical OR)
# Returns True if at least one of the statements is true.
result_or_1 = x or y
print(f"True or False: {result_or_1}") # Output: True

result_or_2 = (p > q) or (q == 10)
print(f"({p} > {q}) or ({q} == 10): {result_or_2}") # Output: True (False or True)

# not (Logical NOT)
# Reverses the result; returns False if the statement is true, and vice versa.
result_not_1 = not x
print(f"not True: {result_not_1}") # Output: False

result_not_2 = not (p == q)
print(f"not ({p} == {q}): {result_not_2}") # Output: True (not False)
print()

print("\n--- End of Operators Explanation ---")


# --- 3. Comparison Operators ---
# Comparison operators are used to compare two values.
# They return boolean values (True or False).

print("--- 3. Comparison Operators ---")

m = 10
n = 12

# Equal (==)
# Returns True if the values are equal.
print(f"{m} == {n}: {m == n}")  # Output: False

# Not Equal (!=)
# Returns True if the values are not equal.
print(f"{m} != {n}: {m != n}")  # Output: True

# Greater Than (>)
# Returns True if the left operand is greater than the right operand.
print(f"{m} > {n}: {m > n}")  # Output: False

# Less Than (<)
# Returns True if the left operand is less than the right operand.
print(f"{m} < {n}: {m < n}")  # Output: True

# Greater Than or Equal To (>=)
# Returns True if the left operand is greater than or equal to the right operand.
print(f"{m} >= {n}: {m >= n}")  # Output: False

# Less Than or Equal To (<=)
# Returns True if the left operand is less than or equal to the right operand.
print(f"{m} <= {n}: {m <= n}")  # Output: True
print()


# --- 4. Assignment Operators ---
# Assignment operators are used to assign values to variables.

print("--- 4. Assignment Operators ---")

c = 15  # Assigns 15 to c

# Add and Assign (+=)
c += 5  # Equivalent to c = c + 5
print(f"c += 5: {c}")  # Output: 20

# Subtract and Assign (-=)
c -= 3  # Equivalent to c = c - 3
print(f"c -= 3: {c}")  # Output: 17

# Multiply and Assign (*=)
c *= 2  # Equivalent to c = c * 2
print(f"c *= 2: {c}")  # Output: 34
print()


# --- 5. Bitwise Operators ---
# Bitwise operators perform operations on integers at the bit level.

print("--- 5. Bitwise Operators ---")

val1 = 6  # Binary: 0110
val2 = 2  # Binary: 0010

# Bitwise AND (&)
# Performs a bitwise AND on each pair of corresponding bits.
print(f"Bitwise AND ({val1} & {val2}): {val1 & val2}")  # Output: 2 (0010)

# Bitwise OR (|)
# Performs a bitwise OR on each pair of corresponding bits.
print(f"Bitwise OR ({val1} | {val2}): {val1 | val2}")  # Output: 6 (0110)
print()


# --- 6. Identity Operators ---
# Identity operators compare the memory locations of two objects.

print("--- 6. Identity Operators ---")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# is
# Returns True if both variables refer to the same object.
print(f"list1 is list2: {list1 is list2}")      # Output: False (different objects)
print(f"list1 is list3: {list1 is list3}")        # Output: True (same object)

# is not
# Returns True if both variables refer to different objects.
print(f"list1 is not list2: {list1 is not list2}")  # Output: True
print()


# --- 7. Membership Operators ---
# Membership operators test for membership in a sequence (e.g., strings, lists, tuples).

print("--- 7. Membership Operators ---")

message = "Hello, World!"
numbers = [1, 2, 3, 4, 5]

# in
# Returns True if a value is found in the sequence.
print(f"'H' in message: {'H' in message}")      # Output: True
print(f"6 in numbers: {6 in numbers}")          # Output: False

# not in
# Returns True if a value is not found in the sequence.
print(f"'z' not in message: {'z' not in message}")# Output: True
print(f"3 not in numbers: {3 not in numbers}")      # Output: False
print()

print("\n--- End of Operators Explanation ---")


