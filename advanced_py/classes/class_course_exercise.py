"""
========================================================
  Python Classes & OOP — Exercises
  Structured to match course outline (Parts I & II)
========================================================
Each exercise has:
  - A clear task description
  - Starter code (where helpful)
  - Expected output / hints
  - A "Challenge" extension

Run: python python_oop_exercises.py
"""

# ============================================================
# PART I – PYTHON CLASSES: CORE CONCEPTS
# ============================================================

print("=" * 55)
print("  PART I — Python Classes: Core Concepts")
print("=" * 55)

# ------------------------------------------------------------
# Exercise 1: Introduction to Classes
# ------------------------------------------------------------
print("\n--- Exercise 1: Introduction to Classes ---")
"""
TASK:
Create a class called `Book` with the following:
- An __init__ method that accepts: title, author, pages
- A method called `summary()` that returns a formatted string

Expected output:
  "Clean Code by Robert Martin — 464 pages"

CHALLENGE: Add a method `is_long_book()` that returns True
           if pages > 300, False otherwise.
"""

# YOUR CODE HERE ↓
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"{self.title} by {self.author} — {self.pages} pages"

    def is_long_book(self):
        return self.pages > 300

# Test your solution:
b1 = Book("Clean Code", "Robert Martin", 464)
b2 = Book("Python Crash Course", "Eric Matthes", 540)
print(b1.summary())
print(b2.summary())
print(f"Is '{b1.title}' a long book? {b1.is_long_book()}")


# ------------------------------------------------------------
# Exercise 2: Instance Attributes
# ------------------------------------------------------------
print("\n--- Exercise 2: Instance Attributes ---")
"""
TASK:
Create a class `Person` with:
- Attributes: name, age, city
- A method `introduce()` → "Hi, I'm Alice, 30, from Lagos."
- A method `move_to(new_city)` → updates the city

Verify that two Person objects are independent (changing one
doesn't affect the other).

CHALLENGE: Add a birthday() method that increments age by 1.
"""

# YOUR CODE HERE ↓
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age}, from {self.city}."

    def move_to(self, new_city):
        self.city = new_city

    def birthday(self):
        self.age += 1

# Test your solution:
p1 = Person("Alice", 30, "Lagos")
p2 = Person("Bob", 25, "Abuja")
print(p1.introduce())
p1.move_to("London")
print(p1.introduce())
print(p2.introduce())   # Bob should be unchanged


# ------------------------------------------------------------
# Exercise 3: Class Attributes
# ------------------------------------------------------------
print("\n--- Exercise 3: Class Attributes ---")
"""
TASK:
Create a class `Robot` with:
- A class attribute `manufacturer = "RoboTech"`
- A class attribute `robot_count = 0` (increments on each creation)
- Instance attributes: model, task
- A class method `get_fleet_info()` → "RoboTech fleet: 3 robots"

CHALLENGE: Add a class method `reset_count()` that resets
           robot_count to 0.
"""

# YOUR CODE HERE ↓
class Robot:
    manufacturer = "RoboTech"
    robot_count = 0

    def __init__(self, model, task):
        self.model = model
        self.task = task
        Robot.robot_count += 1

    @classmethod
    def get_fleet_info(cls):
        return f"{cls.manufacturer} fleet: {cls.robot_count} robots"

    @classmethod
    def reset_count(cls):
        cls.robot_count = 0

# Test your solution:
r1 = Robot("R2D2", "Navigation")
r2 = Robot("C3PO", "Translation")
r3 = Robot("HAL", "Operations")
print(Robot.get_fleet_info())
print(f"Manufacturer: {r1.manufacturer}")


# ------------------------------------------------------------
# Exercise 4: Instance Methods
# ------------------------------------------------------------
print("\n--- Exercise 4: Instance Methods ---")
"""
TASK:
Create a class `ShoppingCart` with:
- items: a list (starts empty)
- add_item(name, price): adds {"name": name, "price": price}
- remove_item(name): removes item by name
- total(): returns sum of all item prices
- display(): prints all items and total

CHALLENGE: Add a method `apply_discount(percent)` that
           reduces total by that percentage.
"""

