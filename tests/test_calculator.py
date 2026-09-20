import pytest
from app.calculator import calculate


@pytest.mark.parametrize("operation, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 3, 2),
    ("multiply", 4, 3, 12),
    ("divide", 10, 2, 5),
])
def test_calculate_valid_operations(operation, a, b, expected):
    assert calculate(operation, a, b) == expected


def test_calculate_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation: modulo"):
        calculate("modulo", 5, 2)


def test_calculate_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        calculate("divide", 5, 0)
