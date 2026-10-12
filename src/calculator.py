"""Mathematical calculator and statistical operations module.

Provides basic arithmetic and summary calculation utilities
with input validation and error handling.
"""

from typing import Sequence, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the arithmetic sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the arithmetic difference between two numbers."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the arithmetic product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return the quotient of division a by b.

    Raises:
        ZeroDivisionError: If divisor b is equal to zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculate_mean(values: Sequence[Number]) -> float:
    """Compute the arithmetic mean of a sequence of numbers.

    Raises:
        ValueError: If sequence is empty.
    """
    if not values:
        raise ValueError("Values sequence cannot be empty.")
    return float(sum(values) / len(values))
