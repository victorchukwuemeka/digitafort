# Lesson 4: Encapsulation and Properties

## Goal
Protect internal state and validate data with properties.

## Key Concepts
- Encapsulation with internal attributes
- `@property` and setters
- Validation and invariants

## Example
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

## Quick Exercises
1. Add a `quantity` property that rejects negative values.
2. Add a `total_value` read-only property.
