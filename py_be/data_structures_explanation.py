"""
# Introduction to Python's Built-in Data Structures

    
Data structures are a way of organizing and storing data so that it can be accessed and
modified efficiently. Choosing the right data structure is crucial for writing clean,
efficient, and effective code.
"""

# --- 1. Lists ---
# Characteristics: Ordered, mutable (changeable), allows duplicate elements.
# Analogy: A shopping list where you can add, remove, or change items.

print("--- 1. Lists ---")

# When to use a List:
# - When you have a collection of items that needs to be in a specific order.
# - When you need to add, remove, or modify items in the collection.

# Example: A list of tasks in a to-do list.
tasks = ["Buy groceries", "Pay bills", "Walk the dog"]
print(f"Initial tasks: {tasks}")

# Adding a new task
tasks.append("Call the dentist")
print(f"After adding a task: {tasks}")

# Modifying a task
tasks[1] = "Pay electricity bill"
print(f"After modifying a task: {tasks}")

# Removing a task
tasks.remove("Walk the dog")
print(f"After removing a task: {tasks}")

# Accessing by index (order is preserved)
print(f"First task: {tasks[0]}")
print()







# --- 2. Tuples: The Immutable Sequence ---
# Characteristics: Ordered, immutable (unchangeable), allows duplicate elements.
# Analogy: A permanent record of a transaction, or a set of coordinates (x, y).

print("--- 2. Tuples: The Immutable Sequence ---")

# --- 2.1. Tuple Creation ---
print("\n--- 2.1. Tuple Creation ---")
# Using parentheses
my_tuple = (1, "hello", 3.14, "hello")
print(f"Standard tuple: {my_tuple}")

# Creating a single-element tuple (the trailing comma is crucial!)
single_item_tuple = ("just one",)
not_a_tuple = ("this is just a string")
print(f"A single-item tuple: {single_item_tuple}, type: {type(single_item_tuple)}")
print(f"Not a tuple: {not_a_tuple}, type: {type(not_a_tuple)}")

# Tuple packing (creating a tuple without parentheses)
# This is the process of creating a tuple by simply listing values separated by commas.
# Python automatically "packs" these values into a tuple.
packed_tuple = 10, 20, "thirty"
print(f"Packed tuple: {packed_tuple}, type: {type(packed_tuple)}")


# --- 2.2. Immutability in Detail ---
print("\n--- 2.2. Immutability in Detail ---")
# Once a tuple is created, you cannot change, add, or remove its elements.
# my_tuple[0] = 99 # This would raise a TypeError: 'tuple' object does not support item assignment

# The "gotcha" of immutability: If a tuple contains a mutable object (like a list),
# the contents of that mutable object CAN be changed.
mutable_tuple = (1, 2, [3, 4, 5])
print(f"Original mutable tuple: {mutable_tuple}")
mutable_tuple[2][0] = 99 # Change an element inside the list
print(f"Tuple after modifying the list inside it: {mutable_tuple}")
# The tuple itself hasn't changed; it still contains the same list object.

# --- 2.3. Tuple Unpacking ---
print("\n--- 2.3. Tuple Unpacking ---")
# Basic unpacking
a, b, c = packed_tuple
print(f"Unpacked values: a={a}, b={b}, c={c}")

# Extended unpacking (using *)
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# --- 2.4. Tuple Methods ---
print("\n--- 2.4. Tuple Methods ---")
# Tuples have only two methods because they are immutable.
# .count(value): returns the number of times a value appears
print(f"The word 'hello' appears {my_tuple.count('hello')} times in {my_tuple}")

# .index(value): returns the index of the first occurrence of a value
print(f"The first occurrence of 'hello' is at index {my_tuple.index('hello')}")

# --- 2.5. Why and When to Use Tuples (Use Cases) ---
print("\n--- 2.5. Why and When to Use Tuples ---")
# 1. Data Integrity: For data that should not change after creation.
#    e.g., Coordinates, RGB values, configuration settings.
point = (10, 20)

# 2. Returning Multiple Values from a Function: It's the standard way to return more than one value.
def get_user_info():
    return "Alice", 30, "alice@example.com" # Returns a tuple
name, age, email = get_user_info()
print(f"Function returned: Name={name}, Age={age}, Email={email}")

# 3. Dictionary Keys: Tuples can be used as dictionary keys because they are immutable and hashable.
#    A "hash" is a fixed-size integer that identifies a particular value. Only immutable objects are hashable.
#    Lists cannot be keys because their contents can change, which would change their hash.
location_data = {
    (40.7128, -74.0060): "New York City",
    (34.0522, -118.2437): "Los Angeles"
}
print(f"Data for {point}: {location_data.get(point, 'Not Found')}")

# --- 2.6. Performance and Memory ---
print("\n--- 2.6. Performance and Memory ---")
# Tuples are generally more memory-efficient than lists. Because they are immutable,
# Python can allocate the exact amount of memory needed. Lists, being dynamic,
# often allocate more memory than necessary to accommodate future appends efficiently.
# This also means iterating over a tuple can be slightly faster than iterating over a list.
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple_perf = (1, 2, 3, 4, 5)
print(f"Memory size of list: {sys.getsizeof(my_list)} bytes")
print(f"Memory size of tuple: {sys.getsizeof(my_tuple_perf)} bytes")

# --- 2.7. Advanced: Named Tuples ---
print("\n--- 2.7. Advanced: Named Tuples ---")
# Named tuples are a great way to create simple, readable, object-like structures without
# the overhead of a full class. They are part of the `collections` module.
from collections import namedtuple

