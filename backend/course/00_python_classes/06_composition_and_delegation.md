# Lesson 6: Composition and Delegation

## Goal
Prefer composition for flexible designs and cleaner APIs.

## Key Concepts
- "Has-a" relationships
- Delegating responsibilities
- Avoiding deep inheritance trees

## Example
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

## Quick Exercises
1. Build a `Logger` class and compose it inside a `Service`.
2. Delegate `log()` calls from `Service` to `Logger`.
