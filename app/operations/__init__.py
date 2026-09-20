"""Core operations for the calculator application."""


def addition(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtraction(a: float, b: float) -> float:
    """Return the difference of a and b (a - b)."""
    return a - b


def multiplication(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def division(a: float, b: float) -> float:
    """Return the quotient of a and b (a / b).

    Raises:
        ValueError: If b is zero, since division by zero is undefined.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