# Create a 'Point' named tuple "class"
Point = namedtuple('Point', ['x', 'y', 'z'])

# Create instances of our new Point named tuple
p1 = Point(x=10, y=20, z=30)
p2 = Point(5, 15, 25) # Can also be instantiated positionally

print(f"Named tuple instance: {p1}")
# You can access elements by name (like an object) or by index (like a regular tuple).
print(f"Access by name (p1.x): {p1.x}")
print(f"Access by index (p1[1]): {p1[1]}")
print(f"p2.z = {p2.z}")
print()









# --- 3. Dictionaries ---
# Characteristics: Ordered (as of Python 3.7, insertion order is preserved), mutable,
# stores key-value pairs, keys must be unique and immutable (e.g., strings, numbers, tuples).
# Analogy: A real-world dictionary where you look up a word (key) to find its definition (value).

print("--- 3. Dictionaries ---")

# When to use a Dictionary:
# - When you need to associate unique keys with values for fast lookups.
# - When you need to represent structured data, like a record or a JSON object.
# - When the order of items is important (Python 3.7+).

# --- 3.1. Dictionary Creation ---
print("\n--- 3.1. Dictionary Creation ---")
# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with initial values
user_profile = {
    "username": "jdoe",
    "email": "jdoe@example.com",
    "is_active": True,
    "roles": ["admin", "editor"]
}
print(f"User profile: {user_profile}")

# Using dict() constructor
another_dict = dict(name="Alice", age=30)
print(f"Another dictionary: {another_dict}")

# --- 3.2. Accessing Elements ---
print("\n--- 3.2. Accessing Elements ---")
# Using square brackets (raises KeyError if key not found)
print(f"Username: {user_profile['username']}")

# Using .get() method (returns None or a default value if key not found)
print(f"Email (using .get()): {user_profile.get('email')}")
print(f"Phone (using .get(), key not found): {user_profile.get('phone')}")
print(f"Phone (using .get() with default): {user_profile.get('phone', 'N/A')}")

# --- 3.3. Adding and Updating Elements ---
print("\n--- 3.3. Adding and Updating Elements ---")
# Adding a new key-value pair
user_profile["last_login"] = "2023-10-27T10:00:00Z"
print(f"After adding last_login: {user_profile}")

# Modifying an existing value
user_profile["is_active"] = False
print(f"After modifying is_active: {user_profile}")

# Using .update() to add multiple items or update existing ones
user_profile.update({"city": "New York", "email": "jane.doe@example.com"})
print(f"After .update(): {user_profile}")

# --- 3.4. Removing Elements ---
print("\n--- 3.4. Removing Elements ---")
# Using `del` keyword
del user_profile["roles"]
print(f"After deleting 'roles': {user_profile}")

# Using .pop() (removes item with specified key and returns its value)
last_login_time = user_profile.pop("last_login")
print(f"Removed last_login: {last_login_time}, Dictionary now: {user_profile}")

# Using .popitem() (removes the last inserted item, Python 3.7+)
item = user_profile.popitem()
print(f"Removed last item with .popitem(): {item}, Dictionary now: {user_profile}")

# Using .clear() (removes all items)
user_profile.clear()
print(f"After .clear(): {user_profile}")

# --- 3.5. Iterating Through Dictionaries ---
print("\n--- 3.5. Iterating Through Dictionaries ---")
student_grades = {
    "Math": 90,
    "Science": 85,
    "History": 92
}

print("Iterating over keys:")
for subject in student_grades: # By default, iterates over keys
    print(f"Subject: {subject}")

print("Iterating over values (.values()):")
for grade in student_grades.values():
    print(f"Grade: {grade}")

print("Iterating over key-value pairs (.items()):")
for subject, grade in student_grades.items():
    print(f"{subject}: {grade}")

# --- 3.6. Nested Dictionaries ---
print("\n--- 3.6. Nested Dictionaries ---")
# Dictionaries can contain other dictionaries or lists as values.
company_data = {
    "employees": {
        "emp001": {"name": "Alice", "department": "HR"},
        "emp002": {"name": "Bob", "department": "IT"}
    },
    "locations": ["New York", "London"]
}
print(f"Company data: {company_data}")
print(f"Alice's department: {company_data['employees']['emp001']['department']}")
print(f"First location: {company_data['locations'][0]}")
print()


# --- 4. Sets ---
# Characteristics: Unordered, mutable, does not allow duplicate elements.
# Analogy: A collection of unique tags for a blog post.

print("--- 4. Sets ---")

# When to use a Set:
# - When you need to store a collection of unique items.
# - When you need to perform mathematical set operations like union, intersection, and difference.
# - For fast membership testing (checking if an item is in the collection).

# Example: Finding unique tags from a list that might have duplicates.
tags_list = ["python", "coding", "tips", "python", "guide"]
unique_tags = set(tags_list)
print(f"List with duplicate tags: {tags_list}")
print(f"Set of unique tags: {unique_tags}")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: all unique elements from both sets
union_set = set_a.union(set_b)
print(f"Union of {set_a} and {set_b}: {union_set}")

# Intersection: elements that are in both sets
intersection_set = set_a.intersection(set_b)
print(f"Intersection of {set_a} and {set_b}: {intersection_set}")

# Difference: elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print(f"Difference (A - B): {difference_set}")
print()

print("\n--- End of Data Structures Explanation ---")