# YOUR CODE HERE ↓
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        return self  # allows chaining

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def total(self):
        return sum(item["price"] for item in self.items)

    def display(self):
        print("Shopping Cart:")
        for item in self.items:
            print(f"  {item['name']:<20} ${item['price']:.2f}")
        print(f"  {'TOTAL':<20} ${self.total():.2f}")

    def apply_discount(self, percent):
        factor = 1 - (percent / 100)
        for item in self.items:
            item["price"] *= factor

# Test your solution:
cart = ShoppingCart()
cart.add_item("Python Book", 39.99).add_item("Keyboard", 89.99).add_item("Mouse", 29.99)
cart.display()
cart.remove_item("Mouse")
cart.apply_discount(10)  # 10% off
print("\nAfter removing Mouse and 10% discount:")
cart.display()


# ------------------------------------------------------------
# Exercise 5: Class Methods & Alternative Constructors
# ------------------------------------------------------------
print("\n--- Exercise 5: Class Methods ---")
"""
TASK:
Create a class `Circle` with:
- __init__(radius)
- class method `from_diameter(diameter)` → creates Circle using diameter
- class method `unit_circle()` → creates Circle with radius = 1
- instance method `area()` → π * r²
- instance method `circumference()` → 2 * π * r

CHALLENGE: Add a class attribute `pi = 3.14159` and use it
           instead of importing math.
"""

# YOUR CODE HERE ↓
import math

class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @classmethod
    def unit_circle(cls):
        return cls(1)

    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    def __str__(self):
        return f"Circle(r={self.radius:.2f})"

# Test your solution:
c1 = Circle(5)
c2 = Circle.from_diameter(10)
c3 = Circle.unit_circle()

for c in [c1, c2, c3]:
    print(f"{c} | Area: {c.area():.2f} | Circumference: {c.circumference():.2f}")


# ------------------------------------------------------------
# Exercise 6: Static Methods
# ------------------------------------------------------------
print("\n--- Exercise 6: Static Methods ---")
"""
TASK:
Create a class `StringUtils` with only static methods:
- `reverse(s)` → returns reversed string
- `is_palindrome(s)` → True if string reads same forwards/backwards
- `count_vowels(s)` → count of vowels in string
- `title_case(s)` → converts string to title case

CHALLENGE: Add `truncate(s, max_len, suffix="...")` that
           truncates long strings gracefully.
"""

# YOUR CODE HERE ↓
class StringUtils:
    @staticmethod
    def reverse(s):
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        cleaned = s.lower().replace(" ", "")
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_vowels(s):
        return sum(1 for ch in s.lower() if ch in "aeiou")

    @staticmethod
    def title_case(s):
        return s.title()

    @staticmethod
    def truncate(s, max_len, suffix="..."):
        if len(s) <= max_len:
            return s
        return s[:max_len - len(suffix)] + suffix

# Test your solution:
print(StringUtils.reverse("Python"))
print(StringUtils.is_palindrome("racecar"))
print(StringUtils.is_palindrome("hello"))
print(StringUtils.count_vowels("programming"))
print(StringUtils.title_case("python is great"))
print(StringUtils.truncate("The quick brown fox", 12))


# ------------------------------------------------------------
# Exercise 7: Magic / Dunder Methods
# ------------------------------------------------------------
print("\n--- Exercise 7: Magic / Dunder Methods ---")
"""
TASK:
Create a class `Fraction` that represents a mathematical fraction.
Implement:
- __init__(numerator, denominator)
- __str__ → "3/4"
- __repr__ → "Fraction(3, 4)"
- __add__ → adds two fractions (a/b + c/d = (a*d + b*c) / (b*d))
- __sub__ → subtracts fractions
- __mul__ → multiplies fractions
- __eq__ → checks if two fractions are equal
- A `simplify()` helper method using GCD

CHALLENGE: Implement __truediv__ and __lt__ / __gt__.
"""

