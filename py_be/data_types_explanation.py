"""
# Python Built-in Data Types

This file provides a detailed explanation and examples for Python's main built-in data types.
Each section includes a description and runnable code to demonstrate the data type's properties and usage.
"""

# --- 1. Text Type: str ---
# Strings are used to store text data. They are immutable, meaning they cannot be changed after creation.
# They are created by enclosing characters in single quotes (''), double quotes (""), or triple quotes (''' ''' or """ """).

print("--- Text Type: str ---")
first_name = "John"
last_name = 'Doe'
bio = """John is a software developer
who loves to code in Python."""

print(f"First Name: {first_name}, Type: {type(first_name)}")
print(f"Full Name: {first_name} {last_name}")
print(f"Bio: {bio}")
print()


# --- 2. Numeric Types: int, float, complex ---
# These are used to store numerical values.
# - int: For whole numbers (e.g., 10, -5, 0).
# - float: For numbers with a decimal point (e.g., 3.14, -0.5).
# - complex: For numbers with a real and imaginary part (e.g., 1 + 2j).

print("--- Numeric Types: int, float, complex ---")
integer_num = 100
float_num = 25.5
complex_num = 3 + 4j

print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")
print()


# --- 3. Sequence Types: list, tuple, range ---
# These are used to store ordered collections of items.

print("--- Sequence Types: list, tuple, range ---")

# list: A mutable (changeable), ordered collection. Allows duplicate members.
fruits_list = ["apple", "banana", "cherry", "apple"]
fruits_list.append("orange") # You can add items
fruits_list[1] = "blueberry" # You can change items
print(f"List: {fruits_list}, Type: {type(fruits_list)}")

# tuple: An immutable (unchangeable), ordered collection. Allows duplicate members.
fruits_tuple = ("apple", "banana", "cherry", "apple")
# fruits_tuple[1] = "blueberry" # This would cause a TypeError
print(f"Tuple: {fruits_tuple}, Type: {type(fruits_tuple)}")
print(f"First item in tuple: {fruits_tuple[0]}")

# range: Represents an immutable sequence of numbers, commonly used for looping.
num_range = range(5) # Generates numbers from 0 to 4
print(f"Range: {num_range}, Type: {type(num_range)}")
print("Numbers in range(5):", list(num_range)) # Convert to list to see the numbers
print()


# --- 4. Mapping Type: dict ---
# Dictionaries are used to store data values in key:value pairs.
# They are ordered (as of Python 3.7), mutable, and do not allow duplicate keys.

print("--- Mapping Type: dict ---")
person = {
    "name": "Jane Doe",
    "age": 28,
    "city": "New York"
}
person["email"] = "jane.doe@example.com" # Add a new key-value pair
person["age"] = 29 # Update a value
print(f"Dictionary: {person}, Type: {type(person)}")
print(f"Person's name: {person['name']}")
print()


# --- 5. Set Types: set, frozenset ---
# Sets are unordered, mutable collections of unique items. `frozenset` is an immutable version.

print("--- Set Types: set, frozenset ---")

# set: An unordered, mutable collection with no duplicate elements.
unique_fruits = {"apple", "banana", "cherry", "apple"} # The duplicate "apple" is removed
unique_fruits.add("orange")
print(f"Set: {unique_fruits}, Type: {type(unique_fruits)}")

# frozenset: An immutable version of a set.
frozen_unique_fruits = frozenset({"apple", "banana", "cherry"})
# frozen_unique_fruits.add("orange") # This would cause an AttributeError
print(f"Frozenset: {frozen_unique_fruits}, Type: {type(frozen_unique_fruits)}")
print()


# --- 6. Boolean Type: bool ---
# Used to represent one of two values: True or False.
# Often the result of comparison operations.

print("--- Boolean Type: bool ---")
is_active = True
has_permission = False
is_greater = 10 > 5

print(f"Is Active: {is_active}, Type: {type(is_active)}")
print(f"Has Permission: {has_permission}, Type: {type(has_permission)}")
print(f"Is 10 > 5? {is_greater}, Type: {type(is_greater)}")
print()


# --- 7. Binary Types: bytes, bytearray, memoryview ---
# These are used to handle binary data (sequences of bytes).

print("--- Binary Types: bytes, bytearray, memoryview ---")

# bytes: An immutable sequence of bytes.
byte_data = b"Hello"
print(f"Bytes: {byte_data}, Type: {type(byte_data)}")
print(f"First byte: {byte_data[0]}") # Prints the ASCII value of 'H'

# bytearray: A mutable sequence of bytes.
byte_array_data = bytearray(b"World")
byte_array_data[0] = 87 # Change 'W' (ASCII 87) to 'w' (ASCII 119)
byte_array_data[0] = 119
print(f"Bytearray: {byte_array_data}, Type: {type(byte_array_data)}")

# memoryview: A memory view on an object, allowing access to its internal data without copying.
mem_view = memoryview(byte_array_data)
print(f"Memory View: {mem_view}, Type: {type(mem_view)}")
print(f"Slice of memory view: {mem_view[1:4].tobytes()}")

print("\n--- End of Data Types Explanation ---")
