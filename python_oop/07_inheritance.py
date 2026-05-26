"""
# Python Inheritance: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Inheritance in Python. It covers single inheritance, multi-level chains,
multiple inheritance, MRO, super(), method overriding, mixins, and
the diamond problem.

Inheritance lets a class (child) derive attributes and methods from
another class (parent), promoting code reuse and hierarchical design.
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON INHERITANCE — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. Single Inheritance Basics ---")
# =====================================================================
# A child class inherits ALL attributes and methods from the parent.
# Syntax: class Child(Parent):

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says '{self.sound}!'"

    def describe(self):
        return f"{self.name} is an animal."

class Dog(Animal):
    """Dog inherits from Animal — gets speak() and describe() for free."""
    pass

rex = Dog("Rex", "Woof")
print(f"rex.speak()    -> {rex.speak()}")
print(f"rex.describe() -> {rex.describe()}")
print(f"isinstance(rex, Dog)    -> {isinstance(rex, Dog)}")
print(f"isinstance(rex, Animal) -> {isinstance(rex, Animal)}")


# =====================================================================
print("\n--- 2. Method Overriding ---")
# =====================================================================
# A child class can OVERRIDE a parent method by defining a method
# with the same name. The child's version takes precedence.

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")  # Call parent's __init__
        self.indoor = indoor

    def describe(self):
        """Override: more specific description for cats."""
        location = "indoor" if self.indoor else "outdoor"
        return f"{self.name} is an {location} cat."

whiskers = Cat("Whiskers", indoor=False)
print(f"whiskers.speak()    -> {whiskers.speak()}")     # Inherited
print(f"whiskers.describe() -> {whiskers.describe()}")  # Overridden


# =====================================================================
print("\n--- 3. The super() Function ---")
# =====================================================================
# super() returns a proxy object that delegates method calls to the
# parent class. It's essential for calling parent implementations.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)  # Initialize Vehicle part
        self.battery_kwh = battery_kwh       # Add EV-specific attribute

    def info(self):
        # Extend parent's info (not replace it)
        base = super().info()
        return f"{base} (Electric, {self.battery_kwh}kWh)"

ev = ElectricVehicle("Tesla", "Model 3", 2024, 75)
print(f"ev.info() -> {ev.info()}")
print(f"ev.make   -> {ev.make}")   # Inherited attribute


# =====================================================================
print("\n--- 4. Multi-Level Inheritance ---")
# =====================================================================
# Inheritance can chain through multiple levels: A → B → C.

class LivingThing:
    def breathe(self):
        return f"{type(self).__name__} is breathing."

class Mammal(LivingThing):
    def feed_young(self):
        return f"{type(self).__name__} feeds milk to young."

class Dolphin(Mammal):
    def swim(self):
        return f"{type(self).__name__} is swimming."

flipper = Dolphin()
print(f"flipper.breathe()    -> {flipper.breathe()}")     # From LivingThing
print(f"flipper.feed_young() -> {flipper.feed_young()}")  # From Mammal
print(f"flipper.swim()       -> {flipper.swim()}")        # Own method

# Inspect the inheritance chain
print(f"Dolphin MRO: {[c.__name__ for c in Dolphin.__mro__]}")


# =====================================================================
print("\n--- 5. Multiple Inheritance ---")
# =====================================================================
# Python supports inheriting from multiple parent classes.

class Flyable:
    def fly(self):
        return f"{type(self).__name__} is flying!"

class Swimmable:
    def swim(self):
        return f"{type(self).__name__} is swimming!"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Quack")

donald = Duck("Donald")
print(f"donald.speak() -> {donald.speak()}")  # From Animal
print(f"donald.fly()   -> {donald.fly()}")    # From Flyable
print(f"donald.swim()  -> {donald.swim()}")   # From Swimmable
print(f"Duck MRO: {[c.__name__ for c in Duck.__mro__]}")


# =====================================================================
print("\n--- 6. The Diamond Problem and MRO ---")
# =====================================================================
# The diamond problem occurs when a class inherits from two classes
# that share a common ancestor. Python solves this with C3 Linearization
# (Method Resolution Order — MRO).

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass  # Inherits greet from both B and C — which one wins?

d = D()
print(f"d.greet() -> {d.greet()}")  # B wins — it comes first in MRO
print(f"D MRO: {[cls.__name__ for cls in D.__mro__]}")

# super() follows MRO, not just the immediate parent
class E(B, C):
    def greet(self):
        return f"E says: {super().greet()}"  # Calls B.greet (next in MRO)

e = E()
print(f"e.greet() -> {e.greet()}")


# =====================================================================
print("\n--- 7. Cooperative Multiple Inheritance ---")
# =====================================================================
# For multiple inheritance to work smoothly, all classes should use
# super() — this ensures every class in the MRO gets initialized.

class Base:
    def __init__(self, **kwargs):
        # Base absorbs any remaining kwargs
        print(f"  Base.__init__ called (remaining kwargs: {kwargs})")

class Left(Base):
    def __init__(self, left_val, **kwargs):
        self.left_val = left_val
        print(f"  Left.__init__: left_val={left_val}")
        super().__init__(**kwargs)

class Right(Base):
    def __init__(self, right_val, **kwargs):
        self.right_val = right_val
        print(f"  Right.__init__: right_val={right_val}")
        super().__init__(**kwargs)

class Child(Left, Right):
    def __init__(self, child_val, **kwargs):
        self.child_val = child_val
        print(f"  Child.__init__: child_val={child_val}")
        super().__init__(**kwargs)

print("Creating Child — observe the MRO-driven init chain:")
c = Child(child_val="C", left_val="L", right_val="R")
print(f"c.child_val={c.child_val}, c.left_val={c.left_val}, c.right_val={c.right_val}")


# =====================================================================
print("\n--- 8. Mixins —  Reusable Behaviour Modules ---")
# =====================================================================
# A mixin is a class designed to be combined with other classes via
# multiple inheritance. It adds specific behaviour without being
# a standalone entity.

import json

class JsonMixin:
    """Mixin: adds JSON serialisation to any class with a to_dict method."""
    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

class LoggingMixin:
    """Mixin: adds simple logging capability."""
    def log(self, message):
        print(f"  [{type(self).__name__}] {message}")

class Server(JsonMixin, LoggingMixin):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def to_dict(self):
        return {"host": self.host, "port": self.port}

    def start(self):
        self.log(f"Starting on {self.host}:{self.port}")

srv = Server("0.0.0.0", 8080)
srv.start()
print(f"srv.to_json():\n{srv.to_json()}")


# =====================================================================
print("\n--- 9. isinstance() and issubclass() ---")
# =====================================================================

print(f"isinstance(rex, Dog)       -> {isinstance(rex, Dog)}")
print(f"isinstance(rex, Animal)    -> {isinstance(rex, Animal)}")
print(f"isinstance(rex, object)    -> {isinstance(rex, object)}")

print(f"issubclass(Dog, Animal)    -> {issubclass(Dog, Animal)}")
print(f"issubclass(Cat, Animal)    -> {issubclass(Cat, Animal)}")
print(f"issubclass(Dog, Cat)       -> {issubclass(Dog, Cat)}")
print(f"issubclass(Animal, object) -> {issubclass(Animal, object)}")


# =====================================================================
print("\n--- 10. Real-World Example: Employee Hierarchy ---")
# =====================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r}, age={self.age})"

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def annual_cost(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team = []

    def add_report(self, employee):
        self.team.append(employee)

    def annual_cost(self):
        """Manager cost includes a 20% management overhead."""
        return self.salary * 1.20

    def team_cost(self):
        return sum(e.annual_cost() for e in self.team) + self.annual_cost()

class Intern(Employee):
    def __init__(self, name, age, employee_id, salary, university):
        super().__init__(name, age, employee_id, salary)
        self.university = university

    def annual_cost(self):
        """Interns cost 80% of their salary (part-time)."""
        return self.salary * 0.80

mgr = Manager("Alice", 35, "M001", 120000, "Engineering")
dev = Employee("Bob", 28, "E001", 95000)
intern = Intern("Charlie", 21, "I001", 40000, "MIT")

mgr.add_report(dev)
mgr.add_report(intern)

print(f"mgr     -> {mgr}")
print(f"dev     -> {dev}")
print(f"intern  -> {intern}")
print(f"mgr.annual_cost()  -> ${mgr.annual_cost():,.2f}")
print(f"dev.annual_cost()  -> ${dev.annual_cost():,.2f}")
print(f"intern.annual_cost() -> ${intern.annual_cost():,.2f}")
print(f"mgr.team_cost()    -> ${mgr.team_cost():,.2f}")


print("\n" + "=" * 70)
print("  End of Python Inheritance Explanation")
print("=" * 70)
