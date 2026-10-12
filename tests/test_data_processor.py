"""Unit tests for data processor module."""

import unittest
from src.data_processor import (
    sanitize_string,
    filter_active_records,
    extract_field_values,
)


class TestDataProcessor(unittest.TestCase):
    """Test suite for data processor utilities."""

    def test_sanitize_string(self) -> None:
        """Test string normalization and whitespace removal."""
        self.assertEqual(sanitize_string("  Hello World  "), "hello world")
        with self.assertRaises(TypeError):
            sanitize_string(123)  # type: ignore

    def test_filter_active_records(self) -> None:
        """Test filtering active records from list."""
        data = [
            {"id": 1, "is_active": True},
            {"id": 2, "is_active": False},
            {"id": 3, "is_active": True},
        ]
        active = filter_active_records(data)
        self.assertEqual(len(active), 2)
        self.assertEqual([item["id"] for item in active], [1, 3])

    def test_extract_field_values(self) -> None:
        """Test extraction of existing field values."""
        records = [
            {"name": "Alice", "score": 95},
            {"name": "Bob"},
            {"name": "Charlie", "score": 88},
        ]
        scores = extract_field_values(records, "score")
        self.assertEqual(scores, [95, 88])


if __name__ == "__main__":
    unittest.main()