# YOUR CODE HERE ↓
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common = gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

# Test your solution:
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f"f1 = {f1}, f2 = {f2}")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")
print(f"f1 == f2: {f1 == f2}")
print(f"f2 < f1: {f2 < f1}")


# ------------------------------------------------------------
# Exercise 8: Properties and Encapsulation
# ------------------------------------------------------------
print("\n--- Exercise 8: Properties and Encapsulation ---")
"""
TASK:
Create a class `Employee` with:
- Private attributes: __name, __salary, __department
- Properties (getters) for all three
- Salary setter with validation: must be >= 0
- Name setter with validation: must not be empty
- A method `get_annual_salary()` → salary * 12
- A method `give_raise(percent)` → increases salary

CHALLENGE: Add a `__str__` that shows only public info,
           and a property `salary_band` that returns
           "Junior" / "Mid" / "Senior" based on salary.
"""

# YOUR CODE HERE ↓
class Employee:
    def __init__(self, name, salary, department):
        self.name = name              # uses setter
        self.salary = salary          # uses setter
        self.__department = department

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = value.strip()

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = value

    @property
    def department(self):
        return self.__department

    @property
    def salary_band(self):
        if self.__salary < 50000:
            return "Junior"
        elif self.__salary < 100000:
            return "Mid"
        return "Senior"

    def get_annual_salary(self):
        return self.__salary * 12

    def give_raise(self, percent):
        self.__salary *= (1 + percent / 100)

    def __str__(self):
        return f"Employee: {self.__name} | Dept: {self.__department} | Band: {self.salary_band}"

# Test your solution:
emp = Employee("Grace Hopper", 75000, "Engineering")
print(emp)
print(f"Monthly: ${emp.salary:,.2f} | Annual: ${emp.get_annual_salary():,.2f}")
emp.give_raise(15)
print(f"After 15% raise: ${emp.salary:,.2f}")
print(f"New band: {emp.salary_band}")


# ------------------------------------------------------------
# Exercise 9: Object Introspection
# ------------------------------------------------------------
print("\n--- Exercise 9: Object Introspection ---")
"""
TASK:
Create a class `Config` with some attributes.
Then write a function `inspect_object(obj)` that:
- Prints the object's type
- Lists all non-dunder attributes and their values
- Checks for specific attributes using hasattr
- Dynamically sets a new attribute using setattr
- Retrieves it back using getattr

CHALLENGE: Filter out private attributes (starting with _)
           and only display public ones.
"""

# YOUR CODE HERE ↓
class Config:
    app_name = "MyApp"

    def __init__(self):
        self.debug = False
        self.version = "1.0.0"
        self.max_connections = 100
        self._secret_key = "hidden"     # protected
        self.__password = "supersecret" # private

    def reset(self):
        self.debug = False

def inspect_object(obj):
    print(f"\nInspecting: {type(obj).__name__}")
    print(f"Type: {type(obj)}")
    print("Public attributes:")
    for key, val in obj.__dict__.items():
        if not key.startswith("_"):
            print(f"  {key} = {val}")
    print(f"\nHas 'debug'? {hasattr(obj, 'debug')}")
    print(f"Has 'theme'? {hasattr(obj, 'theme')}")

    # Dynamically add attribute
    setattr(obj, "theme", "dark")
    print(f"After setattr — theme: {getattr(obj, 'theme')}")

# Test your solution:
cfg = Config()
inspect_object(cfg)


