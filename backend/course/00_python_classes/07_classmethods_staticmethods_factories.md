# Lesson 7: Classmethods, Staticmethods, and Factory Patterns

## Goal
Create alternate constructors and clean factory APIs.

## Key Concepts
- `@classmethod` for alternate constructors
- `@staticmethod` for utility helpers
- Simple factory patterns

## Example
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["email"])
```

## Quick Exercises
1. Add a `from_csv_row` classmethod to a `User` class.
2. Write a staticmethod `is_valid_email(email)`.
