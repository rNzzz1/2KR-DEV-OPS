"""Unit tests for calculator and statistical operations module."""

import unittest
from src.calculator import add, subtract, multiply, divide, calculate_mean


class TestCalculator(unittest.TestCase):
    """Test suite for calculator functions."""

    def test_add(self) -> None:
        """Test addition of numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self) -> None:
        """Test subtraction of numbers."""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self) -> None:
        """Test multiplication of numbers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self) -> None:
        """Test division of numbers."""
        self.assertEqual(divide(10, 2), 5.0)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_calculate_mean(self) -> None:
        """Test mean calculation."""
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)
        with self.assertRaises(ValueError):
            calculate_mean([])


if __name__ == '__main__':
    unittest.main()