# ------------------------------------------------------------
# Exercise 10: Composition (Has-A Relationship)
# ------------------------------------------------------------
print("\n--- Exercise 10: Composition ---")
"""
TASK:
Model a `Computer` using composition:
- class `CPU` with: brand, cores, speed_ghz
- class `RAM` with: capacity_gb, type (DDR4/DDR5)
- class `Storage` with: capacity_gb, type (SSD/HDD)
- class `Computer` that has a CPU, RAM, and Storage

Computer should have a `specs()` method that prints
a full specification sheet.

CHALLENGE: Add a `is_gaming_ready()` method that returns
True if cores >= 8, RAM >= 16GB, and Storage >= 512GB.
"""

# YOUR CODE HERE ↓
class CPU:
    def __init__(self, brand, cores, speed_ghz):
        self.brand = brand
        self.cores = cores
        self.speed_ghz = speed_ghz

    def __str__(self):
        return f"{self.brand} — {self.cores} cores @ {self.speed_ghz}GHz"


class RAM:
    def __init__(self, capacity_gb, memory_type):
        self.capacity_gb = capacity_gb
        self.memory_type = memory_type

    def __str__(self):
        return f"{self.capacity_gb}GB {self.memory_type}"


class Storage:
    def __init__(self, capacity_gb, storage_type):
        self.capacity_gb = capacity_gb
        self.storage_type = storage_type

    def __str__(self):
        return f"{self.capacity_gb}GB {self.storage_type}"


class Computer:
    def __init__(self, brand, cpu, ram, storage):
        self.brand = brand
        self.cpu = cpu          # composed
        self.ram = ram          # composed
        self.storage = storage  # composed

    def specs(self):
        print(f"\n{'=' * 40}")
        print(f"  {self.brand} Specifications")
        print(f"{'=' * 40}")
        print(f"  CPU:     {self.cpu}")
        print(f"  RAM:     {self.ram}")
        print(f"  Storage: {self.storage}")
        print(f"{'=' * 40}")

    def is_gaming_ready(self):
        return (self.cpu.cores >= 8 and
                self.ram.capacity_gb >= 16 and
                self.storage.capacity_gb >= 512)

# Test your solution:
cpu = CPU("Intel Core i9", 12, 5.2)
ram = RAM(32, "DDR5")
ssd = Storage(1000, "NVMe SSD")

pc = Computer("Custom Gaming Rig", cpu, ram, ssd)
pc.specs()
print(f"Gaming ready? {pc.is_gaming_ready()}")


# ============================================================
# PART II – OBJECT-ORIENTED PROGRAMMING CONCEPTS
# ============================================================

print("\n" + "=" * 55)
print("  PART II — OOP Concepts")
print("=" * 55)

# ------------------------------------------------------------
# Exercise 11: Single Inheritance
# ------------------------------------------------------------
print("\n--- Exercise 11: Single Inheritance ---")
"""
TASK:
Create an inheritance hierarchy:

  Vehicle (base)
    ├── Car
    ├── Truck
    └── Motorcycle

Vehicle has: brand, year, fuel_type
             start(), stop(), fuel_info()

Car adds:    num_doors, trunk_capacity
Truck adds:  payload_tons, has_trailer
Motorcycle adds: is_sport

Each subclass should:
- Call super().__init__()
- Override a describe() method

CHALLENGE: Add a `Vehicle.age()` method that returns
           (current_year - self.year).
"""

# YOUR CODE HERE ↓
from datetime import date

class Vehicle:
    def __init__(self, brand, year, fuel_type):
        self.brand = brand
        self.year = year
        self.fuel_type = fuel_type
        self._running = False

    def start(self):
        self._running = True
        return f"{self.brand} started."

    def stop(self):
        self._running = False
        return f"{self.brand} stopped."

    def fuel_info(self):
        return f"Fuel type: {self.fuel_type}"

    def age(self):
        return date.today().year - self.year

    def describe(self):
        return f"{self.year} {self.brand} ({self.fuel_type})"


