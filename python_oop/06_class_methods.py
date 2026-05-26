"""
# Python Class Methods: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Class Methods in Python. It covers instance methods, @classmethod,
@staticmethod, factory patterns, and when to use each type.

Python offers three flavours of methods:
  - Instance methods (self)  — operate on instance data
  - Class methods (cls)      — operate on class data
  - Static methods (none)    — utility functions scoped to the class
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON CLASS METHODS — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. Instance Methods (the default) ---")
# =====================================================================
# Instance methods take 'self' as the first parameter.
# They can read and modify instance state AND class state.

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old ({self.species})"

    # Instance method that modifies instance state
    def birthday(self):
        self.age += 1
        return f"🎂 {self.name} is now {self.age}!"

rex = Dog("Rex", 3)
print(f"rex.description() -> {rex.description()}")
print(f"rex.birthday()    -> {rex.birthday()}")
print(f"rex.age after birthday -> {rex.age}")


# =====================================================================
print("\n--- 2. Class Methods with @classmethod ---")
# =====================================================================
# A class method receives the CLASS (not the instance) as its first
# argument, conventionally named 'cls'. It can modify class-level state
# but has no access to instance-specific attributes.

class Employee:
    raise_percentage = 1.05  # 5% raise — shared by all employees
    _employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._employee_count += 1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percentage)
        return self.salary

    @classmethod
    def set_raise_percentage(cls, percentage):
        """Modify the raise percentage for ALL employees."""
        cls.raise_percentage = percentage
        print(f"  Raise percentage updated to {percentage}")

    @classmethod
    def get_employee_count(cls):
        """Access class-level data."""
        return cls._employee_count

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(f"Employee count: {Employee.get_employee_count()}")
print(f"Alice salary: ${e1.salary}")

Employee.set_raise_percentage(1.10)  # 10% raise for everyone
e1.apply_raise()
print(f"Alice salary after 10% raise: ${e1.salary}")


# =====================================================================
print("\n--- 3. Class Methods as Alternative Constructors ---")
# =====================================================================
# The most common use of @classmethod is to provide alternative ways
# to construct objects (factory methods).

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        """Parse 'YYYY-MM-DD' string into a Date object."""
        parts = date_string.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return cls(year, month, day)  # cls() so subclasses work correctly

    @classmethod
    def today(cls):
        """Create a Date for today."""
        import datetime
        d = datetime.date.today()
        return cls(d.year, d.month, d.day)

    @classmethod
    def from_timestamp(cls, timestamp):
        """Create a Date from a Unix timestamp."""
        import datetime
        d = datetime.date.fromtimestamp(timestamp)
        return cls(d.year, d.month, d.day)

    def __repr__(self):
        return f"Date({self.year:04d}-{self.month:02d}-{self.day:02d})"

d1 = Date(2025, 12, 25)
d2 = Date.from_string("2025-07-04")
d3 = Date.today()

print(f"Standard constructor:  {d1}")
print(f"from_string factory:   {d2}")
print(f"today factory:         {d3}")


# =====================================================================
print("\n--- 4. Static Methods with @staticmethod ---")
# =====================================================================
# Static methods don't receive self or cls. They are utility functions
# that logically belong to the class but don't need instance/class data.

class MathHelper:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def clamp(value, min_val, max_val):
        """Restrict value to [min_val, max_val] range."""
        return max(min_val, min(value, max_val))

print(f"MathHelper.is_even(4)     -> {MathHelper.is_even(4)}")
print(f"MathHelper.is_even(7)     -> {MathHelper.is_even(7)}")
print(f"MathHelper.factorial(6)   -> {MathHelper.factorial(6)}")
print(f"MathHelper.clamp(15, 0, 10) -> {MathHelper.clamp(15, 0, 10)}")


# =====================================================================
print("\n--- 5. When to Use Each Method Type ---")
# =====================================================================
# Decision guide:
#   - Need instance data?         → Instance method
#   - Need to modify class state? → Class method
#   - Alternative constructor?    → Class method
#   - Pure utility function?      → Static method

class Showcase:
    class_var = "shared"

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        """Has access to self AND cls (via self.__class__)."""
        return f"instance: self.value={self.value}, cls={self.__class__.class_var}"

    @classmethod
    def class_method(cls):
        """Has access to cls but NOT self."""
        return f"class: cls.class_var={cls.class_var}"

    @staticmethod
    def static_method():
        """No access to self or cls."""
        return "static: no access to instance or class data"

s = Showcase(42)
print(f"s.instance_method()       -> {s.instance_method()}")
print(f"Showcase.class_method()   -> {Showcase.class_method()}")
print(f"Showcase.static_method()  -> {Showcase.static_method()}")


# =====================================================================
print("\n--- 6. Class Methods and Inheritance ---")
# =====================================================================
# When a subclass calls an inherited @classmethod, 'cls' is the SUBCLASS,
# not the parent. This is critical for factory methods.

class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    @classmethod
    def create_default(cls):
        """Factory that uses cls — works correctly with subclasses."""
        return cls("Unknown", 4)

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, legs={self.legs})"

class Cat(Animal):
    pass

class Spider(Animal):
    @classmethod
    def create_default(cls):
        return cls("Unknown", 8)  # Spiders have 8 legs

generic = Animal.create_default()
cat = Cat.create_default()         # cls is Cat, not Animal
spider = Spider.create_default()

print(f"Animal.create_default() -> {generic}")
print(f"Cat.create_default()    -> {cat}")
print(f"type(cat) -> {type(cat)}")   # Cat, not Animal!
print(f"Spider.create_default() -> {spider}")


# =====================================================================
print("\n--- 7. Combining All Three Method Types ---")
# =====================================================================

class Temperature:
    """Full-featured temperature class using all method types."""

    def __init__(self, celsius):
        self._celsius = celsius

    # --- Instance methods ---
    def to_fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self._celsius + 273.15

    # --- Class method (factory) ---
    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    @classmethod
    def from_kelvin(cls, k):
        return cls(k - 273.15)

    # --- Static method (utility) ---
    @staticmethod
    def is_boiling(celsius):
        return celsius >= 100

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0

    def __repr__(self):
        return f"Temperature({self._celsius:.1f}°C)"

t1 = Temperature(100)
t2 = Temperature.from_fahrenheit(212)
t3 = Temperature.from_kelvin(373.15)

print(f"t1 = {t1}, F={t1.to_fahrenheit():.1f}, K={t1.to_kelvin():.1f}")
print(f"t2 (from 212°F) = {t2}")
print(f"t3 (from 373.15K) = {t3}")
print(f"Is 100°C boiling? {Temperature.is_boiling(100)}")
print(f"Is -5°C freezing? {Temperature.is_freezing(-5)}")


# =====================================================================
print("\n--- 8. Real-World Example: JSON Serializable Model ---")
# =====================================================================

import json

class Product:
    """Product with instance, class, and static methods."""

    _catalog = []  # Class-level product catalog

    def __init__(self, name, price, category="General"):
        self.name = name
        self.price = price
        self.category = category
        Product._catalog.append(self)

    # Instance method: serialise this object
    def to_dict(self):
        return {"name": self.name, "price": self.price, "category": self.category}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

    # Class method: deserialise from dict
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data.get("category", "General"))

    # Class method: access class state
    @classmethod
    def catalog_summary(cls):
        total = sum(p.price for p in cls._catalog)
        return f"{len(cls._catalog)} products, total value: ${total:.2f}"

    # Static method: utility
    @staticmethod
    def format_price(amount):
        return f"${amount:,.2f}"

    def __repr__(self):
        return f"Product({self.name!r}, {Product.format_price(self.price)})"

p1 = Product("Laptop", 999.99, "Electronics")
p2 = Product("Book", 24.99, "Education")
p3 = Product.from_dict({"name": "Mouse", "price": 49.99, "category": "Electronics"})

print(f"p1 -> {p1}")
print(f"p1.to_json():\n{p1.to_json()}")
print(f"p3 (from_dict) -> {p3}")
print(f"Catalog: {Product.catalog_summary()}")
print(f"Formatted: {Product.format_price(1234567.89)}")


print("\n" + "=" * 70)
print("  End of Python Class Methods Explanation")
print("=" * 70)
