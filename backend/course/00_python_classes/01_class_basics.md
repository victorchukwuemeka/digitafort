# Lesson 1: Class Basics and Object Lifecycle

## Goal
Build a solid mental model of what a class is, how objects are created, and how methods receive `self`.

## Key Concepts
- Class definition and instantiation
- Instance methods and `self`
- The object lifecycle: create -> use -> discard
- Identity vs equality

## Example
```python
class User:
    def greet(self):
        return "Hello!"

u = User()
print(u.greet())
```

## Notes
- `self` is the instance itself.
- Methods are functions that live on the class, bound to the instance at call time.

## Quick Exercises
1. Create a `Car` class with a `start()` method that returns a string.
2. Instantiate two `Car` objects and call `start()` on both.
3. Print `id(car1)` and `id(car2)` and explain why they differ.