class Car(Vehicle):
    def __init__(self, brand, year, fuel_type, num_doors, trunk_capacity):
        super().__init__(brand, year, fuel_type)
        self.num_doors = num_doors
        self.trunk_capacity = trunk_capacity

    def describe(self):
        base = super().describe()
        return f"{base} | {self.num_doors}-door | Trunk: {self.trunk_capacity}L"


class Truck(Vehicle):
    def __init__(self, brand, year, fuel_type, payload_tons, has_trailer):
        super().__init__(brand, year, fuel_type)
        self.payload_tons = payload_tons
        self.has_trailer = has_trailer

    def describe(self):
        trailer = "with trailer" if self.has_trailer else "no trailer"
        return f"{super().describe()} | Payload: {self.payload_tons}t | {trailer}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, fuel_type, is_sport):
        super().__init__(brand, year, fuel_type)
        self.is_sport = is_sport

    def describe(self):
        style = "Sport" if self.is_sport else "Cruiser"
        return f"{super().describe()} | {style}"

# Test your solution:
vehicles = [
    Car("Toyota", 2020, "Petrol", 4, 500),
    Truck("Volvo", 2019, "Diesel", 20, True),
    Motorcycle("Ducati", 2022, "Petrol", True),
]

for v in vehicles:
    print(v.describe())
    print(f"  Age: {v.age()} years | {v.fuel_info()}")


# ------------------------------------------------------------
# Exercise 12: Polymorphism & Duck Typing
# ------------------------------------------------------------
print("\n--- Exercise 12: Polymorphism & Duck Typing ---")
"""
TASK:
Create a set of classes that all share a common interface
WITHOUT using formal inheritance:

  - Printer → print_document(content)
  - EmailSender → print_document(content)  (sends instead)
  - FileWriter → print_document(content)   (writes to string)

Then write a function `process_document(sender, content)`
that works with any of them.

This demonstrates duck typing — no shared base class needed.

CHALLENGE: Add a `CloudUploader` class that "uploads" the content.
"""

# YOUR CODE HERE ↓
class Printer:
    def print_document(self, content):
        print(f"[PRINTER] Printing: {content}")

class EmailSender:
    def __init__(self, recipient):
        self.recipient = recipient

    def print_document(self, content):
        print(f"[EMAIL] Sending to {self.recipient}: {content}")

class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.log = []

    def print_document(self, content):
        self.log.append(content)
        print(f"[FILE] Written to '{self.filename}': {content}")

class CloudUploader:
    def print_document(self, content):
        print(f"[CLOUD] Uploading to S3: {content[:30]}...")

def process_document(sender, content):
    """Works with ANY object that has print_document()"""
    sender.print_document(content)

# Test your solution:
handlers = [
    Printer(),
    EmailSender("boss@company.com"),
    FileWriter("output.txt"),
    CloudUploader(),
]

for handler in handlers:
    process_document(handler, "Q3 Financial Report — Confidential")


# ------------------------------------------------------------
# Exercise 13: Abstract Base Classes
# ------------------------------------------------------------
print("\n--- Exercise 13: Abstraction with ABC ---")
"""
TASK:
Create an abstract base class `PaymentMethod` with:
- Abstract methods: charge(amount), refund(amount)
- Concrete method: receipt(amount) → formatted receipt

Implement concrete classes:
  - CreditCard(card_number, holder_name)
  - PayPal(email)
  - CryptoCurrency(wallet_address, currency="BTC")

CHALLENGE: Add a transaction log to the base class
           that records all charges and refunds.
"""

# YOUR CODE HERE ↓
from abc import ABC, abstractmethod
from datetime import datetime

