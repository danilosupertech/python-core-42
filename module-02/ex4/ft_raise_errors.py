#!/usr/bin/env python3
"""Raising custom errors for plant health validation."""


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int,
) -> str:
    """
    Check if a plant has healthy conditions.

    Args:
        plant_name: Name of the plant
        water_level: Water level (1-10)
        sunlight_hours: Daily sunlight (2-12)

    Returns:
        str: Success message if healthy

    Raises:
        ValueError: If any parameter is invalid
    """
    if not plant_name or plant_name.strip() == "":
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        raise ValueError(f"Water level {water_level} is invalid (must be 1-10)")

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is invalid (must be 2-12)")

    return f"Plant '{plant_name}' is healthy!"


def test_good_values() -> None:
    """Test with valid values."""
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")


def test_bad_plant_name() -> None:
    """Test with empty plant name."""
    print("Testing empty plant name...")
    try:
        result = check_plant_health("", 5, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")


def test_bad_water_level() -> None:
    """Test with invalid water level."""
    print("Testing bad water level...")
    try:
        result = check_plant_health("tomato", 15, 8)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")


def test_bad_sunlight_hours() -> None:
    """Test with invalid sunlight hours."""
    print("Testing bad sunlight hours...")
    try:
        result = check_plant_health("tomato", 5, 0)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")


def main() -> None:
    """Run all plant health tests."""
    print("=== Garden Plant Health Checker ===")
    test_good_values()
    test_bad_plant_name()
    test_bad_water_level()
    test_bad_sunlight_hours()
    print("All error raising tests completed!")


if __name__ == "__main__":
    main()
