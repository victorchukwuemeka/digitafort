"""
# Python Class Properties: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Class Properties in Python. It covers the @property decorator, getters,
setters, deleters, computed properties, validation, and real-world patterns.

Properties let you define methods that are accessed like attributes,
providing a clean interface while maintaining control over data access.
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON CLASS PROPERTIES — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. The Problem: Direct Attribute Access ---")
# =====================================================================
# Without properties, you expose raw attributes. If you later need
# validation, computation, or side-effects, you'd have to change
# the interface (breaking existing code).

class RawCircle:
    def __init__(self, radius):
        self.radius = radius  # No validation — any value is accepted

c = RawCircle(-5)
print(f"RawCircle with radius=-5: {c.radius}")
print("⚠ Negative radius accepted — no validation!")


# =====================================================================
print("\n--- 2. The Java/C++ Approach: Explicit Getters and Setters ---")
# =====================================================================
# In other languages, you'd write get_radius() / set_radius() methods.
# This works but is verbose and un-Pythonic.

class VerboseCircle:
    def __init__(self, radius):
        self._radius = None
        self.set_radius(radius)

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

vc = VerboseCircle(10)
print(f"vc.get_radius() -> {vc.get_radius()}")
vc.set_radius(20)
print(f"After set_radius(20): {vc.get_radius()}")
print("This works but requires explicit method calls — not Pythonic.")


# =====================================================================
print("\n--- 3. The Pythonic Way: @property Decorator ---")
# =====================================================================
# @property lets you define a method that behaves like an attribute.
# You access it as obj.radius (not obj.radius()).

class Circle:
    """Circle with validated radius via @property."""

    def __init__(self, radius):
        # This triggers the setter (which validates the value)
        self.radius = radius

    @property
    def radius(self):
        """Getter: returns the stored radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter: validates before storing."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected number, got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"Radius cannot be negative, got {value}")
        self._radius = value

    @property
    def area(self):
        """Read-only computed property."""
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        """Read-only computed property."""
        import math
        return 2 * math.pi * self._radius

    def __repr__(self):
        return f"Circle(radius={self._radius})"

c = Circle(5)
print(f"c.radius        -> {c.radius}")
print(f"c.area           -> {c.area:.4f}")
print(f"c.circumference  -> {c.circumference:.4f}")

c.radius = 10  # Triggers setter with validation
print(f"After c.radius = 10: area -> {c.area:.4f}")

# Validation in action
for bad in [-3, "abc"]:
    try:
        c.radius = bad
    except (ValueError, TypeError) as e:
        print(f"  Correctly rejected {bad!r}: {e}")


# =====================================================================
print("\n--- 4. Read-Only Properties ---")
# =====================================================================
# Omitting the setter makes a property read-only.

class Immutable:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def magnitude(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

point = Immutable(3, 4)
print(f"point.x         -> {point.x}")
print(f"point.y         -> {point.y}")
print(f"point.magnitude -> {point.magnitude}")

try:
    point.x = 99
except AttributeError as e:
    print(f"  Cannot set read-only property: {e}")


# =====================================================================
print("\n--- 5. The @property.deleter ---")
# =====================================================================
# You can define a deleter to handle 'del obj.attribute'.

class CacheableData:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._processed = None

    @property
    def processed(self):
        if self._processed is None:
            print("  [Processing data...]")
            self._processed = sorted(set(self._raw_data))
        return self._processed

    @processed.deleter
    def processed(self):
        print("  [Cache cleared]")
        self._processed = None

data = CacheableData([3, 1, 4, 1, 5, 9, 2, 6, 5])
print(f"First access:  {data.processed}")
print(f"Cached access: {data.processed}")  # No "Processing" message

del data.processed                         # Clear cache
print(f"After delete:  {data.processed}")  # Re-processes


# =====================================================================
print("\n--- 6. property() as a Built-in Function ---")
# =====================================================================
# @property is syntactic sugar for the property() built-in.
# property(fget, fset, fdel, doc) — all arguments are optional.

class OldStyleProperty:
    def __init__(self, value):
        self._value = value

    def _get_value(self):
        return self._value

    def _set_value(self, val):
        self._value = val

    def _del_value(self):
        print("  Deleting value!")
        del self._value

    # Explicitly create the property descriptor
    value = property(_get_value, _set_value, _del_value, "The value property.")

osp = OldStyleProperty(100)
print(f"osp.value -> {osp.value}")
osp.value = 200
print(f"After assignment: osp.value -> {osp.value}")
print(f"Docstring: {OldStyleProperty.value.__doc__}")


# =====================================================================
print("\n--- 7. Computed Properties with Caching ---")
# =====================================================================
# Properties that derive values from other attributes are called
# computed properties. Cache them when computation is expensive.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        """Computed on every access (no cache needed for simple math)."""
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    @property
    def is_square(self):
        return self._width == self._height

    def __repr__(self):
        return f"Rectangle({self._width}x{self._height})"

r = Rectangle(10, 5)
print(f"r -> {r}")
print(f"r.area      -> {r.area}")
print(f"r.perimeter -> {r.perimeter}")
print(f"r.is_square -> {r.is_square}")

r.width = 5
print(f"After r.width=5: is_square -> {r.is_square}")


# =====================================================================
print("\n--- 8. Properties in Inheritance ---")
# =====================================================================
# Properties are inherited and can be overridden in subclasses.

class Shape:
    @property
    def kind(self):
        return "generic shape"

class Square(Shape):
    def __init__(self, side):
        self._side = side

    @property
    def kind(self):
        return "square"

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Side must be positive")
        self._side = value

s = Square(7)
print(f"s.kind -> {s.kind}")
print(f"s.side -> {s.side}")
s.side = 12
print(f"After s.side=12: {s.side}")


# =====================================================================
print("\n--- 9. Properties vs __slots__ ---")
# =====================================================================
# __slots__ restricts which attributes an instance can have.
# Properties work with __slots__ but you must include the backing
# attribute name in __slots__.

class Efficient:
    __slots__ = ("_name",)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.strip().title()

e = Efficient()
e.name = "  alice smith  "
print(f"e.name -> {e.name}")

# Cannot add arbitrary attributes with __slots__
try:
    e.age = 30
except AttributeError as e_err:
    print(f"  __slots__ restriction: {e_err}")


# =====================================================================
print("\n--- 10. Real-World Example: User Profile ---")
# =====================================================================

class UserProfile:
    """User profile with validated, computed, and formatted properties."""

    def __init__(self, first_name, last_name, email, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self._birth_year = birth_year

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        self._first_name = value.strip().title()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        self._last_name = value.strip().title()

    @property
    def full_name(self):
        """Computed: combines first and last name."""
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError(f"Invalid email: {value}")
        self._email = value.lower().strip()

    @property
    def age(self):
        """Computed from birth year."""
        from datetime import date
        return date.today().year - self._birth_year

    def __repr__(self):
        return f"UserProfile({self.full_name!r}, {self.email!r}, age={self.age})"

user = UserProfile("  jane  ", "  DOE  ", "Jane.Doe@EXAMPLE.com", 1995)
print(f"user.full_name  -> {user.full_name}")
print(f"user.email      -> {user.email}")
print(f"user.age        -> {user.age}")
print(f"repr(user)      -> {repr(user)}")


print("\n" + "=" * 70)
print("  End of Python Class Properties Explanation")
print("=" * 70)
