"""Simple calculator program supporting add, subtract, multiply, divide."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Perform basic arithmetic operations on two numbers.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    parser.add_argument("--operation", choices=["add", "subtract", "multiply", "divide"], 
                        default="add", help="Operation to perform")

    args = parser.parse_args()
    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    result = ops[args.operation](args.a, args.b)
    print(result)
