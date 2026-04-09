# Lesson 1: Class Basics

## Goal
Understand how to define a class, create objects, and call methods.

## Key Concepts
- Class definition syntax
- Instance creation
- Instance methods and `self`

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
- Methods are just functions defined inside the class.

## Quick Exercises
1. Create a `Car` class with a `start()` method that returns a string.
2. Instantiate two `Car` objects and call `start()` on both.
