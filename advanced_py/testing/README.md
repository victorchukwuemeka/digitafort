# Testing in Python: unittest and pytest

Testing is essential for building robust, maintainable software. This course covers two of the most popular testing frameworks in Python: `unittest` and `pytest`.

## 1. Why Test?
- **Reliability:** Ensure code works as expected.
- **Regression Prevention:** Make sure new changes don't break existing features.
- **Documentation:** Tests often serve as examples of how to use code.
- **Confidence while refactoring:** Good tests let you improve code structure without fear.
- **Faster debugging:** Small focused tests make it easier to find what broke.

### What makes a good test?
- It checks one clear behavior.
- It has a descriptive name.
- It is repeatable and independent from other tests.
- It fails for the right reason.
- It is easy to read and maintain.

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

### Common `unittest` Assertions
- `assertEqual(a, b)` checks that two values are equal.
- `assertTrue(x)` checks that a value is truthy.
- `assertFalse(x)` checks that a value is falsy.
- `assertIn(item, collection)` checks membership.
- `assertRaises(Error)` checks that code raises an exception.

### Running `unittest`
From the `testing` directory:

```bash
python -m unittest unittest_exercises.py
```

Or let `unittest` discover tests automatically:

```bash
python -m unittest discover
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

### Why many developers like `pytest`
- Test files and test functions are quick to write.
- Failure messages are usually easier to read.
- Fixtures reduce repeated setup code.
- Parametrization helps you cover many inputs with little duplication.

### Running `pytest`
From the `testing` directory:

```bash
pytest
```

Run a specific file:

```bash
pytest pytest_exercises.py
```

Run with more detail:

```bash
pytest -v
```

Stop on the first failure:

```bash
pytest -x
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

## 5. Testing Levels: From Unit Tests to the Others
When people say "testing," they usually mean several layers of testing, not just one.

### Unit Tests
Unit tests check one small piece of code in isolation, such as a function or a single class method.

Examples:
- Testing that `multiply(2, 3)` returns `6`
- Testing that `BankAccount.withdraw()` raises an error when balance is too low

Why use them:
- They are fast.
- They are easy to debug.
- They help catch logic errors early.

### Integration Tests
Integration tests check whether multiple parts of the system work together correctly.

Examples:
- Testing that your Python code saves data correctly to a database
- Testing that a service function calls another module and handles the returned value properly

These are useful when:
- Your code depends on databases, files, APIs, or multiple modules
- You want to verify that connections between parts are correct

### Functional Tests
Functional tests check that a feature behaves correctly from the user's point of view.

Examples:
- A login function accepts correct credentials and rejects invalid ones
- A shopping cart total updates after adding an item

Functional tests focus on behavior, not internal implementation.

### End-to-End Tests
End-to-end tests simulate a full real-world workflow across the entire application.

Examples:
- A user signs up, logs in, places an order, and receives a confirmation
- A user fills out a form in a web app and sees the saved result on the dashboard

These tests are powerful, but they are usually:
- Slower
- Harder to maintain
- More dependent on the environment

### Smoke Tests
Smoke tests are quick checks to confirm the most important parts of the application still work after a change or deployment.

Examples:
- The app starts successfully
- The home page loads
- The main API endpoint returns a successful response

Think of smoke tests as "basic health checks."

### Regression Tests
Regression tests make sure old bugs do not come back after new code is added.

Example:
- If a bug once caused `"Madam"` to fail as a palindrome, add a test for it so future changes do not reintroduce that bug.

### A Simple Mental Model
- **Unit:** Does this small piece work?
- **Integration:** Do these parts work together?
- **Functional:** Does this feature behave correctly?
- **End-to-end:** Does the whole workflow succeed?
- **Smoke:** Does the app still basically work?
- **Regression:** Did an old bug come back?

In real projects, strong testing usually combines several of these levels.

---

## 6. Test Naming Conventions
- Name files like `test_*.py` or `*_test.py` so pytest can discover them.
- Name test functions like `test_returns_false_for_non_palindrome()`.
- Use names that describe behavior, not implementation details.

Good examples:
- `test_withdraw_reduces_balance`
- `test_is_palindrome_ignores_spaces_and_case`
- `test_divide_raises_error_for_zero`

---

## 7. Pytest Fixtures in Plain English
A fixture is reusable setup code. Instead of creating the same sample data in every test, you define it once and ask for it by name.

Example:

```python
import pytest

@pytest.fixture
def user_record():
    return {"name": "Ada", "active": True}

def test_user_is_active(user_record):
    assert user_record["active"] is True
```

Fixtures help keep tests short and focused.

---

## 8. Parametrized Tests
Parametrization lets one test function run with many inputs.

```python
import pytest

@pytest.mark.parametrize("value, expected", [
    ("level", True),
    ("python", False),
    ("Madam", True),
])
def test_palindrome_cases(value, expected):
    assert is_palindrome(value) == expected
```

This is especially useful when you want to test edge cases like:
- Empty strings
- Mixed capitalization
- Numbers
- Punctuation

---

## 9. Choosing the Right Test Type
Here is a practical rule of thumb:

- Use **unit tests** for core logic and utility functions.
- Use **integration tests** when a feature depends on databases, files, or external services.
- Use **functional tests** for business rules and user-facing features.
- Use **end-to-end tests** for critical application flows.
- Use **smoke tests** after deployment or major merges.
- Use **regression tests** whenever you fix a bug.

A healthy test suite usually has:
- Many unit tests
- Fewer integration tests
- Even fewer end-to-end tests

This keeps the suite fast while still giving broad confidence.

---

## 10. Best Practices
- Keep each test focused on one behavior.
- Prefer simple data over complicated test setup.
- Test both valid and invalid inputs.
- Include edge cases such as empty values or zero.
- Avoid writing tests that depend on execution order.
- If a bug is fixed, add a test for it.

---

## 11. Exercises
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

3. **Extended Pytest Challenges:**
   - Add a function that counts vowels in a string.
   - Test punctuation, uppercase input, and empty strings.
   - Add a function that divides two numbers and raises an error for division by zero.
   - Use `pytest.raises(...)` to verify exceptions.
   - Create at least one fixture for reusable sample text.

---

## 12. Suggested Practice Flow
1. Read the function docstring.
2. Write one simple passing test.
3. Add edge-case tests.
4. Add invalid-input or exception tests.
5. Refactor duplicated test setup into fixtures or parametrized tests.

By the time you finish, your tests should explain both what the code does and what it should never do.
