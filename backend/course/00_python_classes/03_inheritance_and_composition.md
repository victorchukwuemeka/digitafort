# Lesson 3: Inheritance and Composition

## Goal
Understand when to extend a class and when to combine classes.

## Key Concepts
- Inheritance with subclasses
- Method overriding
- `super()` basics
- Composition (having objects as attributes)

## Example (Inheritance)
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"
```

## Example (Composition)
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

## Notes
- Inheritance is good for "is-a" relationships.
- Composition is good for "has-a" relationships.

## Quick Exercises
1. Create a `BaseUser` class and a `AdminUser` subclass.
2. Build a `Blog` class that "has a" `PostRepository`.
