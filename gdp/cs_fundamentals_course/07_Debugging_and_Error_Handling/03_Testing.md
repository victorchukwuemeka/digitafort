# Testing

Testing is the practice of checking whether software behaves the way we expect. It helps us catch bugs early, protect against regressions, and build confidence when changing code.

## Why Testing Matters

- It confirms that code works for expected cases.
- It helps reveal edge cases.
- It prevents old bugs from returning.
- It makes refactoring safer.

## Common Types of Testing

### Unit Testing

Tests one small piece of code, such as a function or class method.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

### Integration Testing

Checks that multiple parts of the system work together correctly.

Example:

- API plus database
- frontend plus backend
- file reader plus parser

### Manual Testing

A human tries the software directly to verify behavior.

## Good Test Design

- Test normal cases.
- Test edge cases.
- Test invalid input.
- Keep tests small and readable.
- Make expected behavior explicit.

## Example Edge Cases

For a function that divides two numbers, good tests include:

- normal division
- dividing by one
- dividing zero
- dividing by zero
- negative values

## Key Takeaway

Testing does not replace thinking, but it gives us a safety net. The better our tests, the easier it is to build and improve software with confidence.
