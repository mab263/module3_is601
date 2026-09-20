import pytest
from app.operations import addition, subtraction, multiplication, division


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (-5, -5, -10),
])
def test_addition(a, b, expected):
    assert addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (5, 3, 2),
    (0, 5, -5),
    (-1, -1, 0),
])
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (2, 3, 6),
    (0, 5, 0),
    (-2, 3, -6),
])
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (10, 2, 5),
    (9, 3, 3),
    (-6, 2, -3),
])
def test_division(a, b, expected):
    assert division(a, b) == expected


def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)
