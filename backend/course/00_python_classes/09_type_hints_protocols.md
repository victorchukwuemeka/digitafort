# Lesson 9: Type Hints and Protocols (Designing Interfaces)

## Goal
Use typing to communicate class contracts clearly.

## Key Concepts
- Type hints for classes
- `Protocol` for structural typing
- Designing clean interfaces

## Example
```python
from typing import Protocol

class Storable(Protocol):
    def save(self) -> None: ...

class User:
    def save(self) -> None:
        print("saved")
```

## Quick Exercises
1. Define a `Cacheable` protocol with `cache_key()`.
2. Make a class satisfy it without inheritance.
