# Error Handling

Error handling is how we prepare our programs to deal with bad input, missing data, unexpected states, or failed operations without crashing unnecessarily.

## Why Error Handling Matters

Programs run in the real world, and the real world is messy.

- Files may be missing
- Users may enter invalid data
- Networks may fail
- Databases may be unavailable

Good error handling makes software safer, easier to maintain, and easier to debug.

## Exceptions in Python

Python uses exceptions to represent runtime problems.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That was not a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

## Main Parts of Error Handling

### `try`

Put risky code here.

### `except`

Handle specific errors here.

### `else`

Run this if no exception happened.

### `finally`

Run this no matter what, often for cleanup.

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
else:
    print(file.read())
finally:
    print("Operation finished.")
```

## Good Practices

- Catch specific exceptions instead of using a broad catch-all.
- Write helpful error messages.
- Fail early when input is invalid.
- Do not hide important errors silently.
- Log errors when needed.

## Key Takeaway

Error handling is about expecting failure points and designing software that responds clearly and safely when those failures happen.
