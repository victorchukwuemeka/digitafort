# Lesson 4: Encapsulation, Properties, and Dunder Methods

## Goal
Use properties to control access and add helpful behavior with dunder methods.

## Key Concepts
- Encapsulation (protecting internal state)
- `@property` and setters
- Common dunder methods: `__repr__`, `__str__`, `__eq__`

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

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"
```

## Notes
- Use leading underscore for "internal" attributes.
- `__repr__` should be developer-friendly.

## Quick Exercises
1. Add a `__str__` to `Product` that prints a user-friendly sentence.
2. Implement `__eq__` to compare products by name and price.
