# Lesson 2: `__init__` and Attributes

## Goal
Learn how to store state on objects using instance attributes.

## Key Concepts
- `__init__` runs when a new object is created
- Instance attributes live on `self`
- Class vs instance variables

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

## Notes
- Use class variables for shared defaults.
- Use instance attributes for per-object state.

## Quick Exercises
1. Add an `age` attribute to the `User` class.
2. Make a `User` with a custom `role` and print both values.
