"""
# Python Classes and Objects: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Classes and Objects in Python. It covers class definition, object
instantiation, attributes, methods, class vs instance data, and
real-world design patterns.
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON CLASSES & OBJECTS — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. What Is a Class? ---")
# =====================================================================
# A class is a blueprint or template for creating objects. It defines:
#   - Attributes (data)
#   - Methods (behaviour)
# Think of a class as a cookie cutter, and objects as the cookies.

class Dog:
    """A simple Dog class to demonstrate the basics."""
    # Class-level attribute: shared by ALL instances
    species = "Canis familiaris"

    def __init__(self, name, breed, age):
        # Instance attributes: unique to each object
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        return f"{self.name} says: Woof!"

    def description(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

print("Class 'Dog' defined successfully.")
print(f"Dog.species (class attribute) -> {Dog.species}")


# =====================================================================
print("\n--- 2. Creating Objects (Instantiation) ---")
# =====================================================================
# An object is a specific instance of a class. Each object has its own
# copy of instance attributes but shares class attributes.

rex = Dog("Rex", "German Shepherd", 5)
bella = Dog("Bella", "Golden Retriever", 3)

print(f"rex.description()  -> {rex.description()}")
print(f"bella.description() -> {bella.description()}")
print(f"rex.speak()   -> {rex.speak()}")
print(f"bella.speak()  -> {bella.speak()}")

# Both share the class attribute
print(f"rex.species   -> {rex.species}")
print(f"bella.species  -> {bella.species}")
print(f"Same object?   -> {rex.species is bella.species}")


# =====================================================================
print("\n--- 3. Instance vs Class Attributes ---")
# =====================================================================
# Class attributes are defined directly in the class body.
# Instance attributes are defined in __init__ (or on the instance).
# If an instance attribute shadows a class attribute, the instance wins.

class Counter:
    """Demonstrates class vs instance attribute behaviour."""
    count = 0  # Class attribute: tracks total instances

    def __init__(self, label):
        self.label = label       # Instance attribute
        Counter.count += 1       # Modify class attribute via the class

c1 = Counter("Alpha")
c2 = Counter("Beta")
c3 = Counter("Gamma")

print(f"Counter.count     -> {Counter.count}")  # 3
print(f"c1.label          -> {c1.label}")
print(f"c2.label          -> {c2.label}")

# Shadowing: setting 'count' on an instance creates an instance attribute
c1.count = 999
print(f"c1.count (instance) -> {c1.count}")      # 999 (instance)
print(f"Counter.count (class) -> {Counter.count}")  # Still 3


# =====================================================================
print("\n--- 4. Adding and Deleting Attributes Dynamically ---")
# =====================================================================
# Python allows you to add or remove attributes on instances at runtime.

class Flexible:
    pass

obj = Flexible()
obj.x = 10
obj.y = 20
obj.label = "dynamic"

print(f"obj.x     -> {obj.x}")
print(f"obj.y     -> {obj.y}")
print(f"obj.label -> {obj.label}")
print(f"obj.__dict__ -> {obj.__dict__}")

del obj.label
print(f"After deleting 'label': {obj.__dict__}")


# =====================================================================
print("\n--- 5. Methods: Instance, Class, and Static ---")
# =====================================================================
# Instance methods: receive 'self', operate on instance data.
# Class methods:    receive 'cls', operate on class data.
# Static methods:   receive nothing, utility functions inside the class.

class MathUtils:
    """Demonstrates the three types of methods."""
    pi = 3.14159265

    def __init__(self, value):
        self.value = value

    # Instance method — accesses instance state via self
    def square(self):
        return self.value ** 2

    # Class method — accesses class state via cls
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    # Static method — no access to class or instance state
    @staticmethod
    def add(a, b):
        return a + b

m = MathUtils(7)
print(f"m.square()            -> {m.square()}")
print(f"MathUtils.circle_area(5) -> {MathUtils.circle_area(5):.4f}")
print(f"MathUtils.add(3, 4)      -> {MathUtils.add(3, 4)}")


# =====================================================================
print("\n--- 6. The __str__ and __repr__ Dunder Methods ---")
# =====================================================================
# __str__:  human-readable string (used by print())
# __repr__: unambiguous developer string (used in REPL, debugging)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

book = Book("Clean Code", "Robert C. Martin", 464)
print(f"str(book)  -> {str(book)}")
print(f"repr(book) -> {repr(book)}")


# =====================================================================
print("\n--- 7. Object Identity, Equality, and Type Checking ---")
# =====================================================================

a = Dog("Max", "Poodle", 2)
b = Dog("Max", "Poodle", 2)
c = a

print(f"a == b         -> {a == b}")       # False (default compares identity)
print(f"a is b         -> {a is b}")       # False (different objects)
print(f"a is c         -> {a is c}")       # True  (same object)
print(f"type(a)        -> {type(a)}")
print(f"isinstance(a, Dog) -> {isinstance(a, Dog)}")


# =====================================================================
print("\n--- 8. Implementing Custom Equality (__eq__) ---")
# =====================================================================

class Point:
    """A 2D point with proper equality semantics."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)

print(f"p1 == p2 -> {p1 == p2}")  # True (values match)
print(f"p1 == p3 -> {p1 == p3}")  # False
print(f"p1 is p2 -> {p1 is p2}")  # False (different objects)


# =====================================================================
print("\n--- 9. Real-World Example: Bank Account ---")
# =====================================================================

class BankAccount:
    """A simple bank account with deposit, withdraw, and transfer."""
    bank_name = "Python National Bank"

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"+{amount:.2f}")
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  ⚠ Insufficient funds for {self.owner}")
            return self
        self.balance -= amount
        self.transactions.append(f"-{amount:.2f}")
        return self

    def transfer(self, other, amount):
        if amount > self.balance:
            print(f"  ⚠ Cannot transfer: insufficient funds")
            return self
        self.withdraw(amount)
        other.deposit(amount)
        print(f"  💸 Transferred ${amount:.2f}: {self.owner} → {other.owner}")
        return self

    def statement(self):
        txns = ", ".join(self.transactions) if self.transactions else "None"
        return (f"[{self.bank_name}] {self.owner}: "
                f"${self.balance:.2f} | Txns: {txns}")

alice_acct = BankAccount("Alice", 1000)
bob_acct = BankAccount("Bob", 500)

alice_acct.deposit(250).withdraw(100).transfer(bob_acct, 300)
print(f"  {alice_acct.statement()}")
print(f"  {bob_acct.statement()}")


# =====================================================================
print("\n--- 10. Objects Are Everywhere ---")
# =====================================================================
# In Python, EVERYTHING is an object — integers, strings, lists,
# functions, even classes themselves.

print(f"type(42)          -> {type(42)}")
print(f"type('hello')     -> {type('hello')}")
print(f"type([1, 2, 3])   -> {type([1, 2, 3])}")
print(f"type(Dog)         -> {type(Dog)}")
print(f"type(print)       -> {type(print)}")
print(f"isinstance(42, object) -> {isinstance(42, object)}")


print("\n" + "=" * 70)
print("  End of Python Classes & Objects Explanation")
print("=" * 70)
