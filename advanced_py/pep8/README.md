# PEP 8 — Python Style Guide

## 1. What is PEP 8?
PEP 8 is Python's official style guide — a set of rules for writing clean, readable code. It won't affect whether your code runs, but it makes your code look professional and familiar to other Python developers.

Start by installing a tool to check your style:

```bash
pip install pycodestyle
pycodestyle my_script.py
```

Or auto-format with Black (the modern standard):

```bash
pip install black
black my_script.py
```

Let's look at the rules with examples of wrong vs right.

## 2. Indentation — 4 Spaces
Python uses indentation for blocks. PEP 8 says 4 spaces per level — no tabs.

```python
# Wrong
def greet(name):
	if name:		# tab — invisible but wrong
		print("Hello")

# Correct
def greet(name):
    if name:
        print("Hello")
```

## 3. Line Length — 79 Characters
Keep lines under 79 characters. No horizontal scrolling.

```python
# Wrong — too long, requires scrolling
result = some_long_function_name(argument_one, argument_two, argument_three, argument_four)

# Correct — break with parentheses
result = some_long_function_name(
    argument_one, argument_two,
    argument_three, argument_four
)

# Alternative for expressions
total = (price * quantity + tax
         - discount + shipping)
```

## 4. Blank Lines
Blank lines separate logical sections.

```python
import os
import sys


class UserProfile:
    """Two blank lines above top-level classes/functions."""

    def __init__(self):
        pass

    def get_name(self):
        """One blank line between methods."""
        pass


def outside_function():
    """Two blank lines above this too."""
    pass
```

## 5. Imports — Grouped and Ordered
```python
# Wrong — mixed up
import os
import my_module
import sys
import requests

# Correct — standard lib, then third-party, then local
import os
import sys

import requests

from myproject import config
```

## 6. Naming Conventions
Names communicate what something is:

```python
# Wrong — inconsistent
class customer:
    def getTotal(self):
        pass
MAX_VALUE = 100

# Correct — snake_case for variables/functions, PascalCase for classes
MAX_VALUE = 100

class Customer:
    def get_total(self):
        pass
```

## 7. Whitespace
```python
# Wrong
x=1
y = x+2
spam( ham[ 1 ], { eggs: 2 } )

# Correct
x = 1
y = x + 2
spam(ham[1], {eggs: 2})
```

## 8. Comments — Explain Why
Comments should explain the reasoning, not restate the code:

```python
# Wrong — obvious
x = x + 1  # increment x by 1

# Correct — explains the reasoning
# Retry up to 3 times because the API returns 429 under load
for attempt in range(3):
    try:
        return fetch_data()
    except HTTPError:
        time.sleep(2 ** attempt)
```

## 9. Docstrings
Docstrings document functions and classes — what they do, their parameters, and return values:

```python
def calculate_tax(price: float, rate: float) -> float:
    """Calculate sales tax for a given price and rate.

    Args:
        price: Pre-tax price in dollars.
        rate: Tax rate as decimal (0.1 for 10%).

    Returns:
        Tax amount in dollars.
    """
    return price * rate


class BankAccount:
    """Represents a bank account with deposit and withdrawal."""
    ...
```

## 10. Pythonic Comparisons
```python
# Wrong
if len(items) > 0:
if x == None:
if type(x) == int:
for i in range(len(items)):

# Correct
if items:               # truthiness
if x is None:           # identity
if isinstance(x, int):  # type check
for item in items:      # direct iteration
```

The rule: write code for humans to read, not just for machines to execute.
