from app.calculator import calculate

def get_number(prompt: str) -> float:
    """Prompt the user for a number, re-prompting on invalid input."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print(f"Invalid number: '{value}'. Please enter a numeric value.")

def repl():
    print("Welcome to the Calculator REPL!")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'exit': ").strip().lower()

        if operation == "exit":
            print("Goodbye!")
            break

        if operation not in ("add", "subtract", "multiply", "divide"):
            print(f"Unknown operation: '{operation}'. Please try again.\n")
            continue

        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        try:
            result = calculate(operation, a, b)
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    repl()
