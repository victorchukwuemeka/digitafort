# Lesson 2: `__init__`, Attributes, and State

## Goal
Model object state using attributes and understand class vs instance variables.

## Key Concepts
- `__init__` runs on creation
- Instance attributes live on `self`
- Class attributes are shared
- Mutability pitfalls with class attributes

## Example
```python
class User:
    role = "member"  # class variable

    def __init__(self, name, email):
        self.name = name
        self.email = email

u = User("Ada", "ada@example.com")
print(u.name, u.role)
```

## Common Pitfall
```python
class Bad:
    tags = []  # shared by all instances!
```

## Quick Exercises
1. Add an `age` attribute to the `User` class.
2. Make a `User` with a custom `role` and print both values.
3. Fix a shared-list bug by moving the list into `__init__`.
