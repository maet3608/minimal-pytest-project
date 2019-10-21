import pytest
import mymath.calculator

from mymath.calculator import add, div, filesum, fileconcat, approx_eq


# Simple tests
# ----------------------------------------------------
def test_add():
    assert add(1, 2) == 3
    
def test_div():
    assert div(4, 2) == 2
    assert div(0, 2) == 0

    
# Catching exceptions
# ------------------------------------------------------------------------------
def test_div_by_zero():
    with pytest.raises(ValueError) as ex:
        div(1, 0)
    assert str(ex.value) == 'Cannot divide by zero!'


# Tests organized in class
# ------------------------------------------------------------------------------
class TestCalculator:

    def test_add(self):
        assert add(1, 2) == 3

    def test_add_zero(self):
        assert add(0, 0) == 0
        assert add(1, 0) == 1
        assert add(0, 2) == 2

    def test_div(self):
        assert div(4, 2) == 2


# Fixtures
# ------------------------------------------------------------------------------
@pytest.fixture(scope="function")
def numbers_file():
    f = open("tests/data/numbers.txt")

    def fin():
        f.close()
    return f


def test_filesum(numbers_file):
    assert filesum(numbers_file) == 6


def test_fileconcat(numbers_file):
    assert fileconcat(numbers_file) == 123


# Monkey patching, Mocking
# ------------------------------------------------------------------------------
def test_approx_eq(monkeypatch):
    def mock_eps(machine):
        return 2
        
    assert approx_eq(1, 1)
    #monkeypatch.setattr(mymath.calculator, 'eps', mock_eps)
    monkeypatch.setattr('mymath.calculator.eps', mock_eps)
    assert approx_eq(1, 2)
