#!/usr/bin/env python3
"""Demonstration of finally blocks for resource cleanup."""


def water_plants(plant_list: list[str]) -> None:
    """
    Water plants with guaranteed cleanup.

    Args:
        plant_list: List of plant names to water
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_normal_watering() -> None:
    """Test watering with valid plant list."""
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")


def test_watering_with_error() -> None:
    """Test watering with invalid data."""
    print("\nTesting with error...")
    plants = ["tomato", None, "carrots"]
    water_plants(plants)
    print("Cleanup always happens, even with errors!")


def main() -> None:
    """Run watering system tests."""
    print("=== Garden Watering System ===")
    test_normal_watering()
    test_watering_with_error()


if __name__ == "__main__":
    main()
