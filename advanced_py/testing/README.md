# Testing in Python: unittest and pytest

Testing is essential for building robust, maintainable software. This course covers two of the most popular testing frameworks in Python: `unittest` and `pytest`.

## 1. Why Test?
- **Reliability:** Ensure code works as expected.
- **Regression Prevention:** Make sure new changes don't break existing features.
- **Documentation:** Tests often serve as examples of how to use code.

---

## 2. unittest (The Standard Library Way)
`unittest` is Python's built-in testing framework, inspired by JUnit. It follows an Object-Oriented approach.

### Key Concepts:
- **Test Case:** The smallest unit of testing. It checks for a specific response to a particular set of inputs. `unittest` provides a base class, `TestCase`.
- **Assertions:** Methods like `assertEqual()`, `assertTrue()`, `assertRaises()` used to check conditions.
- **Test Suite:** A collection of test cases.
- **Test Runner:** A component that orchestrates the execution of tests and provides the outcome.
- **Setup & Teardown:** `setUp()` runs before every test; `tearDown()` runs after.

### Example:
```python
import unittest

def multiply(a, b):
    return a * b

class TestMathOperations(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
```

---

## 3. pytest (The Modern Way)
`pytest` is a third-party framework (requires `pip install pytest`) that is widely preferred for its simplicity and powerful features.

### Key Features:
- **Simple Assertions:** Just use Python's built-in `assert` statement. No need for `self.assertEqual()`.
- **Function-based:** No need to wrap tests in classes (though you can).
- **Fixtures:** Modular, reusable setup/teardown code.
- **Parametrization:** Run the same test with different inputs using `@pytest.mark.parametrize`.
- **Plugins:** A massive ecosystem of plugins (e.g., `pytest-cov` for coverage).

### Example:
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (20, 5, 4),
    (0, 5, 0),
])
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected
```

---

## 4. Comparing unittest and pytest

| Feature | unittest | pytest |
|---------|----------|--------|
| **Origin** | Built-in | Third-party (`pip install pytest`) |
| **Style** | Object-Oriented (Classes) | Functional (mostly) |
| **Assertions**| `self.assertEqual` | `assert a == b` |
| **Setup/Teardown** | `setUp`/`tearDown` | Fixtures |
| **Extensibility**| Limited | Highly extensible via plugins |

---

## 5. Exercises
Complete the following in the provided `.py` files:

1. **Unittest Practice (`unittest_exercises.py`):**
   - Create a `BankAccount` class with `deposit` and `withdraw` methods.
   - Write a test class that ensures:
     - Deposits increase the balance.
     - Withdrawals decrease the balance.
     - Withdrawals fail if funds are insufficient.

2. **Pytest Practice (`pytest_exercises.py`):**
   - Implement a function that checks if a string is a palindrome.
   - Write tests for:
     - Simple palindromes (e.g., "racecar").
     - Mixed case palindromes (e.g., "Madam").
     - Non-palindromes.
     - Use `@pytest.mark.parametrize` for multiple cases.
