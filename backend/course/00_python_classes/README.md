# Python Classes (OOP) 

## 1. What a Class Really Is
A class is a **blueprint**. An object is a **concrete instance** that holds its own state and can call the class’s methods.

### The Real Mental Model: Attribute Lookup
When you access `obj.attr`, Python looks in this exact order:
1. The instance dictionary (`obj.__dict__`)
2. The class (`ClassName.__dict__`)
3. Base classes in method resolution order (MRO)

This explains why class attributes are shared until you override them on an instance.

```python
class User:
    role = "member"

u = User()
print(u.role)      # class attribute

u.role = "admin"
print(u.role)      # instance attribute shadows class
print(User.role)   # still "member"
```

### Identity vs Equality
- `is` means **same object** (same memory)
- `==` means **same value** (if `__eq__` exists)

```python
u1 = User()
u2 = User()
print(u1 is u2)  # False
print(u1 == u2)  # False (no __eq__ defined)
```

**Why this matters:** if you don’t define `__eq__`, two objects with identical data will still be treated as unequal.

**Exercises**
1. Create two objects and compare `is` vs `==`.
2. Implement `__eq__` and compare again.
3. Explain in one sentence where Python looks first for attributes.

---

## 2. `__init__`, State, and the Class vs Instance Trap
`__init__` runs when an object is created. It is where you define **per‑object state**.

```python
class User:
    role = "member"  # class variable

    def __init__(self, name, email):
        self.name = name
        self.email = email
```

### The Classic Bug: Shared Mutable Class Attributes
```python
class Bad:
    tags = []  # shared by all instances
```

Every instance sees the same list. This causes subtle bugs.

Correct pattern:
```python
class Good:
    def __init__(self):
        self.tags = []
```

**Why this matters:** a shared list can cause data leakage between objects in real applications (e.g., users seeing each other’s data).

**Exercises**
1. Create the shared‑list bug and demonstrate it.
2. Fix it by moving the list into `__init__`.

---

## 3. Inheritance, `super()`, and MRO
Inheritance is useful only when the relationship is truly **is‑a**. Otherwise, it creates fragile code.

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"
```

### `super()` = Cooperative Initialization
`super()` is not “parent only”; it is **cooperative** and follows MRO. This matters in multiple inheritance.

```python
class Base:
    def __init__(self):
        print("Base init")

class Child(Base):
    def __init__(self):
        super().__init__()
        print("Child init")
```

### MRO (Method Resolution Order)
```python
print(Child.mro())
```

**Why this matters:** incorrect inheritance trees make bugs hard to trace because method lookup becomes confusing.

**Exercises**
1. Build `BaseUser` and `AdminUser`.
2. Add a shared `log()` method and reuse it.
3. Print and explain `AdminUser.mro()`.

---

## 4. Encapsulation and Properties (Real Validation)
Encapsulation in Python means **controlling access** to internal state, not hiding it completely.

Use properties when you want:
- validation
- computed values
- a stable API that can change internally without breaking callers

```python
class Product:
    def __init__(self, name, price):
        self._price = price
        self.name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be positive")
        self._price = value
```

**Exercises**
1. Add a `quantity` property that rejects negatives.
2. Add a `total_value` read‑only property.

---

## 5. Dunder Methods (Make Objects Feel Native)
Dunder methods define how your class behaves with Python built‑ins.

### `__repr__` vs `__str__`
- `__repr__`: unambiguous, for developers
- `__str__`: readable, for users

### `__eq__`, Ordering, and Hashing
If you define `__eq__`, you must think about `__hash__` and immutability, especially if objects are used as dictionary keys.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name and self.price == other.price
```

**Exercises**
1. Add `__str__` to print a friendly sentence.
2. Add `__lt__` to compare by price.
3. Decide whether your class should be hashable and explain why.

---

