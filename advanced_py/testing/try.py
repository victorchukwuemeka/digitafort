import pytest

#divide
def divide(a,e):
    if e == 0 :
        raise ValueError("Cannot be divided by Zero")
    return a/e

def test_divide():
    assert divide(10,2) == 5

def test_divide():
    assert divide(20,5) == 4





@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (20, 5, 4),
    (0, 5, 0),
])
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected
