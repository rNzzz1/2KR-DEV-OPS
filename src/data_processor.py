"""Data processing and normalization utility module.

Contains helper functions to sanitize strings, filter records,
and perform statistical transformations on structured datasets.
"""

from typing import Any, Dict, List, Optional


def sanitize_string(value: str) -> str:
    """Strip whitespace and normalize casing of input string.

    Args:
        value: Input raw string.

    Returns:
        Cleaned lowercase string.
    """
    if not isinstance(value, str):
        raise TypeError("Input value must be a string.")
    return value.strip().lower()


def filter_active_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter records that have an active status.

    Args:
        records: List of dictionary records containing 'is_active' flag.

    Returns:
        Subset of records with is_active set to True.
    """
    return [record for record in records if record.get("is_active") is True]


def extract_field_values(
    records: List[Dict[str, Any]], field_name: str
) -> List[Any]:
    """Extract all values for a given key from list of dictionaries.

    Args:
        records: Collection of records.
        field_name: Target attribute key.

    Returns:
        List containing non-None values for the specified attribute.
    """
    results: List[Any] = []
    for item in records:
        val: Optional[Any] = item.get(field_name)
        if val is not None:
            results.append(val)
    return results
