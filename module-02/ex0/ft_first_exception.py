#!/usr/bin/env python3
"""Agricultural data validation pipeline for temperature sensors."""


def check_temperature(temp_str: str) -> int:
    """
    Validate and convert temperature string to integer.

    Args:
        temp_str: Temperature as string

    Returns:
        int: Temperature value if valid

    Raises:
        ValueError: If temperature is out of range
    """
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")

    return temperature


def test_temperature_input() -> None:
    """Demonstrate temperature validation with various inputs."""
    print("=== Garden Temperature Checker ===")

    test_cases = ["25", "abc", "100", "-50"]

    for test_value in test_cases:
        print(f"Testing temperature: {test_value}")
        try:
            temp = check_temperature(test_value)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as error:
            print(f"Error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
