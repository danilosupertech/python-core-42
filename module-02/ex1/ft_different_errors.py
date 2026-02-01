#!/usr/bin/env python3
"""Demonstration of different error types in garden operations."""


def garden_operations() -> None:
    """Demonstrate different types of errors that can occur."""
    print("=== Garden Error Types Demo ===")

    # ValueError
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    # ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    # FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r", encoding="utf-8") as file:
            file.read()
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: No such file '{error.filename}'")

    # KeyError
    print("Testing KeyError...")
    try:
        plants = {"tomato": 5, "lettuce": 3}
        _ = plants["missing_plant"]
    except KeyError as error:
        print(f"Caught KeyError: {error}")

    # Multiple errors together
    print("Testing multiple errors together...")
    try:
        int("not_a_number")
    except (ValueError, TypeError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
