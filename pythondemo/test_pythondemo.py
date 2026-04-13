import pytest
import pythondemo

# ✅ Correct output test
def test_add():
    assert pythondemo.add(2, 3) == 5

# ❌ Failing test (for understanding)
def test_multiply_fail():
    assert pythondemo.multiply(4, 3) == 11

# ✅ Exception test
def test_divide_by_zero():
    with pytest.raises(ValueError):
        pythondemo.divide(10, 0)

# ✅ Logical test
def test_is_even():
    assert pythondemo.is_even(4) is True
    assert pythondemo.is_even(5) is False


# ✅ Task 1: Factorial test cases

def test_factorial_basic():
    assert pythondemo.factorial(5) == 120
    assert pythondemo.factorial(0) == 1

# ✅ Negative number test (Task 2)
def test_factorial_negative():
    with pytest.raises(ValueError):
        pythondemo.factorial(-3)

# ✅ Large input test (Task 2)
def test_factorial_large():
    assert pythondemo.factorial(10) == 3628800


# ✅ Parametrized test
@pytest.mark.parametrize("a,b,result", [
    (1,2,3),
    (2,2,4),
    (5,5,11)  # failing case
])
def test_add_param(a,b,result):
    assert pythondemo.add(a,b) == result