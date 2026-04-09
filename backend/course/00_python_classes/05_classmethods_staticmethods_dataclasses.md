# Lesson 5: Classmethods, Staticmethods, and Dataclasses

## Goal
Know when to use class-level behavior and reduce boilerplate with dataclasses.

## Key Concepts
- `@classmethod` for alternate constructors
- `@staticmethod` for utility behavior
- `@dataclass` for clean data containers

## Example
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def origin(cls):
        return cls(0, 0)

    @staticmethod
    def distance(a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
```

## Notes
- Use `@classmethod` when the method should construct or configure the class.
- Use `@staticmethod` for related helpers that don't touch `self` or `cls`.

## Quick Exercises
1. Add a classmethod to create a `Point` from a tuple.
2. Write a staticmethod that checks if two points are on the same axis.
