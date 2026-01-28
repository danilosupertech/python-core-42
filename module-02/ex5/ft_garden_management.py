#!/usr/bin/env python3
"""Integrated garden management system with error handling."""


class GardenError(Exception):
    """Base exception for all garden-related errors."""




class PlantError(GardenError):
    """Exception for problems with plants."""




class WaterError(GardenError):
    """Exception for problems with watering."""




class GardenManager:
    """Manages plants with comprehensive error handling."""

    def __init__(self) -> None:
        """Initialize empty garden."""
        self.plants: dict[str, dict[str, int]] = {}
        self.water_supply = 100

    def add_plant(self, name: str, water_level: int, sunlight_hours: int) -> None:
        """
        Add a plant with validation.

        Args:
            name: Plant name
            water_level: Water requirement (1-10)
            sunlight_hours: Required sunlight (2-12)

        Raises:
            PlantError: If plant data is invalid
        """
        try:
            if not name or name.strip() == "":
                raise ValueError("Plant name cannot be empty!")
            if water_level < 1 or water_level > 10:
                raise ValueError(f"Water level {water_level} is invalid (must be 1-10)")
            if sunlight_hours < 2 or sunlight_hours > 12:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is invalid (must be 2-12)"
                )
            self.plants[name] = {
                "water_level": water_level,
                "sunlight_hours": sunlight_hours,
            }
            print(f"Added {name} successfully")
        except ValueError as error:
            print(f"Error adding plant: {error}")

    def water_all_plants(self) -> None:
        """Water all plants with cleanup guarantee."""
        try:
            print("Opening watering system")
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
                self.water_supply -= 5
        except Exception as error:
            print(f"Watering error: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> None:
        """
        Check health of a specific plant.

        Args:
            plant_name: Name of plant to check

        Raises:
            PlantError: If plant has issues
        """
        try:
            if plant_name not in self.plants:
                raise PlantError(f"Plant {plant_name} not found in garden!")

            plant = self.plants[plant_name]
            print(
                f"{plant_name}: healthy "
                f"(water: {plant['water_level']}, "
                f"sun: {plant['sunlight_hours']})"
            )
        except PlantError as error:
            print(f"Error checking {plant_name}: {error}")

    def check_water_supply(self) -> None:
        """
        Check available water.

        Raises:
            WaterError: If water is insufficient
        """
        try:
            if self.water_supply < 20:
                raise WaterError("Not enough water in tank")
            print(f"Water supply: {self.water_supply}L - OK")
        except WaterError as error:
            print(f"Caught GardenError: {error}")
            print("System recovered and continuing...")


def main() -> None:
    """Demonstrate integrated garden management."""
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 3, 6)
    manager.add_plant("", 4, 7)

    print("\nWatering plants...")
    manager.water_all_plants()

    print("\nChecking plant health...")
    manager.check_plant_health("tomato")
    manager.check_plant_health("lettuce")
    manager.check_plant_health("basil")

    print("\nTesting error recovery...")
    manager.check_water_supply()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