## 6. Composition and Delegation (Prefer This Over Inheritance)
Composition is a **has‑a** relationship and usually scales better than inheritance.

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
```

**Why this matters:** composition keeps your classes smaller and easier to test.

**Exercises**
1. Build a `Logger` and delegate `log()` calls from a `Service`.
2. Replace an inheritance relationship with composition.

---

## 7. Classmethods, Staticmethods, and Factories
This section is about **where a method belongs**. Ask two questions:
1. Does this method need the class itself (`cls`)?
2. Does this method need an instance (`self`)?

If it needs the class, use `@classmethod`. If it needs neither, use `@staticmethod`. If it needs the instance, keep it a normal method.

### `@classmethod` (Alternate Constructors)
Use a classmethod when you want a **named constructor** that returns an instance of the class. The key point is it receives `cls`, so it respects subclasses automatically.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["email"])
```

**Why this matters:** if you subclass `User`, `from_dict` will create the subclass, not the base class.

```python
class AdminUser(User):
    pass

admin = AdminUser.from_dict({"name": "Ada", "email": "ada@example.com"})
print(type(admin).__name__)  # AdminUser
```

### `@staticmethod` (Utility Helpers)
Use a staticmethod for helper logic that **belongs with the class conceptually** but does not need `self` or `cls`.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email
```

**Why this matters:** you keep related logic near the class without faking a `self` or `cls` parameter.

### Factory Methods (Putting It Together)
A factory method is just a classmethod that **chooses how to build objects** based on input.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_source(cls, source_type, payload):
        if source_type == "dict":
            return cls(payload["name"], payload["email"])
        if source_type == "csv":
            name, email = payload.split(",")
            return cls(name.strip(), email.strip())
        raise ValueError("unknown source_type")
```

**Pitfalls to avoid**
- Do not use `@staticmethod` when you actually need `cls`. You will lose subclass support.
- Do not use `@classmethod` when you need per‑instance state; that belongs in normal methods.

**Exercises**
1. Add `from_csv_row` as a classmethod that parses `"name,email"`.
2. Add `is_valid_email` as a staticmethod and use it inside `from_dict`.
3. Create a subclass and confirm `from_dict` returns the subclass.

---

## 8. Dataclasses and Slots
Dataclasses reduce boilerplate for data containers and make your intent clear.

```python
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Point:
    x: int
    y: int
```

**Why this matters:** `frozen=True` makes objects immutable and safer to use as keys.

**Exercises**
1. Convert a normal class to a dataclass.
2. Explain when `slots=True` is useful.

---

## 9. Type Hints and Protocols (Interfaces Without Inheritance)
Protocols allow **structural typing**: if it walks like a duck, it’s accepted.

```python
from typing import Protocol

class Storable(Protocol):
    def save(self) -> None: ...

class User:
    def save(self) -> None:
        print("saved")
```

**Why this matters:** you can enforce a contract without forcing a class hierarchy.

**Exercises**
1. Define a `Cacheable` protocol with `cache_key()`.
2. Make a class satisfy it without inheritance.

---

# Practical Project: Inventory + Checkout Engine

## Goal
Build a small but realistic system using composition, validation, and clean APIs.

### Classes to implement
1. **Product** (`sku`, `name`, `price`, validation)
2. **Inventory** (stock tracking + add/remove/available)
3. **CartItem** (`product`, `qty`)
4. **Cart** (add/remove/total)
5. **Checkout** (verify stock, deduct, return receipt)

### Stretch Goals
- Discounts with a strategy object
- Use `@dataclass` for `Product` and `CartItem`
- Compare products by `sku`

### Starter File
See `00_python_classes/inventory.py` for a starter implementation.

---

## Suggested Path (Use This to Avoid Overload)
1. Read sections 1–3 and build tiny examples as you go.
2. Practice 4–6 with validation and composition.
3. Finish 7–10 and refactor your code to be cleaner.
4. Complete the practical in `inventory.py`.
