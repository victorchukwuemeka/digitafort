import pytest

# feature where fixture -> reusable easily call the name to get the  functions

"""
@pytest.fixture 
def order():
    return []


@pytest.fixture
def outer(order, inner):
    order.append("outer")

"""



"""
student = { "name": "Holly", "latest_test_score": "B", "class": "Sixth Grade" }

def student(pupil):
	print("Name: " + pupil["name"])
	print("Latest Test Score: " + pupil["latest_test_score"])
	print("Class: " + pupil["class"])


#student(student)





def show_student_details(pupil):
	print("Name: " + pupil["name"])
	print("Latest Test Score: " + pupil["latest_test_score"])
	print("Class: " + pupil["class"])

#show_student_details(student)
"""



"""
def func(x):
    return x + 2

def test_answer():
    assert func(3) == 5

test_answer() 

"""

#divide
"""
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
"""
