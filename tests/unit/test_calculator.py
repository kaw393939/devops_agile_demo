import pytest
from calculator import add, subtract, multiply, divide

# Unit Tests for add
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

# Unit Tests for subtract
def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-5, -3) == -2

# Unit Tests for multiply
def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, 3) == -6

# Unit Tests for divide
def test_divide_positive():
    assert divide(6, 3) == 2

def test_divide_negative():
    assert divide(-6, 3) == -2

# An examlple of a negative test
def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(6, 0)
    assert "Cannot divide by zero!" in str(excinfo.value)
