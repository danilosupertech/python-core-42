#!/usr/bin/env python3
"""Custom exception classes for garden error handling."""


class GardenError(Exception):
    """Base exception for all garden-related errors."""


class PlantError(GardenError):
    """Exception for problems with plants."""


class WaterError(GardenError):
    """Exception for problems with watering."""


def test_plant_error() -> None:
    """Demonstrate PlantError handling."""
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def test_water_error() -> None:
    """Demonstrate WaterError handling."""
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_catch_all_garden_errors() -> None:
    """Demonstrate catching all GardenError subtypes."""
    print("Testing catching all garden errors...")
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]

    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def main() -> None:
    """Run all custom error tests."""
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    test_water_error()
    test_catch_all_garden_errors()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
