from app.operations import addition, subtraction, multiplication, division

OPERATIONS = {
    "add": addition,
    "subtract": subtraction,
    "multiply": multiplication,
    "divide": division,
}

def calculate(operation: str, a: float, b: float) -> float:
    """Look up the operation and apply it. Raises ValueError for unknown ops or bad math."""
    if operation not in OPERATIONS:
        raise ValueError(f"Unknown operation: {operation}")
    return OPERATIONS[operation](a, b)
