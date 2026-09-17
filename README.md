# Writing Automated Tests for Python Applications

A compact, practical Python project that demonstrates how to write and run automated unit tests for utility functions using the standard library.

## Value proposition

This repository is a clean reference for:
- implementing small, reusable Python functions,
- validating behavior with automated tests, and
- catching regressions quickly via local test runs and CI.

## Features

- Arithmetic utilities: `add`, `subtract`, `multiply`, `divide`
- String utilities: `reverse_string`, `count_vowels`
- Parsing utility: `parse_int_list` for comma-separated integers
- Error handling coverage (`ValueError`, `TypeError`) in tests
- CI workflow for automated test execution on push and pull request

## Tech stack

- [Python 3](https://www.python.org/)
- [`unittest`](https://docs.python.org/3/library/unittest.html)
- [GitHub Actions](https://docs.github.com/actions)

## Project structure

- [`utils.py`](./utils.py) – utility functions under test
- [`test_utils.py`](./test_utils.py) – unit tests for `utils.py`
- [`.github/workflows/ci.yml`](./.github/workflows/ci.yml) – CI pipeline

## Prerequisites

- Python 3.9+ (3.10+ recommended)
- Git (optional, for cloning)

## Installation

```bash
git clone https://github.com/kumarimanjusrimohantycse2024-art/Writing-Automated-Tests-for-Python-Applications.git
cd Writing-Automated-Tests-for-Python-Applications
```

No external dependencies are required.

## Configuration

No environment variables or secret configuration are needed.

## Usage examples

Run a few functions directly:

```python
import utils

print(utils.add(2, 3))                  # 5
print(utils.reverse_string("hello"))    # "olleh"
print(utils.parse_int_list("1, 2, 3"))   # [1, 2, 3]
```

## Testing

Run the test suite:

```bash
python -m unittest -v
```

Expected result: all tests pass.

## Troubleshooting

- **`ModuleNotFoundError: No module named 'utils'`**
  - Run tests from the repository root directory.
- **`python: command not found`**
  - Use `python3 -m unittest -v` depending on your system.
- **Unexpected test failure**
  - Confirm you are using a supported Python version and that local edits are saved.

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Add/update tests for behavior changes
4. Run `python -m unittest -v`
5. Open a pull request with a clear summary

## License / status

- **License:** No license file is currently present in this repository.
- **Project status:** Active educational/demo project.
