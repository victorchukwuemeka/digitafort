"""
# Python Operators: Arithmetic and Logical

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

