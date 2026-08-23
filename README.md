# Week 3 Task – Automated Tests for Python Applications

Author: Dell  
Date: 02-08-2026

---

## Overview

This Week 3 task implements a small Python module and a suite of automated tests to demonstrate test-driven development (TDD) principles, unit testing, and clear documentation.

The project contains:

- `utils.py` – Python module with reusable utility functions.
- `test_utils.py` – Automated tests using Python’s built-in `unittest` framework.
- `README.md` – This documentation, explaining the module, tests, and how to run them.

All tests pass successfully, as shown by:

```text
Ran 14 tests in X.XXXs

OK
```

---

## Module: `utils.py`

The `utils.py` module provides three groups of functions:

### 1. Math operations

- `add(a, b)`  
  Returns the sum of `a` and `b`.

- `subtract(a, b)`  
  Returns `a - b`.

- `multiply(a, b)`  
  Returns the product `a * b`.

- `divide(a, b)`  
  Returns `a / b`.  
  Raises `ValueError` if `b == 0` to prevent division by zero.

These functions are simple but are ideal for demonstrating unit tests with normal cases and error handling.

### 2. String utilities

- `reverse_string(s)`  
  Returns the reversed version of the string `s`.  
  Raises `TypeError` if `s` is not a string.

- `count_vowels(s)`  
  Counts the number of vowels (`a, e, i, o, u`) in the string `s`, case-insensitive.  
  Raises `TypeError` if `s` is not a string.

These functions allow testing normal behavior, edge cases (empty string, no vowels), and type errors.

### 3. Data parsing

- `parse_int_list(csv_string)`  
  Parses a comma-separated string of integers into a list of `int`.  
  Example: `"1,2,3"` → `[1, 2, 3]`  
  - Ignores extra spaces.
  - Skips empty entries (`,,`).
  - Raises `ValueError` if any item is not a valid integer.
  - Raises `TypeError` if the input is not a string.

This function is useful for testing error handling and parsing logic.

---

## Test Suite: `test_utils.py`

The tests are written using the `unittest` framework. They cover normal use, edge cases, and error conditions.

### Math function tests

- `test_add_basic`  
  Checks addition with positive and negative numbers.

- `test_subtract_basic`  
  Verifies subtraction producing positive and negative results.

- `test_multiply_basic`  
  Tests multiplication with positive and negative operands.

- `test_divide_basic`  
  Confirms correct division results, including floating-point values.

- `test_divide_by_zero_raises`  
  Ensures dividing by zero raises `ValueError`.

These tests ensure the math functions behave correctly and handle invalid operations safely.

### String function tests

- `test_reverse_string_basic`  
  Tests reversing normal strings and the empty string.

- `test_reverse_string_type_error`  
  Verifies that passing a non-string (e.g., integer) raises `TypeError`.

- `test_count_vowels_basic`  
  Checks vowel counting for lowercase and uppercase inputs and for strings with no vowels.

- `test_count_vowels_type_error`  
  Ensures non-string input raises `TypeError`.

These tests validate both functionality and proper type checking.

### Data parsing tests

- `test_parse_int_list_basic`  
  Tests parsing a simple comma-separated list like `"1,2,3"`.

- `test_parse_int_list_spaces`  
  Confirms that spaces around numbers are handled correctly: `" 1 ,  2 ,3 "` → `[1, 2, 3]`.

- `test_parse_int_list_empty_items`  
  Ensures empty entries (`,,`) are skipped, but valid numbers remain: `"1,,2,,,3"` → `[1, 2, 3]`.

- `test_parse_int_list_invalid_value`  
  Checks that invalid entries like `"two"` cause `ValueError`.

- `test_parse_int_list_type_error`  
  Ensures a non-string input (e.g., integer) raises `TypeError`.

These tests confirm that parsing works as expected and that errors are raised for invalid inputs.

---

## Development and Testing Methodology

### Approach

For this task, I used a **test-after development** style:

1. Implemented the core functions in `utils.py`.
2. Designed tests in `test_utils.py` to cover:
   - Normal and typical scenarios.
   - Edge cases (empty strings, extra commas, spaces).
   - Error conditions (invalid types, invalid values, division by zero).
3. Ran the tests using `python test_utils.py`.
4. Fixed any failing tests by correcting logic or adding error handling.
5. Refactored the code slightly for clarity and maintainability while ensuring all tests still passed.

This process demonstrates TDD principles: letting tests define the expected behavior and using them to confirm that changes do not break existing functionality.

---

## How to Run the Tests

1. Ensure Python 3 is installed (e.g., Python 3.13).
2. Open a terminal in the `week3_tests` folder (where `utils.py` and `test_utils.py` are located).
3. Run:

   ```bash
   python test_utils.py
   ```

4. You should see output similar to:

   ```text
   ..............
   ----------------------------------------------------------------------
   Ran 14 tests in 0.00Xs

   OK
   ```

This indicates that all 14 tests passed successfully.

---

## Refactoring and Maintainability

After all tests passed:

- The code in `utils.py` was checked for:
  - Clear function names.
  - Useful docstrings.
  - Consistent error handling (`ValueError`, `TypeError`).
- No further refactoring was needed because the code is already small and readable.
- The tests in `test_utils.py` are organized into classes:
  - `TestMathFunctions`
  - `TestStringFunctions`
  - `TestParseIntList`
  This structure makes it easy to add more tests in the future.

---


- `README.md` – Documentation explaining:
  - What the module does.
  - What each test
