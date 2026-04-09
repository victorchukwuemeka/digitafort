# Python Object-Oriented Programming — Complete Deep Course

> A comprehensive, no-fluff reference. Every section goes deep. Read it once, keep it forever.

---

## Table of Contents

1. [What a Class Really Is — Memory, Namespaces, Lookup](#1-what-a-class-really-is)
2. [__init__, Instance State, and the Shared Mutable Trap](#2-init-instance-state-and-the-shared-mutable-trap)
3. [Inheritance, super(), and MRO](#3-inheritance-super-and-mro)
4. [Encapsulation and Properties](#4-encapsulation-and-properties)
5. [Dunder Methods — Making Objects Feel Native](#5-dunder-methods)
6. [Composition and Delegation](#6-composition-and-delegation)
7. [Class Methods, Static Methods, and Factories](#7-classmethods-staticmethods-and-factories)
8. [Dataclasses and __slots__](#8-dataclasses-and-slots)
9. [Abstract Base Classes and Protocols](#9-abstract-base-classes-and-protocols)
10. [Descriptors — The Engine Behind Properties](#10-descriptors)
11. [Metaclasses](#11-metaclasses)
12. [Memory Management, __slots__, and Performance](#12-memory-management)
13. [Mixins and Multiple Inheritance Patterns](#13-mixins-and-multiple-inheritance-patterns)
14. [Design Principles Applied to Classes](#14-design-principles)
15. [Practical Project — Inventory and Checkout Engine](#15-practical-project)

---

## 1. What a Class Really Is

### Classes Are Objects Too

In Python, everything is an object — including the class itself. When you write `class Foo: ...`, Python creates a `type` object and binds it to the name `Foo`. The class is not a template that gets erased at runtime; it lives in memory, holds a namespace (`__dict__`), and can be passed around like any other value.

```python
class Dog:
    species = "Canis familiaris"

print(type(Dog))       # <class 'type'>
print(Dog.__dict__)    # mappingproxy({'species': 'Canis familiaris', '__dict__': ..., ...})
print(id(Dog))         # some integer — it lives in memory
```

### The Attribute Lookup Chain

When you access `obj.attr`, Python does not do a simple dictionary lookup. It walks a precise chain:

1. **Data descriptors** on the class or its bases (e.g., `property` with both `__get__` and `__set__`)
2. **The instance's own `__dict__`**
3. **Non-data descriptors and other class attributes** (e.g., regular functions, `property` getters only)

This order is not trivia — it is why `property` setters can intercept assignment even though instance dicts are checked second for gets.

```python
class User:
    role = "member"          # class attribute

u = User()
print(u.__dict__)            # {} — instance dict is empty
print(u.role)                # "member" — found on the class

u.role = "admin"             # writes to INSTANCE dict
print(u.__dict__)            # {'role': 'admin'}
print(u.role)                # "admin" — instance shadows class
print(User.role)             # "member" — class unchanged
```

### Identity vs. Equality

- `is` compares **object identity** — same memory address (`id(a) == id(b)`)
- `==` compares **value** — delegates to `__eq__`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  — same value
print(a is b)   # False — different objects
print(a is c)   # True  — same object

# With custom classes:
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # False — no __eq__ defined, falls back to identity
```

Always define `__eq__` if two instances with identical data should compare equal. And if you define `__eq__`, read section 5 about `__hash__` — Python will set it to `None` automatically, breaking dict/set usage.

### `__dict__` is a Real Dictionary

You can read and write it directly (useful for debugging, serialization, and metaprogramming):

```python
class Config:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)   # bulk-assign kwargs as attributes

c = Config(debug=True, port=8080)
print(c.debug)   # True
print(c.port)    # 8080
```

### The `type()` Function and Dynamic Class Creation

`type` is not just for checking types — it's the default metaclass and can create classes dynamically:

```python
# type(name, bases, namespace)
Animal = type("Animal", (), {"sound": "...", "speak": lambda self: self.sound})
Dog = type("Dog", (Animal,), {"sound": "Woof"})

d = Dog()
print(d.speak())   # Woof
```

This is exactly what the `class` statement does under the hood.

---

## 2. __init__, Instance State, and the Shared Mutable Trap

### What __init__ Actually Does

`__init__` is not a constructor — `__new__` is. By the time `__init__` runs, the object already exists. `__init__` is an **initializer**: it sets up the state of an already-created object.

```python
class Foo:
    def __new__(cls, *args, **kwargs):
        print(f"__new__ called — creating instance of {cls}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print(f"__init__ called — initializing with {value}")
        self.value = value

f = Foo(42)
# __new__ called — creating instance of <class '__main__.Foo'>
# __init__ called — initializing with 42
```

You rarely override `__new__` unless you're implementing singletons, immutable types, or metaclasses.

### Class Variables vs. Instance Variables

This is the single most common source of bugs in Python OOP.

```python
class Counter:
    count = 0        # CLASS variable — shared across all instances

    def __init__(self, name):
        self.name = name   # instance variable — unique per instance

    def increment(self):
        Counter.count += 1   # explicitly modifying the class variable
```

The danger: if you mutate a mutable class attribute (list, dict, set), ALL instances see the change.

```python
class Team:
    members = []         # SHARED — this is a bug waiting to happen

t1 = Team()
t2 = Team()
t1.members.append("Alice")

print(t2.members)   # ['Alice'] — t2 sees Alice! Data leakage.
```

**The fix:** always initialize mutable state in `__init__`:

```python
class Team:
    def __init__(self):
        self.members = []    # each instance gets its own list
```

**When class variables ARE appropriate:**

- Constants that are truly shared: `TAX_RATE = 0.2`
- Counters that track class-level state: `instance_count = 0`
- Default values for immutable types (int, str, tuple, frozenset) — safe because you can't mutate them in-place

```python
class Product:
    DEFAULT_CURRENCY = "USD"   # fine — immutable, truly shared
    _instance_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product._instance_count += 1

    @classmethod
    def instance_count(cls):
        return cls._instance_count
```

### Default Argument Trap (Related Gotcha)

The same mutation bug appears in function/method default arguments:

```python
def add_item(item, collection=[]):   # BAD — [] created once at definition
    collection.append(item)
    return collection

print(add_item("a"))   # ['a']
print(add_item("b"))   # ['a', 'b'] — not ['b']!

# Fix:
def add_item(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection
```

### Validating __init__ Arguments

Don't silently accept bad data. Validate early:

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("owner must be a non-empty string")
        if balance < 0:
            raise ValueError(f"Initial balance cannot be negative, got {balance}")
        self.owner = owner.strip()
        self._balance = float(balance)

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"
```

### Post-init Patterns

For complex initialization, split setup into private helpers:

```python
class DatabaseConnection:
    def __init__(self, host, port, dbname, user, password):
        self._config = self._validate_config(host, port, dbname)
        self._credentials = self._load_credentials(user, password)
        self._conn = None

    def _validate_config(self, host, port, dbname):
        if not (1 <= port <= 65535):
            raise ValueError(f"Invalid port: {port}")
        return {"host": host, "port": port, "dbname": dbname}

    def _load_credentials(self, user, password):
        if not user or not password:
            raise ValueError("Credentials cannot be empty")
        return {"user": user, "password": password}
```

---

## 3. Inheritance, super(), and MRO

### When to Use Inheritance (and When Not To)

Inheritance is appropriate only for a genuine **is-a** relationship. If you have to say "well, it's KIND OF like a..." — that's a signal to use composition instead.

Good: `AdminUser` is a `User`. `Dog` is an `Animal`.  
Bad: `Stack` inherits from `list` just to reuse `append`. Use composition.

```python
# Bad — Stack IS NOT a list. Users shouldn't call stack.sort() or stack.insert()
class Stack(list):
    def push(self, item):
        self.append(item)
    def pop_top(self):
        return self.pop()

# Good — Stack HAS a list
class Stack:
    def __init__(self):
        self._data = []
    def push(self, item):
        self._data.append(item)
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()
    def peek(self):
        if not self._data:
            raise IndexError("peek at empty stack")
        return self._data[-1]
    def __len__(self):
        return len(self._data)
    def __repr__(self):
        return f"Stack({self._data!r})"
```

### Method Resolution Order (MRO)

Python uses the C3 linearization algorithm to determine the MRO — the order in which classes are searched for attributes and methods.

```python
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    pass

print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
print(D().hello())   # "B" — B is found first in the MRO
```

The MRO guarantees:
1. A class always appears before its parents
2. The order of base classes is preserved
3. If a class appears in multiple places, only the last occurrence is kept (from the right)

### super() — It's Not "Call the Parent"

`super()` does not call the parent class. It returns a **proxy object** that delegates method calls to the **next class in the MRO**. This distinction matters enormously in multiple inheritance.

```python
class Base:
    def __init__(self):
        print("Base.__init__")

class Left(Base):
    def __init__(self):
        print("Left.__init__")
        super().__init__()    # calls next in MRO, not necessarily Base

class Right(Base):
    def __init__(self):
        print("Right.__init__")
        super().__init__()

class Child(Left, Right):
    def __init__(self):
        print("Child.__init__")
        super().__init__()

Child()
# Child.__init__
# Left.__init__
# Right.__init__
# Base.__init__
# Base is called ONCE — cooperative multiple inheritance works correctly
```

Without `super()`, if `Left.__init__` called `Base.__init__()` directly, `Right.__init__` would never run.

### Rule: Always Use super() in __init__

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)   # initialize parent state first
        self.battery_kwh = battery_kwh

class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, autonomy_level):
        super().__init__(make, model, year)
        self.autonomy_level = autonomy_level

class AutonomousEV(ElectricVehicle, AutonomousVehicle):
    def __init__(self, make, model, year, battery_kwh, autonomy_level):
        # super() will handle the full MRO chain
        super().__init__(make, model, year, battery_kwh)
        self.autonomy_level = autonomy_level
```

### Overriding Methods — Extending, Not Replacing

A common pattern is to extend a parent method rather than replace it entirely:

```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().log(f"{timestamp} — {message}")   # reuse parent logic

class PrefixLogger(TimestampLogger):
    def __init__(self, prefix):
        self.prefix = prefix

    def log(self, message):
        super().log(f"[{self.prefix}] {message}")

logger = PrefixLogger("AUTH")
logger.log("User logged in")
# [LOG] 2024-01-15 10:30:45 — [AUTH] User logged in
```

---

## 4. Encapsulation and Properties

### Python's Convention-Based Encapsulation

Python has no true private members. The convention is:

- `name` — public, part of the API
- `_name` — internal, use with caution, may change
- `__name` — name-mangled to `_ClassName__name`, strong "keep out" signal

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance    # mangled to _Account__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

a = Account(100)
# a.__balance       # AttributeError
# a._Account__balance  # works — Python doesn't truly hide it
```

Name mangling exists to prevent accidental overrides in subclasses, not to provide security.

### Properties — The Right Tool for Validation

A `property` lets you expose an attribute-like interface while running code on access and assignment.

```python
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius   # uses the setter below

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError(f"Temperature below absolute zero: {value}")
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) * 5/9   # delegates to celsius setter

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    def __repr__(self):
        return f"Temperature({self._celsius}°C / {self.fahrenheit:.1f}°F / {self.kelvin:.2f}K)"

t = Temperature(100)
print(t)            # Temperature(100°C / 212.0°F / 373.15K)
t.fahrenheit = 32
print(t.celsius)    # 0.0
```

### When to Use Properties vs. Regular Attributes

Use a `property` when:
- You need to validate on assignment
- The value is computed from other state
- You need to trigger side effects on access/assignment (e.g., cache invalidation)
- You want to keep a read-only attribute (getter only, no setter)

Do NOT use properties for expensive computations — call them methods instead so callers know there's real work happening.

```python
class Circle:
    def __init__(self, radius: float):
        self.radius = radius    # setter validates

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError(f"Radius must be positive, got {value}")
        self._radius = float(value)

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self) -> float:
        import math
        return 2 * math.pi * self._radius

    def __repr__(self):
        return f"Circle(radius={self._radius})"
```

### Cached Properties

For expensive computed properties, use `functools.cached_property` — computed once, then stored:

```python
from functools import cached_property
import math

class Triangle:
    def __init__(self, a, b, c):
        sides = sorted([a, b, c])
        if sides[2] >= sides[0] + sides[1]:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = a, b, c

    @cached_property
    def area(self) -> float:
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @cached_property
    def perimeter(self) -> float:
        return self.a + self.b + self.c

t = Triangle(3, 4, 5)
print(t.area)       # computed
print(t.area)       # returned from cache — no recomputation
print(t.__dict__)   # {'a': 3, 'b': 4, 'c': 5, 'area': 6.0, 'perimeter': 12.0}
```

Note: `cached_property` stores the result in the instance dict. This means it only works if there's no data descriptor (like a `property` setter) blocking it.

---

## 5. Dunder Methods

Dunder (double-underscore) methods let your objects integrate naturally with Python's syntax and built-ins. They are not "magic" — they are explicit hooks into the language's protocols.

### String Representation

```python
class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        # Unambiguous. Should ideally be valid Python to recreate the object.
        return f"Vector({self.x!r}, {self.y!r}, {self.z!r})"

    def __str__(self):
        # Human-readable. Falls back to __repr__ if not defined.
        return f"({self.x}, {self.y}, {self.z})"

    def __format__(self, spec):
        if spec == "unit":
            mag = abs(self)
            return f"({self.x/mag:.3f}, {self.y/mag:.3f}, {self.z/mag:.3f})"
        return str(self)

v = Vector(1, 2, 3)
print(repr(v))         # Vector(1, 2, 3)
print(str(v))          # (1, 2, 3)
print(f"{v:unit}")     # (0.267, 0.535, 0.802)
```

### Arithmetic Operators

```python
class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented   # return NotImplemented, don't raise
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        # scalar * vector — handled by __rmul__
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        # Called when scalar.__mul__(vector) returns NotImplemented
        return self.__mul__(scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __abs__(self):
        import math
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __bool__(self):
        return abs(self) != 0

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)     # Vector(5, 7, 9)
print(3 * v1)      # Vector(3, 6, 9)
print(abs(v1))     # 3.7416...
```

### Comparison and Equality

```python
from functools import total_ordering

@total_ordering   # fills in all comparison methods from __eq__ and __lt__
class Version:
    def __init__(self, major, minor, patch):
        self.major, self.minor, self.patch = major, minor, patch

    def _tuple(self):
        return (self.major, self.minor, self.patch)

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._tuple() == other._tuple()

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._tuple() < other._tuple()

    def __hash__(self):
        return hash(self._tuple())   # safe because Version is effectively immutable

    def __repr__(self):
        return f"Version({self.major}.{self.minor}.{self.patch})"

v1 = Version(1, 2, 3)
v2 = Version(1, 10, 0)
print(v1 < v2)    # True
print(v2 > v1)    # True — provided by @total_ordering
print(sorted([v2, v1]))   # [Version(1.2.3), Version(1.10.0)]
versions = {v1, v2}       # works because __hash__ is defined
```

### __eq__ and __hash__ Contract

If you define `__eq__`, Python sets `__hash__` to `None` by default, making instances unhashable. Rules:

- If objects are mutable and compare by value → define `__eq__`, leave `__hash__ = None` (unhashable, like lists)
- If objects are immutable and compare by value → define both `__eq__` and `__hash__`
- If objects should use identity for both → define neither (inherit from `object`)

### Container Protocol

```python
class Bag:
    def __init__(self):
        self._items = {}

    def add(self, item, count=1):
        self._items[item] = self._items.get(item, 0) + count

    def remove(self, item, count=1):
        if item not in self._items:
            raise KeyError(f"{item!r} not in bag")
        self._items[item] -= count
        if self._items[item] <= 0:
            del self._items[item]

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return sum(self._items.values())

    def __iter__(self):
        for item, count in self._items.items():
            for _ in range(count):
                yield item

    def __getitem__(self, item):
        return self._items.get(item, 0)

    def __repr__(self):
        return f"Bag({self._items!r})"

b = Bag()
b.add("apple", 3)
b.add("banana", 2)
print("apple" in b)     # True
print(len(b))           # 5
print(list(b))          # ['apple', 'apple', 'apple', 'banana', 'banana']
print(b["apple"])       # 3
```

### Context Manager Protocol

```python
class Timer:
    import time

    def __enter__(self):
        import time
        self._start = time.perf_counter()
        return self   # returned as the 'as' target

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self._start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False   # don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))

print(t.elapsed)   # access elapsed time after the block
```

### Callable Objects

```python
class RateLimiter:
    def __init__(self, max_calls: int, period: float):
        self.max_calls = max_calls
        self.period = period
        self._calls = []

    def __call__(self, func):
        import time
        from functools import wraps

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            self._calls = [c for c in self._calls if now - c < self.period]
            if len(self._calls) >= self.max_calls:
                raise RuntimeError("Rate limit exceeded")
            self._calls.append(now)
            return func(*args, **kwargs)
        return wrapper

@RateLimiter(max_calls=3, period=1.0)
def fetch_data(url):
    return f"data from {url}"
```

---

## 6. Composition and Delegation

### Why Composition Beats Inheritance

Inheritance creates tight coupling. Every change to a base class is a potential breaking change in all subclasses. Composition keeps components decoupled, individually testable, and swappable.

The rule: **prefer composition unless inheritance meaningfully reduces duplication AND the is-a relationship is genuinely true.**

```python
# Bad: inheritance for code reuse — not a real is-a
class CSVParser(list):
    def load(self, path):
        import csv
        with open(path) as f:
            self.extend(csv.DictReader(f))

# Good: composition
class CSVParser:
    def __init__(self):
        self._rows = []

    def load(self, path):
        import csv
        with open(path) as f:
            self._rows = list(csv.DictReader(f))

    def __iter__(self):
        return iter(self._rows)

    def __len__(self):
        return len(self._rows)
```

### The Delegation Pattern

Delegate method calls explicitly to composed objects:

```python
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower
        self._running = False

    def start(self):
        self._running = True
        return f"Engine ({self.horsepower}hp) started"

    def stop(self):
        self._running = False
        return "Engine stopped"

    @property
    def running(self):
        return self._running


class Transmission:
    def __init__(self):
        self._gear = 0

    def shift(self, gear: int):
        if not (0 <= gear <= 6):
            raise ValueError(f"Invalid gear: {gear}")
        self._gear = gear
        return f"Shifted to gear {gear}"

    @property
    def gear(self):
        return self._gear


class Car:
    def __init__(self, make: str, model: str, horsepower: int):
        self.make = make
        self.model = model
        self._engine = Engine(horsepower)
        self._transmission = Transmission()

    def start(self):
        return self._engine.start()

    def stop(self):
        self._transmission.shift(0)
        return self._engine.stop()

    def shift(self, gear: int):
        if not self._engine.running:
            raise RuntimeError("Engine must be running to shift")
        return self._transmission.shift(gear)

    @property
    def status(self):
        return {
            "make": self.make,
            "model": self.model,
            "running": self._engine.running,
            "gear": self._transmission.gear
        }

car = Car("Toyota", "Supra", 340)
print(car.start())    # Engine (340hp) started
print(car.shift(3))   # Shifted to gear 3
print(car.status)
```

### Strategy Pattern via Composition

Swap behaviors at runtime without changing the object's class:

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

class BubbleSort(SortStrategy):
    def sort(self, data: list) -> list:
        data = data[:]
        n = len(data)
        for i in range(n):
            for j in range(n - i - 1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSort(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        mid  = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy.sort(data)

sorter = Sorter(QuickSort())
print(sorter.sort([3, 1, 4, 1, 5, 9, 2, 6]))

sorter.set_strategy(BubbleSort())
print(sorter.sort([3, 1, 4, 1, 5, 9, 2, 6]))
```

---

## 7. Classmethods, Staticmethods, and Factories

### @classmethod — Alternate Constructors

A classmethod receives the class (`cls`) as the first argument instead of an instance. The primary use is **factory methods** — alternative ways to construct an object.

```python
from datetime import date
import json

class Person:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
        return cls(data["name"], data["birth_year"])

    @classmethod
    def from_json(cls, json_str: str) -> "Person":
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_csv_row(cls, row: str) -> "Person":
        name, year = row.strip().split(",")
        return cls(name.strip(), int(year.strip()))

    @property
    def age(self) -> int:
        return date.today().year - self.birth_year

    def __repr__(self):
        return f"Person(name={self.name!r}, birth_year={self.birth_year})"

p1 = Person("Alice", 1990)
p2 = Person.from_dict({"name": "Bob", "birth_year": 1985})
p3 = Person.from_json('{"name": "Carol", "birth_year": 1995}')
p4 = Person.from_csv_row("Dave, 1978")
```

This pattern shines with inheritance — the factory method creates the right subclass automatically because `cls` refers to whatever class it's called on:

```python
class Employee(Person):
    def __init__(self, name, birth_year, employee_id):
        super().__init__(name, birth_year)
        self.employee_id = employee_id

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["birth_year"], data["employee_id"])

e = Employee.from_dict({"name": "Eve", "birth_year": 1992, "employee_id": "E001"})
print(type(e))   # <class '__main__.Employee'> — correct class, not Person
```

### @staticmethod — Pure Utility Functions

A staticmethod belongs to the class namespace but receives neither `self` nor `cls`. Use it for helper functions that relate conceptually to the class but don't need access to instance or class state.

```python
class EmailValidator:
    MAX_LENGTH = 254   # RFC 5321

    def __init__(self, email: str):
        if not self.is_valid(email):
            raise ValueError(f"Invalid email: {email!r}")
        self.email = email.lower()

    @staticmethod
    def is_valid(email: str) -> bool:
        import re
        if not isinstance(email, str):
            return False
        if len(email) > EmailValidator.MAX_LENGTH:
            return False
        pattern = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def domain(email: str) -> str:
        if "@" not in email:
            raise ValueError("Not an email address")
        return email.split("@")[1].lower()

print(EmailValidator.is_valid("user@example.com"))   # True — no instance needed
print(EmailValidator.domain("user@example.com"))     # example.com
```

### Choosing Between classmethod, staticmethod, and method

| Use | When |
|-----|------|
| Regular method | Needs access to `self` (instance state) |
| `@classmethod` | Needs access to `cls` (for factory methods, class state) |
| `@staticmethod` | Pure function logically belonging to the class, no instance/class access |

---

## 8. Dataclasses and __slots__

### @dataclass — Eliminate Boilerplate

`dataclasses` auto-generates `__init__`, `__repr__`, and `__eq__` based on annotated fields. It is not "just a namedtuple" — it's fully customizable.

```python
from dataclasses import dataclass, field, KW_ONLY
from typing import ClassVar

@dataclass
class Product:
    sku: str
    name: str
    price: float
    tags: list[str] = field(default_factory=list)   # mutable default — correct pattern
    _discount: float = field(default=0.0, repr=False, compare=False)

    # class variable — not a dataclass field
    TAX_RATE: ClassVar[float] = 0.08

    def __post_init__(self):
        if self.price < 0:
            raise ValueError(f"Price cannot be negative: {self.price}")
        if not self.sku:
            raise ValueError("SKU cannot be empty")
        self.sku = self.sku.upper()

    @property
    def final_price(self) -> float:
        discounted = self.price * (1 - self._discount)
        return round(discounted * (1 + self.TAX_RATE), 2)

p = Product(sku="abc-123", name="Widget", price=29.99, tags=["electronics"])
print(p)
# Product(sku='ABC-123', name='Widget', price=29.99, tags=['electronics'])
print(p.final_price)   # 32.39
```

### Frozen Dataclasses

`frozen=True` makes the class immutable after creation. Fields become read-only. The class gets `__hash__` automatically (since it's immutable).

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        import math
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(0, 0)
p2 = Point(3, 4)
# p1.x = 5     # FrozenInstanceError

points = {p1, p2}   # hashable — works in sets and dict keys
print(p1.distance_to(p2))   # 5.0
```

### Ordering with Dataclasses

```python
from dataclasses import dataclass

@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

versions = [Version(2, 0, 0), Version(1, 9, 3), Version(1, 10, 0)]
print(sorted(versions))
# [Version(major=1, minor=9, patch=3), Version(major=1, minor=10, patch=0), Version(major=2, minor=0, patch=0)]
```

Ordering compares fields in declaration order — like a tuple comparison.

### __slots__ — Memory Optimization

By default, every instance has a `__dict__` for storing attributes. This has overhead: ~200-400 bytes per instance. `__slots__` replaces `__dict__` with a fixed set of slot descriptors:

```python
class PointWithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointWithSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
p1 = PointWithDict(1, 2)
p2 = PointWithSlots(1, 2)

print(sys.getsizeof(p1.__dict__))   # ~232 bytes (the dict itself)
print(sys.getsizeof(p2))            # ~56 bytes (no dict)
```

Tradeoffs of `__slots__`:
- Cannot add new attributes dynamically
- Cannot have a class variable with the same name as a slot
- Multiple inheritance with `__slots__` gets complicated (all classes in the MRO must define `__slots__`)
- Pickle works but requires `__getstate__`/`__setstate__` in some cases

Use `__slots__` when you're creating millions of instances and memory is a real constraint. With `@dataclass(slots=True)` (Python 3.10+) you get both:

```python
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Coordinate:
    lat: float
    lon: float
    alt: float = 0.0
```

---

## 9. Abstract Base Classes and Protocols

### Abstract Base Classes (ABC)

ABCs define an interface that subclasses must implement. If a subclass doesn't implement all abstract methods, instantiation raises `TypeError`.

```python
from abc import ABC, abstractmethod
from typing import Iterator

class DataSource(ABC):
    """Abstract base for all data sources."""

    @abstractmethod
    def connect(self) -> None:
        """Establish connection to the source."""
        ...

    @abstractmethod
    def fetch(self, query: str) -> list[dict]:
        """Execute query and return rows."""
        ...

    @abstractmethod
    def disconnect(self) -> None:
        """Close the connection."""
        ...

    # Concrete method — shared by all subclasses
    def fetch_all(self, query: str) -> list[dict]:
        self.connect()
        try:
            return self.fetch(query)
        finally:
            self.disconnect()

    # Abstract property
    @property
    @abstractmethod
    def connection_string(self) -> str:
        ...


class PostgresSource(DataSource):
    def __init__(self, host, port, dbname, user, password):
        self._config = dict(host=host, port=port, dbname=dbname,
                            user=user, password=password)
        self._conn = None

    @property
    def connection_string(self) -> str:
        c = self._config
        return f"postgresql://{c['user']}@{c['host']}:{c['port']}/{c['dbname']}"

    def connect(self) -> None:
        print(f"Connecting to {self.connection_string}")
        # self._conn = psycopg2.connect(**self._config)

    def fetch(self, query: str) -> list[dict]:
        print(f"Executing: {query}")
        return []   # would use self._conn.cursor() etc.

    def disconnect(self) -> None:
        print("Disconnecting")


# DataSource()   # TypeError: Can't instantiate abstract class
source = PostgresSource("localhost", 5432, "mydb", "user", "pass")
source.fetch_all("SELECT * FROM users")
```

### Protocols — Structural Typing

Protocols (PEP 544) define interfaces through **structure**, not inheritance. Any class with the right methods satisfies the protocol, even without importing or inheriting from it.

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self, canvas: "Canvas") -> None: ...
    def bounding_box(self) -> tuple[float, float, float, float]: ...

class Circle:
    def __init__(self, cx, cy, r):
        self.cx, self.cy, self.r = cx, cy, r

    def draw(self, canvas):
        print(f"Drawing circle at ({self.cx}, {self.cy}) r={self.r}")

    def bounding_box(self):
        return (self.cx - self.r, self.cy - self.r,
                self.cx + self.r, self.cy + self.r)

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def draw(self, canvas):
        print(f"Drawing rect at ({self.x}, {self.y}) {self.w}x{self.h}")

    def bounding_box(self):
        return (self.x, self.y, self.x + self.w, self.y + self.h)

# Neither inherits from Drawable — but both satisfy it
def render_all(shapes: list[Drawable], canvas) -> None:
    for shape in shapes:
        shape.draw(canvas)

shapes = [Circle(0, 0, 5), Rectangle(1, 1, 10, 5)]
render_all(shapes, None)   # works — structural compatibility

# Runtime check (because of @runtime_checkable):
print(isinstance(Circle(0,0,1), Drawable))   # True
```

### ABC vs Protocol — When to Use Which

| Use | When |
|-----|------|
| `ABC` | You control both the interface AND the implementations. You want concrete shared methods. You want `TypeError` at instantiation if methods missing. |
| `Protocol` | You DON'T control the implementing classes (third-party code). You want duck typing with type-checker support. You want zero coupling. |

---

## 10. Descriptors

Descriptors are the underlying mechanism that powers `property`, `classmethod`, `staticmethod`, and `__slots__`. Understanding them gives you deep control over attribute access.

### The Descriptor Protocol

An object is a descriptor if it defines `__get__`, `__set__`, or `__delete__`.

- **Non-data descriptor**: defines only `__get__` (e.g., functions — this is how methods work)
- **Data descriptor**: defines `__get__` AND `__set__` (or `__delete__`) — these take priority over instance `__dict__`

```python
class Validator:
    """A data descriptor that validates on assignment."""

    def __set_name__(self, owner, name):
        # Called when the class is created — gives us the attribute name
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self   # accessed on the class, not an instance
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    def validate(self, value):
        pass   # override in subclasses


class PositiveNumber(Validator):
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected number, got {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"Expected positive number, got {value}")


class NonEmptyString(Validator):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected str, got {type(value).__name__}")
        if not value.strip():
            raise ValueError("String cannot be empty or whitespace")


class Product:
    name = NonEmptyString()
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name, price, quantity):
        self.name = name       # triggers NonEmptyString.__set__
        self.price = price     # triggers PositiveNumber.__set__
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.name!r}, price={self.price}, qty={self.quantity})"

p = Product("Widget", 9.99, 100)
# p.price = -5    # ValueError: Expected positive number, got -5
# p.name = ""     # ValueError: String cannot be empty
```

### How Functions Become Methods (Non-Data Descriptor)

Every function defined in a class is a non-data descriptor. When accessed on an instance, `__get__` binds the function to the instance, creating a bound method:

```python
class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"

g = Greeter()

# These are equivalent:
g.greet("World")
Greeter.greet.__get__(g, Greeter)("World")

# Proof:
print(type(Greeter.greet))    # <class 'function'>
print(type(g.greet))          # <class 'method'> — __get__ returned a bound method
```

---

## 11. Metaclasses

A metaclass is the class of a class. Just as `Dog()` creates an instance of `Dog`, `Dog` itself is an instance of `type`. Metaclasses let you intercept class creation.

### When You Actually Need Metaclasses

- Enforcing class-level constraints (all subclasses must implement X)
- Auto-registering subclasses in a registry
- Auto-adding attributes/methods to classes at definition time
- ORM systems (Django models use a metaclass)

For most problems, use class decorators instead — they're simpler and achieve the same goals.

```python
class RegistryMeta(type):
    """Metaclass that automatically registers all subclasses."""

    _registry: dict = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        # Register everything except the base class itself
        if bases:
            mcs._registry[name] = cls

        return cls

    @classmethod
    def get_registered(mcs):
        return dict(mcs._registry)


class Plugin(metaclass=RegistryMeta):
    def run(self):
        raise NotImplementedError


class AuthPlugin(Plugin):
    def run(self):
        return "running auth"


class CachePlugin(Plugin):
    def run(self):
        return "running cache"


print(RegistryMeta.get_registered())
# {'AuthPlugin': <class 'AuthPlugin'>, 'CachePlugin': <class 'CachePlugin'>}

# Instantiate by name:
name = "AuthPlugin"
plugin = RegistryMeta._registry[name]()
print(plugin.run())   # running auth
```

### Enforcing Method Implementation with Metaclass

```python
class InterfaceMeta(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        # Skip enforcement on the base class itself
        if not bases:
            return cls

        # Find required methods from base classes
        required = set()
        for base in bases:
            required.update(getattr(base, "_required_methods", set()))

        missing = required - set(namespace)
        if missing:
            raise TypeError(
                f"Class {name!r} must implement: {', '.join(sorted(missing))}"
            )
        return cls


class Interface(metaclass=InterfaceMeta):
    _required_methods = {"save", "load", "delete"}

# class BadRepo(Interface):  # TypeError: must implement: delete, load, save
#     pass

class GoodRepo(Interface):
    def save(self, obj): ...
    def load(self, key): ...
    def delete(self, key): ...
```

### Class Decorators — Usually Better Than Metaclasses

```python
def auto_repr(cls):
    """Decorator that adds __repr__ based on __init__ parameters."""
    import inspect
    sig = inspect.signature(cls.__init__)
    params = [p for p in sig.parameters if p != "self"]

    def __repr__(self):
        attrs = ", ".join(f"{p}={getattr(self, p)!r}" for p in params)
        return f"{cls.__name__}({attrs})"

    cls.__repr__ = __repr__
    return cls

@auto_repr
class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

print(Point(1, 2, 3))   # Point(x=1, y=2, z=3)
```

---

## 12. Memory Management

### Reference Counting and Garbage Collection

Python uses reference counting as its primary memory management mechanism. When an object's reference count drops to zero, it's immediately deallocated.

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))   # 2 — x + the getrefcount argument

y = x
print(sys.getrefcount(x))   # 3 — x, y, + argument

del y
print(sys.getrefcount(x))   # 2 again
```

The cyclic garbage collector handles reference cycles (objects that reference each other, keeping counts above zero forever):

```python
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a cycle
a = Node(1)
b = Node(2)
a.next = b
b.next = a   # cycle

del a, b     # ref counts don't drop to zero
gc.collect() # cycle collector cleans this up
```

### Weak References

Use `weakref` when you need a reference that doesn't prevent garbage collection:

```python
import weakref

class ExpensiveObject:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"ExpensiveObject({self.name!r})"

obj = ExpensiveObject("heavy")
ref = weakref.ref(obj)

print(ref())      # ExpensiveObject('heavy') — obj still alive
del obj
print(ref())      # None — obj was collected
```

Practical use — caches that don't prevent garbage collection:

```python
import weakref

class Cache:
    def __init__(self):
        self._store = weakref.WeakValueDictionary()

    def set(self, key, value):
        self._store[key] = value

    def get(self, key):
        return self._store.get(key)
```

### __slots__ Memory Deep Dive

```python
import tracemalloc

tracemalloc.start()

class WithDict:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

class WithSlots:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

N = 100_000

snapshot1 = tracemalloc.take_snapshot()
dicts = [WithDict(i, i*2, i*3) for i in range(N)]
snapshot2 = tracemalloc.take_snapshot()
del dicts

slots = [WithSlots(i, i*2, i*3) for i in range(N)]
snapshot3 = tracemalloc.take_snapshot()
del slots

# WithDict uses roughly 3-4x more memory than WithSlots
```

---

## 13. Mixins and Multiple Inheritance Patterns

### What a Mixin Is

A mixin is a class designed to be mixed into other classes via multiple inheritance. It provides a specific, limited set of behaviors without being a standalone class. Mixins should:

- Not be instantiated on their own
- Not call `__init__` without `super()`
- Be small and single-purpose
- Not inherit from the classes they're designed to mix into

```python
class SerializableMixin:
    """Mixin that adds JSON serialization to any class."""

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith("_")}

    def to_json(self) -> str:
        import json
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def from_json(cls, json_str: str):
        import json
        data = json.loads(json_str)
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj


class ValidatableMixin:
    """Mixin that adds validation hooks."""

    def validate(self) -> list[str]:
        """Return a list of validation errors."""
        errors = []
        for name, value in self.__dict__.items():
            validator = getattr(self.__class__, f"validate_{name}", None)
            if validator:
                error = validator(self, value)
                if error:
                    errors.append(error)
        return errors

    def is_valid(self) -> bool:
        return len(self.validate()) == 0


class TimestampMixin:
    """Mixin that adds created_at and updated_at timestamps."""

    def __init__(self, *args, **kwargs):
        from datetime import datetime
        super().__init__(*args, **kwargs)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def touch(self):
        from datetime import datetime
        self.updated_at = datetime.utcnow()


class User(TimestampMixin, SerializableMixin, ValidatableMixin):
    def __init__(self, name: str, email: str):
        super().__init__()
        self.name = name
        self.email = email

    def validate_email(self, value):
        if "@" not in value:
            return f"Invalid email: {value!r}"

    def validate_name(self, value):
        if not value.strip():
            return "Name cannot be empty"

u = User("Alice", "alice@example.com")
print(u.to_json())
print(u.is_valid())    # True
print(u.validate())    # []

u2 = User("Bob", "not-an-email")
print(u2.validate())   # ["Invalid email: 'not-an-email'"]
```

### Mixin Order Matters

Because of MRO, mixins should go **before** the main base class:

```python
class MyModel(TimestampMixin, SerializableMixin, BaseModel):
    ...
# TimestampMixin.__init__ → SerializableMixin (skips) → BaseModel.__init__
# super() chains through all of them
```

---

## 14. Design Principles

### Single Responsibility Principle

Each class should have one reason to change. When a class does too many things, changes to one responsibility break the other.

```python
# Bad — one class does three jobs
class UserManager:
    def create_user(self, name, email): ...
    def send_welcome_email(self, user): ...     # email logic here too?
    def save_to_database(self, user): ...       # and DB logic?

# Good — separated
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user: User): ...
    def find_by_email(self, email: str) -> User: ...

class EmailService:
    def send_welcome(self, user: User): ...

class UserRegistrationService:
    def __init__(self, repo: UserRepository, email: EmailService):
        self._repo = repo
        self._email = email

    def register(self, name: str, email: str) -> User:
        user = User(name, email)
        self._repo.save(user)
        self._email.send_welcome(user)
        return user
```

### Open/Closed Principle

Classes should be open for extension, closed for modification. Add new behavior by adding new classes, not by editing existing ones.

```python
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...

class NoDiscount(Discount):
    def apply(self, price): return price

class PercentageDiscount(Discount):
    def __init__(self, percent: float):
        self.percent = percent
    def apply(self, price): return price * (1 - self.percent / 100)

class FlatDiscount(Discount):
    def __init__(self, amount: float):
        self.amount = amount
    def apply(self, price): return max(0.0, price - self.amount)

class BuyTwoGetOneFree(Discount):
    def apply(self, price): return price * (2/3)

class Order:
    def __init__(self, items: list[float], discount: Discount = None):
        self._items = items
        self._discount = discount or NoDiscount()

    @property
    def total(self) -> float:
        subtotal = sum(self._items)
        return round(self._discount.apply(subtotal), 2)

# Adding a new discount type doesn't touch Order at all
```

### Dependency Inversion

High-level modules should not depend on low-level modules. Both should depend on abstractions.

```python
from abc import ABC, abstractmethod

class MessageBus(ABC):
    @abstractmethod
    def publish(self, topic: str, message: dict) -> None: ...

class KafkaMessageBus(MessageBus):
    def publish(self, topic, message):
        print(f"[Kafka] → {topic}: {message}")

class InMemoryMessageBus(MessageBus):
    def __init__(self):
        self._messages = []
    def publish(self, topic, message):
        self._messages.append((topic, message))
    @property
    def messages(self):
        return list(self._messages)

class OrderService:
    def __init__(self, bus: MessageBus):
        self._bus = bus   # depends on abstraction, not Kafka directly

    def place_order(self, order_id: str, items: list):
        # ... process order
        self._bus.publish("orders.placed", {"order_id": order_id, "items": items})

# In production:
service = OrderService(KafkaMessageBus())

# In tests:
bus = InMemoryMessageBus()
service = OrderService(bus)
service.place_order("001", ["apple", "banana"])
print(bus.messages)   # [('orders.placed', {'order_id': '001', 'items': [...]})]
```

### God Class Anti-Pattern

A god class knows too much and does too much. Signs:
- More than ~200 lines
- Has many unrelated methods
- Other classes constantly reach into it
- Touching it requires understanding the whole system

Break it apart by responsibility.

---

## 15. Practical Project — Inventory and Checkout Engine

This project applies everything above: composition, validation, descriptors, dunder methods, ABCs, and clean API design.

```python
from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Iterator
from decimal import Decimal, ROUND_HALF_UP
import uuid


# ─── Validators ──────────────────────────────────────────────────────────────

class PositiveDecimal:
    """Descriptor: validates and stores a positive Decimal."""

    def __set_name__(self, owner, name):
        self.public = name
        self.private = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        value = Decimal(str(value))
        if value < 0:
            raise ValueError(f"{self.public} must be non-negative, got {value}")
        setattr(obj, self.private, value)


class NonNegativeInt:
    """Descriptor: validates and stores a non-negative integer."""

    def __set_name__(self, owner, name):
        self.public = name
        self.private = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.public} must be int, got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"{self.public} must be non-negative, got {value}")
        setattr(obj, self.private, value)


# ─── Product ──────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Product:
    """Immutable product definition. Identified by SKU."""
    sku: str
    name: str
    price: Decimal
    category: str = "general"

    def __post_init__(self):
        if not self.sku.strip():
            raise ValueError("SKU cannot be empty")
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
        if self.price < 0:
            raise ValueError(f"Price cannot be negative: {self.price}")
        # frozen=True prevents direct assignment, use object.__setattr__ for coercion
        object.__setattr__(self, "sku", self.sku.strip().upper())
        object.__setattr__(self, "name", self.name.strip())
        object.__setattr__(self, "price", Decimal(str(self.price)))

    def __str__(self):
        return f"{self.name} ({self.sku}) — ${self.price:.2f}"


# ─── Inventory ───────────────────────────────────────────────────────────────

class Inventory:
    """Tracks stock levels. Thread-safety not included — add locks for production."""

    def __init__(self):
        self._stock: dict[str, int] = {}           # sku → quantity
        self._products: dict[str, Product] = {}    # sku → Product

    def add_product(self, product: Product, quantity: int = 0) -> None:
        if product.sku in self._products:
            raise ValueError(f"Product {product.sku!r} already registered. Use restock().")
        if quantity < 0:
            raise ValueError(f"Initial quantity cannot be negative: {quantity}")
        self._products[product.sku] = product
        self._stock[product.sku] = quantity

    def restock(self, sku: str, quantity: int) -> None:
        self._require_registered(sku)
        if quantity <= 0:
            raise ValueError(f"Restock quantity must be positive: {quantity}")
        self._stock[sku] += quantity

    def reserve(self, sku: str, quantity: int) -> None:
        self._require_registered(sku)
        if quantity <= 0:
            raise ValueError(f"Reserve quantity must be positive: {quantity}")
        available = self._stock[sku]
        if available < quantity:
            raise ValueError(
                f"Insufficient stock for {sku!r}: "
                f"need {quantity}, have {available}"
            )
        self._stock[sku] -= quantity

    def release(self, sku: str, quantity: int) -> None:
        """Return reserved items back to stock."""
        self._require_registered(sku)
        self._stock[sku] += quantity

    def available(self, sku: str) -> int:
        self._require_registered(sku)
        return self._stock[sku]

    def product(self, sku: str) -> Product:
        self._require_registered(sku)
        return self._products[sku]

    def _require_registered(self, sku: str) -> None:
        if sku not in self._products:
            raise KeyError(f"Unknown SKU: {sku!r}")

    def __contains__(self, sku: str) -> bool:
        return sku in self._products

    def __repr__(self) -> str:
        lines = [f"  {sku}: {qty} units" for sku, qty in self._stock.items()]
        return "Inventory(\n" + "\n".join(lines) + "\n)"


# ─── Cart ────────────────────────────────────────────────────────────────────

@dataclass
class CartItem:
    product: Product
    quantity: int

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError(f"Quantity must be positive: {self.quantity}")

    @property
    def subtotal(self) -> Decimal:
        return self.product.price * self.quantity

    def __repr__(self):
        return f"CartItem({self.product.sku!r}, qty={self.quantity}, subtotal=${self.subtotal:.2f})"


class Cart:
    def __init__(self):
        self._items: dict[str, CartItem] = {}   # sku → CartItem

    def add(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError(f"Quantity must be positive: {quantity}")
        if product.sku in self._items:
            existing = self._items[product.sku]
            self._items[product.sku] = CartItem(product, existing.quantity + quantity)
        else:
            self._items[product.sku] = CartItem(product, quantity)

    def remove(self, sku: str, quantity: int = None) -> None:
        if sku not in self._items:
            raise KeyError(f"SKU not in cart: {sku!r}")
        if quantity is None or quantity >= self._items[sku].quantity:
            del self._items[sku]
        else:
            item = self._items[sku]
            self._items[sku] = CartItem(item.product, item.quantity - quantity)

    def clear(self) -> None:
        self._items.clear()

    @property
    def items(self) -> list[CartItem]:
        return list(self._items.values())

    @property
    def subtotal(self) -> Decimal:
        return sum(item.subtotal for item in self._items.values())

    def __len__(self) -> int:
        return sum(item.quantity for item in self._items.values())

    def __contains__(self, sku: str) -> bool:
        return sku in self._items

    def __iter__(self) -> Iterator[CartItem]:
        return iter(self._items.values())

    def __repr__(self) -> str:
        lines = [f"  {item}" for item in self._items.values()]
        return f"Cart(\n" + "\n".join(lines) + f"\n  subtotal=${self.subtotal:.2f}\n)"


# ─── Discount Strategy ────────────────────────────────────────────────────────

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, subtotal: Decimal, cart: Cart) -> Decimal:
        """Return the discount AMOUNT (not the new total)."""
        ...

    @property
    @abstractmethod
    def description(self) -> str: ...


class NoDiscount(DiscountStrategy):
    def apply(self, subtotal, cart): return Decimal("0")
    @property
    def description(self): return "No discount"


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        if not (0 < percent <= 100):
            raise ValueError(f"Percent must be 0-100: {percent}")
        self.percent = Decimal(str(percent))

    def apply(self, subtotal, cart):
        return (subtotal * self.percent / 100).quantize(Decimal("0.01"), ROUND_HALF_UP)

    @property
    def description(self):
        return f"{self.percent}% off"


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = Decimal(str(amount))

    def apply(self, subtotal, cart):
        return min(self.amount, subtotal)

    @property
    def description(self):
        return f"${self.amount:.2f} off"


class CategoryDiscount(DiscountStrategy):
    """Percentage discount on items in a specific category."""

    def __init__(self, category: str, percent: float):
        self.category = category
        self.percent = Decimal(str(percent))

    def apply(self, subtotal, cart):
        category_total = sum(
            item.subtotal for item in cart
            if item.product.category == self.category
        )
        return (category_total * self.percent / 100).quantize(Decimal("0.01"), ROUND_HALF_UP)

    @property
    def description(self):
        return f"{self.percent}% off {self.category!r} items"


# ─── Receipt ──────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Receipt:
    order_id: str
    items: tuple[CartItem, ...]
    subtotal: Decimal
    discount_description: str
    discount_amount: Decimal
    tax_rate: Decimal
    tax_amount: Decimal
    total: Decimal

    def __str__(self) -> str:
        lines = [
            f"{'─'*50}",
            f"  ORDER: {self.order_id}",
            f"{'─'*50}",
        ]
        for item in self.items:
            lines.append(f"  {item.product.name:<25} {item.quantity:>3} × ${item.product.price:>7.2f} = ${item.subtotal:>8.2f}")
        lines += [
            f"{'─'*50}",
            f"  {'Subtotal':40} ${self.subtotal:>8.2f}",
            f"  {self.discount_description:40} -${self.discount_amount:>7.2f}",
            f"  {f'Tax ({self.tax_rate*100:.0f}%)':40} ${self.tax_amount:>8.2f}",
            f"{'═'*50}",
            f"  {'TOTAL':40} ${self.total:>8.2f}",
            f"{'─'*50}",
        ]
        return "\n".join(lines)


# ─── Checkout ─────────────────────────────────────────────────────────────────

class Checkout:
    TAX_RATE = Decimal("0.08")

    def __init__(self, inventory: Inventory, discount: DiscountStrategy = None):
        self._inventory = inventory
        self._discount = discount or NoDiscount()

    def process(self, cart: Cart) -> Receipt:
        if len(cart) == 0:
            raise ValueError("Cannot checkout an empty cart")

        # Verify stock availability before reserving anything
        for item in cart:
            available = self._inventory.available(item.product.sku)
            if available < item.quantity:
                raise ValueError(
                    f"Insufficient stock for {item.product.name!r}: "
                    f"need {item.quantity}, have {available}"
                )

        # Reserve stock
        reserved = []
        try:
            for item in cart:
                self._inventory.reserve(item.product.sku, item.quantity)
                reserved.append((item.product.sku, item.quantity))
        except Exception:
            # Roll back any partial reservations
            for sku, qty in reserved:
                self._inventory.release(sku, qty)
            raise

        # Calculate totals
        subtotal = cart.subtotal
        discount_amount = self._discount.apply(subtotal, cart)
        discounted = subtotal - discount_amount
        tax_amount = (discounted * self.TAX_RATE).quantize(Decimal("0.01"), ROUND_HALF_UP)
        total = discounted + tax_amount

        return Receipt(
            order_id=str(uuid.uuid4())[:8].upper(),
            items=tuple(cart.items),
            subtotal=subtotal,
            discount_description=self._discount.description,
            discount_amount=discount_amount,
            tax_rate=self.TAX_RATE,
            tax_amount=tax_amount,
            total=total,
        )


# ─── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Setup products
    apple  = Product("apple-001", "Organic Apple",  Decimal("1.50"),  category="produce")
    milk   = Product("milk-001",  "Whole Milk 1L",   Decimal("2.99"),  category="dairy")
    bread  = Product("bread-001", "Sourdough Loaf",  Decimal("5.49"),  category="bakery")
    cheese = Product("cheese-001","Aged Cheddar",    Decimal("8.99"),  category="dairy")

    # Stock inventory
    inventory = Inventory()
    inventory.add_product(apple,  quantity=100)
    inventory.add_product(milk,   quantity=50)
    inventory.add_product(bread,  quantity=30)
    inventory.add_product(cheese, quantity=20)

    print(inventory)

    # Build a cart
    cart = Cart()
    cart.add(apple,  quantity=6)
    cart.add(milk,   quantity=2)
    cart.add(bread,  quantity=1)
    cart.add(cheese, quantity=1)

    print(cart)

    # Checkout with a 10% discount on dairy
    checkout = Checkout(inventory, discount=CategoryDiscount("dairy", 10))
    receipt = checkout.process(cart)

    print(receipt)

    # Verify inventory was updated
    print(f"Apples remaining: {inventory.available('APPLE-001')}")
    print(f"Milk remaining:   {inventory.available('MILK-001')}")
```

---

## Appendix — Quick Reference

### Dunder Method Cheatsheet

| Method | Trigger | Return |
|--------|---------|--------|
| `__init__` | `obj = Class(...)` | `None` |
| `__new__` | Before `__init__` | new instance |
| `__repr__` | `repr(obj)`, REPL | `str` |
| `__str__` | `str(obj)`, `print()` | `str` |
| `__format__` | `f"{obj:spec}"` | `str` |
| `__bool__` | `bool(obj)`, `if obj:` | `bool` |
| `__len__` | `len(obj)` | `int >= 0` |
| `__contains__` | `x in obj` | `bool` |
| `__iter__` | `for x in obj:` | iterator |
| `__next__` | next value in iterator | value or raise `StopIteration` |
| `__getitem__` | `obj[key]` | value |
| `__setitem__` | `obj[key] = val` | `None` |
| `__delitem__` | `del obj[key]` | `None` |
| `__enter__` | `with obj:` | object (often `self`) |
| `__exit__` | leaving `with` block | `bool` (suppress exception?) |
| `__call__` | `obj(...)` | anything |
| `__eq__` | `obj == other` | `bool` or `NotImplemented` |
| `__lt__` | `obj < other` | `bool` or `NotImplemented` |
| `__hash__` | `hash(obj)` | `int` |
| `__add__` | `obj + other` | result or `NotImplemented` |
| `__radd__` | `other + obj` | result or `NotImplemented` |
| `__iadd__` | `obj += other` | `self` (usually) |
| `__neg__` | `-obj` | result |
| `__abs__` | `abs(obj)` | result |
| `__get__` | descriptor attribute access | value |
| `__set__` | descriptor attribute assignment | `None` |
| `__set_name__` | class body execution | `None` |
| `__init_subclass__` | subclass created | `None` |
| `__class_getitem__` | `Class[T]` | generic alias |

### Inheritance Decision Tree

```
Need to reuse code from another class?
├── Is the relationship truly "is-a"?
│   ├── Yes → Use inheritance
│   │   └── Override methods with super() calls
│   └── No → Use composition (has-a)
│       └── Delegate calls explicitly
│
Need to add behavior to many unrelated classes?
└── Use a Mixin (small, focused, cooperative super())

Need to enforce an interface?
├── You control the implementations → ABC
└── You don't control them → Protocol
```

### When to Use Each Tool

| Tool | Use when |
|------|----------|
| `@property` | Validation on assignment, computed values, stable API |
| `@cached_property` | Expensive computed value, called repeatedly |
| `@classmethod` | Alternate constructors, class-level operations |
| `@staticmethod` | Utility functions logically belonging to the class |
| `@dataclass` | Data containers, value objects, DTOs |
| `@dataclass(frozen=True)` | Immutable value objects, dict/set keys |
| `__slots__` | Millions of instances, memory-critical code |
| `ABC` | Enforced interfaces with shared concrete methods |
| `Protocol` | Duck-typed interfaces, no inheritance coupling |
| Descriptor | Reusable attribute validation across many classes |
| Metaclass | Class creation hooks, auto-registration, ORMs |
| Mixin | Opt-in behaviors added to multiple unrelated classes |
| Composition | "has-a", swappable behaviors, testability |