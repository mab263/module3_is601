"""Calculator dispatcher that maps operation names to their corresponding functions."""

from app.operations import addition, subtraction, multiplication, division

OPERATIONS = {
    "add": addition,
    "subtract": subtraction,
    "multiply": multiplication,
    "divide": division,
}


def calculate(operation: str, a: float, b: float) -> float:
    """Look up and apply the given operation to a and b.

    Args:
        operation: The name of the operation ("add", "subtract", "multiply", "divide").
        a: The first number.
        b: The second number.

    Returns:
        The result of applying the operation to a and b.

    Raises:
        ValueError: If the operation is not recognized, or if a math error occurs
            (e.g. division by zero).
    """
    if operation not in OPERATIONS:
        raise ValueError(f"Unknown operation: {operation}")
    return OPERATIONS[operation](a, b)
