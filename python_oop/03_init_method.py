"""
# Python __init__ Method: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
the __init__ method in Python. It covers constructor mechanics, parameter
handling, default values, validation, delegation, and advanced patterns.

__init__ is the initializer (not constructor) — it runs immediately after
the object is created by __new__, allowing you to set up initial state.
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON __init__ METHOD — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. The Basics: What __init__ Does ---")
# =====================================================================
# __init__ is automatically called when you create an instance.
# Its job is to INITIALIZE the object's attributes.
# It receives 'self' (the newly created instance) as its first argument.

class Greeter:
    def __init__(self):
        # This runs automatically on Greeter()
        self.message = "Hello, World!"
        print(f"  __init__ was called! self.message = '{self.message}'")

g = Greeter()
print(f"g.message -> {g.message}")


# =====================================================================
print("\n--- 2. __init__ with Parameters ---")
# =====================================================================
# You pass arguments during instantiation; they are forwarded to __init__.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I'm {self.name}, {self.age} years old."

alice = Person("Alice", 30)
bob = Person("Bob", 25)
print(f"alice.introduce() -> {alice.introduce()}")
print(f"bob.introduce()   -> {bob.introduce()}")


# =====================================================================
print("\n--- 3. Default Parameter Values ---")
# =====================================================================
# Default values let you create objects with optional configuration.

class Config:
    def __init__(self, host="localhost", port=8080, debug=False):
        self.host = host
        self.port = port
        self.debug = debug

    def __repr__(self):
        return f"Config(host={self.host!r}, port={self.port}, debug={self.debug})"

default_cfg = Config()
custom_cfg = Config("0.0.0.0", 3000, debug=True)
print(f"default_cfg -> {default_cfg}")
print(f"custom_cfg  -> {custom_cfg}")


# =====================================================================
print("\n--- 4. The Mutable Default Argument Trap ---")
# =====================================================================
# NEVER use a mutable object (list, dict, set) as a default argument.
# It is shared across ALL instances because default values are evaluated
# once at function definition time.

# ❌ WRONG way:
class BrokenTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members  # All instances share the SAME list!

t1 = BrokenTeam("Alpha")
t1.members.append("Alice")

t2 = BrokenTeam("Beta")
print(f"  ❌ t2.members -> {t2.members}")  # ['Alice'] — leaked from t1!

# ✅ CORRECT way: use None as sentinel, create a new list inside __init__
class Team:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members is not None else []

t3 = Team("Gamma")
t3.members.append("Charlie")

t4 = Team("Delta")
print(f"  ✅ t4.members -> {t4.members}")  # [] — correctly isolated


# =====================================================================
print("\n--- 5. Input Validation Inside __init__ ---")
# =====================================================================
# __init__ is the ideal place to enforce invariants and validate data
# before the object enters a usable state.

class Temperature:
    """Temperature in Celsius with validation."""
    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError(f"Expected a number, got {type(celsius).__name__}")
        if celsius < self.ABSOLUTE_ZERO:
            raise ValueError(f"{celsius}°C is below absolute zero ({self.ABSOLUTE_ZERO}°C)")
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def __repr__(self):
        return f"Temperature({self.celsius}°C)"

t = Temperature(100)
print(f"t -> {t}")
print(f"t.to_fahrenheit() -> {t.to_fahrenheit()}")

# Validate that bad inputs are rejected
import sys
for bad_value in ["not_a_number", -300]:
    try:
        Temperature(bad_value)
    except (TypeError, ValueError) as e:
        print(f"  Correctly rejected {bad_value!r}: {e}")


# =====================================================================
print("\n--- 6. __init__ vs __new__ ---")
# =====================================================================
# __new__ creates the instance (allocates memory).
# __init__ initializes it (sets attributes).
# __new__ is rarely overridden; __init__ is the standard hook.

class Verbose:
    def __new__(cls, value):
        print(f"  __new__  called — creating instance of {cls.__name__}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print(f"  __init__ called — initializing with value={value}")
        self.value = value

v = Verbose(42)
print(f"v.value -> {v.value}")


# =====================================================================
print("\n--- 7. __init__ Must Return None ---")
# =====================================================================
# __init__ must ALWAYS return None (implicitly or explicitly).
# Returning anything else raises a TypeError.

class Safe:
    def __init__(self):
        self.status = "initialized"
        # return self  <-- would raise TypeError!

s = Safe()
result = Safe.__init__(s)
print(f"__init__ return value -> {result}")
print(f"s.status -> {s.status}")


# =====================================================================
print("\n--- 8. Using *args and **kwargs in __init__ ---")
# =====================================================================
# Flexible initialization for classes that accept variable arguments.

class FlexibleRecord:
    """Stores arbitrary key-value pairs as attributes."""
    def __init__(self, name, *tags, **metadata):
        self.name = name
        self.tags = list(tags)
        # Store each kwarg as an instance attribute
        for key, value in metadata.items():
            setattr(self, key, value)
        self._metadata_keys = list(metadata.keys())

    def __repr__(self):
        extras = {k: getattr(self, k) for k in self._metadata_keys}
        return f"FlexibleRecord(name={self.name!r}, tags={self.tags}, {extras})"

record = FlexibleRecord("Server-1", "production", "critical",
                         ip="10.0.0.1", region="us-east-1", cores=16)
print(f"record      -> {record}")
print(f"record.ip   -> {record.ip}")
print(f"record.cores -> {record.cores}")


# =====================================================================
print("\n--- 9. Calling __init__ in Inheritance (super().__init__) ---")
# =====================================================================
# When a subclass defines __init__, it must call the parent's __init__
# via super() to ensure proper initialization of inherited attributes.

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

class Pet(Animal):
    def __init__(self, name, sound, owner):
        super().__init__(name, sound)  # Initialize Animal's attributes
        self.owner = owner             # Add Pet-specific attribute

    def greet(self):
        return f"{self.name} ({self.sound}!) belongs to {self.owner}"

pet = Pet("Buddy", "Woof", "Alice")
print(f"pet.greet() -> {pet.greet()}")
print(f"pet.name    -> {pet.name}")   # Inherited from Animal
print(f"pet.owner   -> {pet.owner}")  # Defined in Pet


# =====================================================================
print("\n--- 10. Alternative Constructors with @classmethod ---")
# =====================================================================
# __init__ handles the standard construction path. For alternative ways
# to create objects, use @classmethod as a factory method.

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor: parse 'YYYY-MM-DD' string."""
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Alternative constructor: create a Date for today."""
        import datetime
        d = datetime.date.today()
        return cls(d.year, d.month, d.day)

    def __repr__(self):
        return f"Date({self.year:04d}-{self.month:02d}-{self.day:02d})"

d1 = Date(2025, 12, 25)
d2 = Date.from_string("2025-01-01")
d3 = Date.today()

print(f"d1 (standard)   -> {d1}")
print(f"d2 (from_string) -> {d2}")
print(f"d3 (today)       -> {d3}")


# =====================================================================
print("\n--- 11. Real-World Example: Database Connection ---")
# =====================================================================

class DatabaseConnection:
    """Simulates a database connection with full __init__ pattern."""
    _instance_count = 0

    def __init__(self, host, port, database, *, user="root", password="",
                 pool_size=5, timeout=30):
        DatabaseConnection._instance_count += 1
        self.connection_id = DatabaseConnection._instance_count
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.pool_size = pool_size
        self.timeout = timeout
        self.connected = False
        self._connect()

    def _connect(self):
        """Simulate establishing a connection."""
        self.connected = True
        print(f"  🔗 Connection #{self.connection_id}: "
              f"{self.user}@{self.host}:{self.port}/{self.database}")

    def __repr__(self):
        status = "connected" if self.connected else "disconnected"
        return (f"DatabaseConnection(#{self.connection_id}, "
                f"{self.host}:{self.port}/{self.database}, {status})")

db = DatabaseConnection("localhost", 5432, "myapp",
                         user="admin", pool_size=10)
print(f"db -> {db}")


print("\n" + "=" * 70)
print("  End of Python __init__ Method Explanation")
print("=" * 70)
