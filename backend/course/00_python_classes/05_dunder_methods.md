# Lesson 5: Dunder Methods and Object Behavior

## Goal
Make your classes behave naturally with built-in Python features.

## Key Concepts
- `__repr__` vs `__str__`
- `__eq__` and ordering
- `__hash__` and immutability

## Example
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

## Quick Exercises
1. Add `__str__` to print a friendly sentence.
2. Add ordering (`__lt__`) to compare by price.
