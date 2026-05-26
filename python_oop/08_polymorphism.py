"""
# Python Polymorphism: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Polymorphism in Python. It covers duck typing, method overriding,
operator overloading, abstract base classes, and protocol-based design.

Polymorphism ("many forms") lets different classes respond to the same
method name with their own specific behaviour, enabling flexible and
extensible code.
"""

# --- 0. Setup / Initial State ---
from abc import ABC, abstractmethod
import math

print("=" * 70)
print("  PYTHON POLYMORPHISM — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. Basic Polymorphism: Same Method, Different Behaviour ---")
# =====================================================================
# Different classes implement the same method name but with different
# logic. Code that calls this method works with ANY of these classes.

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}: Woof! Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}: Meow!"

class Parrot:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}: Polly wants a cracker!"

# Polymorphic function — works with ANY object that has a speak() method
def make_all_speak(animals):
    for animal in animals:
        print(f"  {animal.speak()}")

animals = [Dog("Rex"), Cat("Whiskers"), Parrot("Polly")]
make_all_speak(animals)
print("All three classes responded to the same speak() interface!")


# =====================================================================
print("\n--- 2. Duck Typing: 'If It Quacks Like a Duck...' ---")
# =====================================================================
# Python doesn't check types at compile time. If an object has the
# required method, it works — regardless of its class hierarchy.

class Robot:
    """Not an animal at all, but has a speak() method."""
    def __init__(self, model):
        self.name = model

    def speak(self):
        return f"{self.name}: BEEP BOOP. I am a robot."

# Robot has no relation to Dog/Cat/Parrot, but it works perfectly
mixed = [Dog("Buddy"), Robot("RX-7"), Cat("Luna")]
print("Duck typing in action:")
make_all_speak(mixed)


# =====================================================================
print("\n--- 3. Polymorphism Through Inheritance ---")
# =====================================================================
# Child classes override parent methods to provide specialised behaviour.
# Code written against the parent type works with all children.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        return (f"{type(self).__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"  {shape.describe()}")

# Polymorphic function
total_area = sum(s.area() for s in shapes)
print(f"Total area of all shapes: {total_area:.2f}")


# =====================================================================
print("\n--- 4. Abstract Base Classes (abc module) ---")
# =====================================================================
# ABCs enforce that subclasses implement required methods.
# You CANNOT instantiate an ABC directly.

class PaymentProcessor(ABC):
    """Abstract base class — defines the interface all processors must follow."""

    @abstractmethod
    def process_payment(self, amount):
        """Process a payment of the given amount."""
        pass

    @abstractmethod
    def refund(self, amount):
        """Refund the given amount."""
        pass

    def receipt(self, amount, action="Payment"):
        """Concrete method — shared by all subclasses."""
        return f"[{type(self).__name__}] {action}: ${amount:.2f}"

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return self.receipt(amount, "CC Payment")

    def refund(self, amount):
        return self.receipt(amount, "CC Refund")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return self.receipt(amount, "PayPal Payment")

    def refund(self, amount):
        return self.receipt(amount, "PayPal Refund")

# Cannot instantiate the abstract class
try:
    p = PaymentProcessor()
except TypeError as e:
    print(f"  Cannot instantiate ABC: {e}")

# Concrete subclasses work fine
processors = [CreditCardProcessor(), PayPalProcessor()]
for proc in processors:
    print(f"  {proc.process_payment(99.99)}")
    print(f"  {proc.refund(25.00)}")


# =====================================================================
print("\n--- 5. Operator Overloading (Dunder Methods) ---")
# =====================================================================
# Python lets you define how operators (+, -, *, ==, <, etc.) work
# with your custom objects by implementing special dunder methods.

class Vector:
    """2D vector with full operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Addition: v1 + v2
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Subtraction: v1 - v2
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Scalar multiplication: v * scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Reverse multiplication: scalar * v
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # Equality: v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Less than (by magnitude): v1 < v2
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    # Absolute value / magnitude: abs(v)
    def __abs__(self):
        return self.magnitude()

    # Length (dimension count): len(v)
    def __len__(self):
        return 2  # 2D vector always has 2 components

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 + v2    -> {v1 + v2}")
print(f"v1 - v2    -> {v1 - v2}")
print(f"v1 * 3     -> {v1 * 3}")
print(f"3 * v1     -> {3 * v1}")
print(f"v1 == v2   -> {v1 == v2}")
print(f"v1 == Vector(3, 4) -> {v1 == Vector(3, 4)}")
print(f"v2 < v1    -> {v2 < v1}")
print(f"abs(v1)    -> {abs(v1)}")
print(f"len(v1)    -> {len(v1)}")


# =====================================================================
print("\n--- 6. Polymorphism with Built-in Functions ---")
# =====================================================================
# Python's built-ins like len(), str(), iter() use polymorphism.
# They call the corresponding dunder methods on your objects.

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

    def __contains__(self, song):
        return song in self.songs

    def __iter__(self):
        return iter(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist("Chill Vibes", ["Song A", "Song B", "Song C", "Song D"])

print(f"len(playlist)          -> {len(playlist)}")
print(f"str(playlist)          -> {str(playlist)}")
print(f"'Song B' in playlist   -> {'Song B' in playlist}")
print(f"'Song Z' in playlist   -> {'Song Z' in playlist}")
print(f"playlist[0]            -> {playlist[0]}")
print(f"playlist[-1]           -> {playlist[-1]}")
print("Iterating: ", end="")
for song in playlist:
    print(song, end=" | ")
print()


# =====================================================================
print("\n--- 7. Method Resolution Order and Polymorphism ---")
# =====================================================================
# When multiple parents define the same method, MRO determines
# which version is called.

class A:
    def action(self):
        return "A.action"

class B(A):
    def action(self):
        return "B.action"

class C(A):
    def action(self):
        return "C.action"

class D(B, C):
    pass

d = D()
print(f"d.action() -> {d.action()}")  # B.action (B comes before C in MRO)
print(f"MRO: {' -> '.join(cls.__name__ for cls in D.__mro__)}")


# =====================================================================
print("\n--- 8. Real-World Example: Notification System ---")
# =====================================================================

class Notification(ABC):
    """Base notification with polymorphic send()."""

    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self):
        pass

    def __repr__(self):
        return f"{type(self).__name__}(to={self.recipient!r})"

class EmailNotification(Notification):
    def send(self):
        return f"📧 Email to {self.recipient}: {self.message}"

class SMSNotification(Notification):
    def send(self):
        return f"📱 SMS to {self.recipient}: {self.message}"

class PushNotification(Notification):
    def send(self):
        return f"🔔 Push to {self.recipient}: {self.message}"

class SlackNotification(Notification):
    def __init__(self, channel, message):
        super().__init__(channel, message)

    def send(self):
        return f"💬 Slack #{self.recipient}: {self.message}"

# Polymorphic dispatch — same interface, different implementations
notifications = [
    EmailNotification("alice@example.com", "Your order shipped!"),
    SMSNotification("+1234567890", "Verification code: 7742"),
    PushNotification("user_42", "New follower!"),
    SlackNotification("engineering", "Deploy v2.1 complete."),
]

print("Sending all notifications:")
for notif in notifications:
    print(f"  {notif.send()}")

print(f"\nTotal notifications sent: {len(notifications)}")


print("\n" + "=" * 70)
print("  End of Python Polymorphism Explanation")
print("=" * 70)
