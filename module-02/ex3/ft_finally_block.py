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
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    """Test watering system with various scenarios."""
    print("=== Garden Watering System ===\n")
    # Test normal watering with a good plant list
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!\n")

    # Test watering with a bad plant list (causes an error)
    print("Testing with error...")
    plants_with_error = ["tomato", None, "carrots"]
    water_plants(plants_with_error)
    print("Cleanup always happens, even with errors!")


def main() -> None:
    """Run watering system tests."""
    test_watering_system()


if __name__ == "__main__":
    main()
