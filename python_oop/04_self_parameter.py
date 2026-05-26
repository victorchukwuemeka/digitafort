"""
# Python self Parameter: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
the 'self' parameter in Python. It covers what self is, why it's explicit,
how it works under the hood, and common misconceptions.

'self' is the conventional name for the first parameter of instance methods.
It refers to the specific instance that is calling the method, giving
the method access to that object's attributes and other methods.
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON self PARAMETER — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. What Is 'self'? ---")
# =====================================================================
# 'self' is a reference to the CURRENT INSTANCE of the class.
# When you call obj.method(), Python automatically passes 'obj' as
# the first argument to method(). That first parameter is 'self'.

class Lamp:
    def __init__(self, color):
        # 'self' here refers to the specific Lamp being created
        self.color = color
        self.is_on = False

    def turn_on(self):
        # 'self' refers to whichever Lamp instance calls this method
        self.is_on = True
        print(f"  The {self.color} lamp is now ON")

    def turn_off(self):
        self.is_on = False
        print(f"  The {self.color} lamp is now OFF")

red_lamp = Lamp("red")
blue_lamp = Lamp("blue")

# When we call red_lamp.turn_on(), Python translates it to:
#   Lamp.turn_on(red_lamp)
red_lamp.turn_on()
blue_lamp.turn_on()

print(f"red_lamp.is_on  -> {red_lamp.is_on}")
print(f"blue_lamp.is_on -> {blue_lamp.is_on}")


# =====================================================================
print("\n--- 2. How Python Passes 'self' Automatically ---")
# =====================================================================
# obj.method() is syntactic sugar for Class.method(obj).
# This is called "bound method" vs "unbound function" distinction.

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, n):
        self.value += n
        return self

calc = Calculator(10)

# These two calls are IDENTICAL:
calc.add(5)                  # Bound method call — self is auto-injected
print(f"After calc.add(5):          calc.value -> {calc.value}")

Calculator.add(calc, 5)      # Unbound call — self is passed explicitly
print(f"After Calculator.add(calc, 5): calc.value -> {calc.value}")


# =====================================================================
print("\n--- 3. self Refers to the Specific Instance ---")
# =====================================================================
# Each instance maintains its own attribute namespace. 'self' ensures
# that methods operate on the correct instance's data.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

s1 = Student("Alice")
s2 = Student("Bob")

s1.add_grade(95)
s1.add_grade(88)
s2.add_grade(72)
s2.add_grade(81)
s2.add_grade(90)

# Each student's grades are completely independent
print(f"s1.name='{s1.name}', grades={s1.grades}, avg={s1.average():.1f}")
print(f"s2.name='{s2.name}', grades={s2.grades}, avg={s2.average():.1f}")


# =====================================================================
print("\n--- 4. self Inside __init__ ---")
# =====================================================================
# In __init__, self is the freshly created (but empty) instance.
# You use self to attach initial attributes to this new object.

class Coordinate:
    def __init__(self, x, y):
        # At this point, 'self' is a brand-new empty Coordinate instance.
        # We are attaching attributes to it.
        self.x = x
        self.y = y
        # self can also call other methods during initialization
        self.magnitude = self._compute_magnitude()

    def _compute_magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"Coordinate({self.x}, {self.y}) [magnitude={self.magnitude:.2f}]"

c = Coordinate(3, 4)
print(f"c -> {c}")
print(f"c.magnitude -> {c.magnitude}")


# =====================================================================
print("\n--- 5. 'self' Is Just a Convention (But Don't Break It) ---")
# =====================================================================
# 'self' is NOT a keyword — it's a universally followed convention.
# You COULD name it anything, but doing so is strongly discouraged.

class Unconventional:
    def __init__(this, value):      # Using 'this' instead of 'self'
        this.value = value

    def show(this):
        return f"Value is {this.value}"

u = Unconventional(42)
print(f"u.show() -> {u.show()}")
print("⚠ Note: Using anything other than 'self' is considered bad practice!")


# =====================================================================
print("\n--- 6. self in Method Chaining ---")
# =====================================================================
# Returning 'self' from methods enables fluent API / method chaining.

class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self._columns = "*"
        self._where = ""
        self._order = ""

    def select(self, columns):
        self._columns = columns
        return self  # <-- returns the instance for chaining

    def where(self, condition):
        self._where = f" WHERE {condition}"
        return self

    def order_by(self, column, direction="ASC"):
        self._order = f" ORDER BY {column} {direction}"
        return self

    def build(self):
        return f"SELECT {self._columns} FROM {self.table}{self._where}{self._order};"

# Chained calls — each method returns self
query = (QueryBuilder("users")
         .select("name, email")
         .where("age > 18")
         .order_by("name")
         .build())
print(f"Generated SQL: {query}")


# =====================================================================
print("\n--- 7. self vs cls ---")
# =====================================================================
# 'self'  -> instance methods -> operates on a specific object
# 'cls'   -> class methods    -> operates on the class itself
# Neither -> static methods   -> utility function, no binding

class Registry:
    _entries = []

    def __init__(self, name):
        self.name = name
        Registry._entries.append(self)

    def instance_info(self):
        """Instance method: 'self' is the object."""
        return f"Instance: {self.name} (id={id(self)})"

    @classmethod
    def class_info(cls):
        """Class method: 'cls' is the class."""
        return f"Class: {cls.__name__}, total entries: {len(cls._entries)}"

    @staticmethod
    def static_info():
        """Static method: no self or cls."""
        return "I'm a utility — I don't know about instances or class."

r1 = Registry("Alpha")
r2 = Registry("Beta")

print(f"r1.instance_info() -> {r1.instance_info()}")
print(f"Registry.class_info() -> {Registry.class_info()}")
print(f"Registry.static_info() -> {Registry.static_info()}")


# =====================================================================
print("\n--- 8. self and the __dict__ Attribute ---")
# =====================================================================
# Every instance has a __dict__ that stores its instance attributes.
# When you write self.x = 10, it's equivalent to self.__dict__['x'] = 10.

class Inspectable:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

obj = Inspectable(1, "two", [3])
print(f"obj.__dict__ -> {obj.__dict__}")

# Direct dict manipulation (equivalent to self.d = 4)
obj.__dict__["d"] = 4
print(f"obj.d -> {obj.d}")
print(f"Updated __dict__ -> {obj.__dict__}")


# =====================================================================
print("\n--- 9. Common Mistake: Forgetting self ---")
# =====================================================================
# If you forget 'self' in a method signature, Python will complain
# that the method received an unexpected argument (the auto-injected self).

class Broken:
    def __init__(self, value):
        self.value = value

    def show(self):
        return f"Value: {self.value}"

    # This method is missing 'self' — it would fail on instance call
    # def bad_method():       # ← Missing 'self'
    #     return "This will crash"

b = Broken(99)
print(f"b.show() -> {b.show()}")
print("⚠ Always include 'self' as the first parameter of instance methods!")


# =====================================================================
print("\n--- 10. self in Inheritance ---")
# =====================================================================
# In inheritance, 'self' always refers to the actual instance type,
# not the class where the method is defined. This is how polymorphism works.

class Base:
    def identify(self):
        return f"self is: {type(self).__name__} (defined in Base)"

class Child(Base):
    pass  # Inherits identify() without overriding

class GrandChild(Child):
    pass

base_obj = Base()
child_obj = Child()
gc_obj = GrandChild()

print(f"base_obj.identify()  -> {base_obj.identify()}")
print(f"child_obj.identify() -> {child_obj.identify()}")
print(f"gc_obj.identify()    -> {gc_obj.identify()}")


# =====================================================================
print("\n--- 11. Real-World Example: Shopping Cart ---")
# =====================================================================

class ShoppingCart:
    """Demonstrates self usage throughout a realistic class."""

    def __init__(self, customer_name):
        self.customer = customer_name
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        return self

    def remove_item(self, name):
        self.items = [i for i in self.items if i["name"] != name]
        return self

    def total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def summary(self):
        lines = [f"🛒 Cart for {self.customer}:"]
        for item in self.items:
            subtotal = item["price"] * item["quantity"]
            lines.append(f"   {item['name']} x{item['quantity']} "
                         f"@ ${item['price']:.2f} = ${subtotal:.2f}")
        lines.append(f"   Total: ${self.total():.2f}")
        return "\n".join(lines)

cart = ShoppingCart("Alice")
cart.add_item("Laptop", 999.99).add_item("Mouse", 29.99, 2).add_item("USB Cable", 9.99, 3)
print(cart.summary())

cart.remove_item("USB Cable")
print(f"\nAfter removing USB Cable: Total = ${cart.total():.2f}")


print("\n" + "=" * 70)
print("  End of Python self Parameter Explanation")
print("=" * 70)
