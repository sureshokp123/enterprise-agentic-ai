# Python Development Guidelines

## Coding Standards

All Python code should follow PEP 8 coding standards.

Use meaningful variable and function names.

Functions should perform a single responsibility.

---

## Project Structure

Projects should follow a modular structure.

Separate:

- API
- Services
- Models
- Database
- Utilities
- Configuration

---

## Error Handling

Always handle expected exceptions.

Avoid using generic Exception unless absolutely necessary.

Use logging instead of print statements in production.

---

## Type Hints

Use Python type hints for function parameters and return values.

Example:

def add(a: int, b: int) -> int

---

## Virtual Environment

Always create a virtual environment.

Example:

python -m venv venv

---

## Dependency Management

Maintain dependencies using requirements.txt.

Install packages using:

pip install -r requirements.txt

---

## Logging

Use Python logging module.

Log levels:

DEBUG

INFO

WARNING

ERROR

CRITICAL

---

## Code Reviews

Every Pull Request should be reviewed before merging.

---

## Unit Testing

Write unit tests using pytest.

Maintain minimum 80% code coverage.