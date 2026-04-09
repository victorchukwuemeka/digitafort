# Lesson 8: Dataclasses and Slots

## Goal
Reduce boilerplate and improve memory usage.

## Key Concepts
- `@dataclass` basics
- `frozen=True` for immutability
- `slots=True` for memory optimization

## Example
```python
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Point:
    x: int
    y: int
```

## Quick Exercises
1. Convert a `User` class into a dataclass.
2. Add default values and type hints.
