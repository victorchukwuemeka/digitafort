"""
# Python Encapsulation: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Encapsulation in Python. It covers access modifiers, name mangling,
properties as access control, defensive copying, and encapsulation
patterns.

Encapsulation is the bundling of data and methods into a single unit (class)
while restricting direct access to internal implementation details.
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON ENCAPSULATION — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. Python's Access Convention: Public, Protected, Private ---")
# =====================================================================
# Python has NO true access modifiers (unlike Java/C++).
# Instead, it uses NAMING CONVENTIONS:
#   public     -> name        (accessible everywhere)
#   protected  -> _name       (convention: internal use, not enforced)
#   private    -> __name      (name mangling: harder to access externally)

class AccessDemo:
    def __init__(self):
        self.public = "I am public"          # Anyone can access
        self._protected = "I am protected"   # Convention: treat as internal
        self.__private = "I am private"      # Name mangling applied

obj = AccessDemo()
print(f"obj.public       -> {obj.public}")
print(f"obj._protected   -> {obj._protected}")

# Direct access to __private fails
try:
    print(obj.__private)
except AttributeError as e:
    print(f"obj.__private    -> AttributeError: {e}")

# But name mangling means it's stored as _ClassName__attribute
print(f"obj._AccessDemo__private -> {obj._AccessDemo__private}")
print("⚠ Name mangling doesn't enforce privacy — it just discourages access.")


# =====================================================================
print("\n--- 2. Why Encapsulation Matters ---")
# =====================================================================
# Without encapsulation, any code can modify internal state arbitrarily,
# leading to broken invariants and hard-to-find bugs.

# ❌ No encapsulation — anyone can corrupt the data
class UnsafeBankAccount:
    def __init__(self, balance):
        self.balance = balance

unsafe = UnsafeBankAccount(1000)
unsafe.balance = -999999  # No validation, no protection!
print(f"❌ Unsafe account balance: {unsafe.balance}")

# ✅ With encapsulation — controlled access
class SafeBankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

safe = SafeBankAccount(1000)
safe.deposit(500)
safe.withdraw(200)
print(f"✅ Safe account balance: {safe.balance}")

try:
    safe.balance = -999  # Cannot set directly
except AttributeError as e:
    print(f"  Cannot set balance directly: {e}")


# =====================================================================
print("\n--- 3. Name Mangling Deep Dive ---")
# =====================================================================
# Any attribute starting with __ (double underscore) and NOT ending
# with __ gets mangled to _ClassName__attribute.

class Secret:
    def __init__(self):
        self.__hidden = 42
        self._single = 100
        self.__dunder__ = "not mangled"  # Dunder names are NOT mangled

    def reveal(self):
        """The class itself can access __hidden normally."""
        return self.__hidden

s = Secret()
print(f"s.reveal()         -> {s.reveal()}")
print(f"s._single          -> {s._single}")
print(f"s.__dunder__       -> {s.__dunder__}")

# Inspect all attributes
print(f"s.__dict__ -> {s.__dict__}")
# Shows: {'_Secret__hidden': 42, '_single': 100, '__dunder__': 'not mangled'}


# =====================================================================
print("\n--- 4. Name Mangling in Inheritance ---")
# =====================================================================
# Name mangling prevents subclasses from accidentally overriding
# parent's private attributes. Each class gets its own mangled name.

class Parent:
    def __init__(self):
        self.__value = "parent's private"

    def get_value(self):
        return self.__value

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "child's private"  # Does NOT override parent's!

    def get_child_value(self):
        return self.__value

c = Child()
print(f"c.get_value()       -> {c.get_value()}")        # Parent's __value
print(f"c.get_child_value() -> {c.get_child_value()}")  # Child's __value
print(f"c.__dict__ -> {c.__dict__}")
# Both _Parent__value and _Child__value coexist!


# =====================================================================
print("\n--- 5. Encapsulation with Properties (Getter/Setter) ---")
# =====================================================================
# Properties are the Pythonic way to implement encapsulation.
# They provide a clean public interface while controlling access.

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @property
    def annual_salary(self):
        """Read-only computed property."""
        return self._salary * 12

emp = Employee("Alice", 5000)
print(f"emp.name           -> {emp.name}")
print(f"emp.salary         -> {emp.salary}")
print(f"emp.annual_salary  -> {emp.annual_salary}")

emp.salary = 6000
print(f"After raise: salary={emp.salary}, annual={emp.annual_salary}")

for bad in [-100, "not_a_number"]:
    try:
        emp.salary = bad
    except (ValueError, TypeError) as e:
        print(f"  Rejected salary={bad!r}: {e}")


# =====================================================================
print("\n--- 6. Defensive Copying ---")
# =====================================================================
# When your class stores mutable data (lists, dicts), return copies
# instead of references to prevent external code from mutating internals.

class Gradebook:
    def __init__(self, student, grades):
        self._student = student
        self._grades = list(grades)  # Defensive copy on input

    @property
    def grades(self):
        return list(self._grades)    # Defensive copy on output

    def add_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError(f"Grade must be 0-100, got {grade}")
        self._grades.append(grade)

    @property
    def average(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0

original = [90, 85, 92]
gb = Gradebook("Alice", original)

# Mutating the original list does NOT affect the gradebook
original.append(0)
print(f"original list:  {original}")
print(f"gb.grades:      {gb.grades}")  # Unaffected!

# Mutating the returned list does NOT affect the gradebook
returned = gb.grades
returned.append(0)
print(f"returned list:  {returned}")
print(f"gb.grades:      {gb.grades}")  # Still unaffected!
print(f"gb.average:     {gb.average:.1f}")


# =====================================================================
print("\n--- 7. Encapsulation with __slots__ ---")
# =====================================================================
# __slots__ restricts which attributes can exist on an instance.
# This prevents accidental attribute creation and saves memory.

class StrictPoint:
    __slots__ = ("_x", "_y")

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f"StrictPoint({self._x}, {self._y})"

sp = StrictPoint(3, 4)
print(f"sp -> {sp}")

# Cannot add arbitrary attributes
try:
    sp.z = 5
except AttributeError as e:
    print(f"  __slots__ prevents sp.z = 5: {e}")


# =====================================================================
print("\n--- 8. The @property Pattern for Write-Once Attributes ---")
# =====================================================================
# Some attributes should be set once during __init__ and never changed.

class Transaction:
    """Immutable transaction record."""
    def __init__(self, txn_id, amount, currency="USD"):
        self._txn_id = txn_id
        self._amount = amount
        self._currency = currency

    @property
    def txn_id(self):
        return self._txn_id

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    def __repr__(self):
        return f"Transaction({self._txn_id}, {self._amount} {self._currency})"

txn = Transaction("TXN-001", 250.00, "EUR")
print(f"txn -> {txn}")
print(f"txn.txn_id -> {txn.txn_id}")

try:
    txn.amount = 9999
except AttributeError as e:
    print(f"  Cannot modify: {e}")


# =====================================================================
print("\n--- 9. Information Hiding vs Encapsulation ---")
# =====================================================================
# Information hiding: concealing implementation details.
# Encapsulation: bundling data + methods together.
# They are related but distinct concepts.

class TemperatureSensor:
    """External code only sees celsius/fahrenheit — not internal storage."""

    def __init__(self, celsius):
        self._raw_reading = celsius  # Internal detail: stored in Celsius

    @property
    def celsius(self):
        """Public interface — hides internal storage name."""
        return self._raw_reading

    @celsius.setter
    def celsius(self, value):
        self._raw_reading = value

    @property
    def fahrenheit(self):
        """Computed from internal storage — user doesn't know how."""
        return self._raw_reading * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Internally converts back to Celsius."""
        self._raw_reading = (value - 32) * 5 / 9

sensor = TemperatureSensor(100)
print(f"sensor.celsius    -> {sensor.celsius}")
print(f"sensor.fahrenheit -> {sensor.fahrenheit}")

sensor.fahrenheit = 32
print(f"After setting 32°F: celsius -> {sensor.celsius}")


# =====================================================================
print("\n--- 10. Real-World Example: Secure Password Manager ---")
# =====================================================================

import hashlib

class UserAccount:
    """Encapsulated user account — password is never stored or returned."""

    def __init__(self, username, password):
        self._username = username
        self.__password_hash = self._hash(password)
        self._login_attempts = 0
        self._locked = False

    @staticmethod
    def _hash(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def username(self):
        return self._username

    @property
    def is_locked(self):
        return self._locked

    def verify_password(self, password):
        """Verify without ever exposing the stored hash."""
        if self._locked:
            return False
        if self._hash(password) == self.__password_hash:
            self._login_attempts = 0
            return True
        self._login_attempts += 1
        if self._login_attempts >= 3:
            self._locked = True
        return False

    def change_password(self, old_password, new_password):
        if not self.verify_password(old_password):
            return False
        self.__password_hash = self._hash(new_password)
        return True

    def __repr__(self):
        status = "LOCKED" if self._locked else "active"
        return f"UserAccount({self._username!r}, {status})"

user = UserAccount("admin", "secure123")
print(f"user -> {user}")
print(f"Verify correct: {user.verify_password('secure123')}")
print(f"Verify wrong:   {user.verify_password('wrong')}")
print(f"Verify wrong:   {user.verify_password('wrong')}")
print(f"Verify wrong:   {user.verify_password('wrong')}")
print(f"Account locked: {user.is_locked}")
print(f"Verify after lock: {user.verify_password('secure123')}")

# The password hash is deeply hidden via name mangling
print(f"Direct __password_hash access? ", end="")
try:
    print(user.__password_hash)
except AttributeError:
    print("Denied (name mangled)")


print("\n" + "=" * 70)
print("  End of Python Encapsulation Explanation")
print("=" * 70)
