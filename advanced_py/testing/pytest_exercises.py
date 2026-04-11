import pytest

# EXERCISE 1: Implement the is_palindrome function
def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.
    Ignores spaces and case.
    """
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

# EXERCISE 2: Write tests for is_palindrome using pytest
def test_simple_palindrome():
    assert is_palindrome("racecar") is True

def test_mixed_case_palindrome():
    assert is_palindrome("Madam") is True

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_non_palindrome():
    assert is_palindrome("hello") is False

# EXERCISE 3: Use pytest.mark.parametrize for multiple test cases
@pytest.mark.parametrize("input_str, expected", [
    ("racecar", True),
    ("Madam", True),
    ("A man a plan a canal Panama", True),
    ("hello", False),
    ("12321", True),
    ("", True),  # Empty string is technically a palindrome
])
def test_is_palindrome_parametrized(input_str, expected):
    assert is_palindrome(input_str) == expected

# EXERCISE 4: (Advanced) Using Fixtures
@pytest.fixture
def sample_data():
    return "No 'x' in Nixon"

def test_is_palindrome_with_fixture(sample_data):
    assert is_palindrome(sample_data) is True

# To run these tests, simply execute `pytest pytest_exercises.py` in your terminal.
