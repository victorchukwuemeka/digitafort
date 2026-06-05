# Debugging Fundamentals

Debugging is the process of finding, understanding, and fixing problems in a program. A strong developer does not just write code well, but also investigates failures calmly and methodically.

## What Debugging Means

When code does not behave as expected, the goal is to answer three questions:

1. What happened?
2. Why did it happen?
3. How do we fix it without breaking something else?

## Common Types of Bugs

### Syntax Errors

These happen when the code breaks the language rules.

```python
print("hello"
```

### Runtime Errors

These happen while the program is running.

```python
10 / 0
```

### Logic Errors

The code runs, but the result is wrong.

```python
def add(a, b):
    return a - b
```

## Good Debugging Habits

- Reproduce the bug consistently.
- Read the error message carefully.
- Reduce the problem to the smallest failing example.
- Check inputs, outputs, and assumptions.
- Change one thing at a time.
- Retest after each fix.

## Useful Debugging Techniques

### Print Debugging

Add temporary print statements to inspect values.

```python
def divide(a, b):
    print("a =", a, "b =", b)
    return a / b
```

### Step-by-Step Tracing

Follow the code line by line to see where behavior changes.

### Rubber Duck Debugging

Explain your code out loud, step by step. Very often the mistake becomes obvious.

### Using a Debugger

A debugger lets you:

- pause execution
- inspect variables
- step into functions
- step over lines
- watch values change

## Key Takeaway

Debugging is not guessing. It is a structured investigation process that turns confusion into evidence and evidence into a fix.