class PaymentMethod(ABC):
    def __init__(self):
        self._transactions = []

    @abstractmethod
    def charge(self, amount): pass

    @abstractmethod
    def refund(self, amount): pass

    def receipt(self, amount, action="Charge"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = f"[{timestamp}] {action}: ${amount:.2f} via {self.__class__.__name__}"
        self._transactions.append(entry)
        return entry

    def transaction_history(self):
        return "\n".join(self._transactions) if self._transactions else "No transactions."


class CreditCard(PaymentMethod):
    def __init__(self, card_number, holder_name):
        super().__init__()
        self.card_number = f"****-****-****-{card_number[-4:]}"
        self.holder_name = holder_name

    def charge(self, amount):
        return self.receipt(amount, "Charge") + f" | Card: {self.card_number}"

    def refund(self, amount):
        return self.receipt(amount, "Refund") + f" | Card: {self.card_number}"


class PayPal(PaymentMethod):
    def __init__(self, email):
        super().__init__()
        self.email = email

    def charge(self, amount):
        return self.receipt(amount, "Charge") + f" | PayPal: {self.email}"

    def refund(self, amount):
        return self.receipt(amount, "Refund") + f" | PayPal: {self.email}"


class CryptoCurrency(PaymentMethod):
    def __init__(self, wallet_address, currency="BTC"):
        super().__init__()
        self.wallet = wallet_address
        self.currency = currency

    def charge(self, amount):
        return self.receipt(amount, "Charge") + f" | {self.currency} Wallet: {self.wallet[:8]}..."

    def refund(self, amount):
        return self.receipt(amount, "Refund") + f" | {self.currency} Wallet: {self.wallet[:8]}..."

# Test your solution:
payments = [
    CreditCard("4111111111111111", "Ada Lovelace"),
    PayPal("ada@example.com"),
    CryptoCurrency("1A2B3C4D5E6F7G8H9I", "ETH"),
]

for method in payments:
    print(method.charge(99.99))
print()


# ------------------------------------------------------------
# Exercise 14: Design Patterns (Singleton + Factory)
# ------------------------------------------------------------
print("\n--- Exercise 14: Design Patterns ---")
"""
TASK A — Singleton:
Create a `Logger` class that:
- Only ever has ONE instance
- Has a log(message) method that stores messages
- Has a show_logs() method

TASK B — Factory:
Create a `NotificationFactory` that creates:
- SMSNotification(phone_number)
- PushNotification(device_id)
- EmailNotification(email)
Each has a send(message) method.

CHALLENGE: Add a `batch_send(messages)` method to each
           notification type.
"""

# YOUR CODE HERE ↓

# --- Singleton Pattern ---
class Logger:
    _instance = None
    _logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {message}"
        self._logs.append(entry)
        print(entry)

    def show_logs(self):
        print("\n--- All Logs ---")
        for log in self._logs:
            print(log)

# --- Factory Pattern ---
class Notification(ABC):
    @abstractmethod
    def send(self, message): pass

    def batch_send(self, messages):
        for msg in messages:
            self.send(msg)


class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.phone = phone_number

    def send(self, message):
        print(f"[SMS → {self.phone}] {message}")


class PushNotification(Notification):
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        print(f"[PUSH → {self.device_id}] {message}")


class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"[EMAIL → {self.email}] {message}")


class NotificationFactory:
    @staticmethod
    def create(notify_type, **kwargs):
        types = {
            "sms":   lambda: SMSNotification(kwargs["phone"]),
            "push":  lambda: PushNotification(kwargs["device_id"]),
            "email": lambda: EmailNotification(kwargs["email"]),
        }
        creator = types.get(notify_type.lower())
        if not creator:
            raise ValueError(f"Unknown notification type: {notify_type}")
        return creator()

# Test your solution:
log1 = Logger()
log2 = Logger()
print(f"Same instance? {log1 is log2}")
log1.log("App started")
log2.log("User logged in")
log1.show_logs()

print()
notifs = [
    NotificationFactory.create("sms", phone="+2349012345678"),
    NotificationFactory.create("push", device_id="device-abc-123"),
    NotificationFactory.create("email", email="user@example.com"),
]
for n in notifs:
    n.send("Your order has shipped!")


