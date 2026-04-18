import pytest

# EXERCISE 1: Implement the is_palindrome function
def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.
    Ignores spaces and case.
    """
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

# EXERCISE 2: Implement a helper that counts vowels in a string
def count_vowels(text: str) -> int:
    """
    Counts vowels in a string.
    Ignores case and skips non-letter characters.
    """
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


# EXERCISE 3: Implement a divide helper that raises an error for zero division
def safe_divide(a: float, b: float) -> float:
    """
    Divides two numbers and raises a ValueError for division by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# EXERCISE 4: Write tests for is_palindrome using pytest
def test_simple_palindrome():
    assert is_palindrome("racecar") is True


def test_mixed_case_palindrome():
    assert is_palindrome("Madam") is True


def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_palindrome_ignores_punctuation():
    assert is_palindrome("No lemon, no melon!") is True


def test_non_palindrome():
    assert is_palindrome("hello") is False


# EXERCISE 5: Use pytest.mark.parametrize for multiple palindrome cases
@pytest.mark.parametrize("input_str, expected", [
    ("racecar", True),
    ("Madam", True),
    ("A man a plan a canal Panama", True),
    ("No lemon, no melon!", True),
    ("hello", False),
    ("12321", True),
    ("", True),  # Empty string is technically a palindrome
])
def test_is_palindrome_parametrized(input_str, expected):
    assert is_palindrome(input_str) == expected


# EXERCISE 6: Test the vowel counter
@pytest.mark.parametrize("text, expected", [
    ("apple", 2),
    ("PYTHON", 1),
    ("Why?", 0),
    ("Aeiou", 5),
    ("", 0),
    ("Testing, one two three.", 7),
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


# EXERCISE 7: (Advanced) Using Fixtures
@pytest.fixture
def sample_data():
    return "No 'x' in Nixon"


@pytest.fixture
def number_pair():
    return (12, 3)


def test_is_palindrome_with_fixture(sample_data):
    assert is_palindrome(sample_data) is True


# EXERCISE 8: Test safe_divide with fixtures and exception handling
def test_safe_divide_with_fixture(number_pair):
    numerator, denominator = number_pair
    assert safe_divide(numerator, denominator) == 4


def test_safe_divide_returns_float():
    assert safe_divide(5, 2) == 2.5


def test_safe_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        safe_divide(10, 0)


# To run these tests, execute `pytest pytest_exercises.py` in your terminal.
