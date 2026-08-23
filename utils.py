"""
utils.py - Example utility module for Week 3 task.

Provides:
- Basic math operations
- String utilities
- Simple data parsing
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return a divided by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def reverse_string(s):
    """Return the reversed string."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

def count_vowels(s):
    """
    Count the number of vowels (a, e, i, o, u) in the string.
    Case-insensitive.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

def parse_int_list(csv_string):
    """
    Parse a comma-separated string of integers into a list of ints.
    Example: "1,2,3" -> [1, 2, 3]
    Raises ValueError if any item is not a valid integer.
    """
    if not isinstance(csv_string, str):
        raise TypeError("Input must be a string")

    parts = csv_string.split(",")
    result = []
    for p in parts:
        p = p.strip()
        if p == "":
            continue
        try:
            result.append(int(p))
        except ValueError:
            raise ValueError(f"Invalid integer value: {p}")
    return result