# ------------------------------------------------------------
# Exercise 15: Mini Project — RPG Battle System
# ------------------------------------------------------------
print("\n--- Exercise 15: Mini Project — RPG Battle ---")
"""
TASK:
Using OOP principles, build a small RPG battle system:

Classes:
  - Character (abstract base)
      attributes: name, health, attack_power, defense
      abstract methods: special_attack(target)
      concrete: take_damage(dmg), is_alive, __str__

  - Warrior(Character): special = "Shield Bash" (2x dmg, ignores defense)
  - Mage(Character): special = "Fireball" (3x dmg, magical)
  - Archer(Character): special = "Rapid Fire" (3 hits of 0.5x dmg each)

Then write:
  - simulate_battle(c1, c2): characters take turns attacking
    until one is defeated. Returns winner.

CHALLENGE: Add a Healer subclass with a `heal_ally(ally)` method,
           and a Team class that manages group battles.
"""

# YOUR CODE HERE ↓
import random

class Character(ABC):
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self._health = health
        self._max_health = health
        self.attack_power = attack_power
        self.defense = defense

    @property
    def health(self): return self._health

    @property
    def is_alive(self): return self._health > 0

    @abstractmethod
    def special_attack(self, target): pass

    def basic_attack(self, target):
        raw = self.attack_power + random.randint(0, 5)
        damage = max(1, raw - target.defense)
        target.take_damage(damage)
        return damage

    def take_damage(self, amount):
        self._health = max(0, self._health - amount)

    def __str__(self):
        bar_len = 20
        filled = int(bar_len * self._health / self._max_health)
        bar = "█" * filled + "░" * (bar_len - filled)
        return f"{self.name:<12} [{bar}] {self._health}/{self._max_health} HP"


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=18, defense=10)

    def special_attack(self, target):
        damage = self.attack_power * 2  # ignores defense
        target.take_damage(damage)
        return f"{self.name} uses SHIELD BASH on {target.name}! -{damage} HP"


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=28, defense=3)

    def special_attack(self, target):
        damage = self.attack_power * 3  # magical, ignores defense
        target.take_damage(damage)
        return f"{self.name} casts FIREBALL at {target.name}! 🔥 -{damage} HP"


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=16, defense=5)

    def special_attack(self, target):
        total = 0
        log = []
        for i in range(3):
            damage = max(1, int(self.attack_power * 0.5) - target.defense // 2)
            target.take_damage(damage)
            total += damage
            log.append(f"  Arrow {i+1}: -{damage} HP")
        result = f"{self.name} uses RAPID FIRE on {target.name}! Total: -{total} HP"
        return result + "\n" + "\n".join(log)


def simulate_battle(c1, c2):
    print(f"\n⚔️  BATTLE: {c1.name} vs {c2.name} ⚔️")
    print("=" * 50)
    turn = 0

    while c1.is_alive and c2.is_alive:
        turn += 1
        attacker, defender = (c1, c2) if turn % 2 == 1 else (c2, c1)

        # Use special every 3rd turn
        if turn % 3 == 0:
            result = attacker.special_attack(defender)
            print(f"\nTurn {turn} — SPECIAL:")
            print(f"  {result}")
        else:
            dmg = attacker.basic_attack(defender)
            print(f"\nTurn {turn}: {attacker.name} attacks {defender.name} for {dmg} dmg")

        print(f"  {c1}")
        print(f"  {c2}")

    winner = c1 if c1.is_alive else c2
    print(f"\n🏆 {winner.name} WINS after {turn} turns!")
    return winner

# Test your solution:
warrior = Warrior("Thor")
mage = Mage("Merlin")
winner = simulate_battle(warrior, mage)


# ============================================================
print("\n" + "=" * 55)
print("  All exercises complete!")
print("  Review the course .md for full theory & explanations.")
print("=" * 55)
