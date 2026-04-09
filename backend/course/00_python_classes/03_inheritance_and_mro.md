# Lesson 3: Inheritance, `super()`, and MRO

## Goal
Extend classes safely and understand method resolution order (MRO).

## Key Concepts
- Subclassing and overriding
- `super()` for cooperative multiple inheritance
- MRO basics and why it matters

## Example
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"
```

## `super()` Example
```python
class Base:
    def __init__(self):
        print("Base init")

class Child(Base):
    def __init__(self):
        super().__init__()
        print("Child init")
```

## Quick Exercises
1. Create a `BaseUser` class and an `AdminUser` subclass.
2. Add a shared `log()` method in the base class and reuse it in the subclass.
3. Print `Child.mro()` and explain the order.
