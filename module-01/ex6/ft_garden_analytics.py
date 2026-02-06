#!/usr/bin/env python3
"""Garden analytics demo with nested helpers and class hierarchy."""


class Plant:  # pylint: disable=too-few-public-methods
    """Base plant with common attributes."""

    def __init__(self, name: str, height: int) -> None:
        """Create a plant with a name and height."""
        self.name = name
        self.height = height

    def grow(self, amount: int = 1) -> int:
        """Increase plant height and report the growth."""
        self.height += amount
        print(f"{self.name} grew {amount}cm")
        return amount

    def describe(self) -> str:
        """Return a simple description for the plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Plant subtype that can bloom."""

    def __init__(self, name: str, height: int, flower_color: str) -> None:
        """Create a flowering plant specifying its bloom color."""
        super().__init__(name, height)
        self.flower_color = flower_color

    def describe(self) -> str:
        """Return a detailed description including bloom color and status."""
        detail = f"{self.name}: {self.height}cm, {self.flower_color} flowers"
        return f"{detail} (blooming)"


class PrizeFlower(FloweringPlant):
    """Flowering plant with prize points."""

    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str,
        prize_points: int,
    ) -> None:
        """Create a prize flower with color and prize points."""
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def describe(self) -> str:
        """Return a detailed description including prize points."""
        detail = super().describe().rstrip(" (blooming)")
        return f"{detail} (blooming), Prize points: {self.prize_points}"


class Garden:
    """Represents a single garden with plants and growth tracking."""

    def __init__(self, owner: str) -> None:
        """Initialize an empty garden for the given owner."""
        self.owner = owner
        self.plants: list[Plant] = []
        self._growth_total = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        """Help all plants grow and track total growth."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self._growth_total += plant.grow()

    def stats(self) -> "GardenManager.GardenStats":
        """Return a stats helper bound to this garden."""
        return GardenManager.GardenStats(self)

    def report(self) -> str:
        """Generate a human-readable garden report."""
        lines = ["Plants in garden:"]
        for plant in self.plants:
            prefix = "- " + plant.describe()
            lines.append(prefix)
        garden_stats = self.stats()
        counts = garden_stats.plant_type_counts()
        lines.append(
            f"Plants added: {garden_stats.plants_added()}, "
            f"Total growth: {garden_stats.total_growth()}cm"
        )
        lines.append(
            "Plant types: "
            f"{counts['regular']} regular, "
            f"{counts['flowering']} flowering, "
            f"{counts['prize']} prize flowers"
        )
        return "\n".join(lines)


class GardenManager:
    """Manages multiple gardens and provides analytics."""

    total_gardens = 0

    class GardenStats:
        """Nested helper for statistics calculations."""

        def __init__(self, garden: Garden) -> None:
            """Bind this stats helper to a garden instance."""
            self.garden = garden

        def plants_added(self) -> int:
            """Return how many plants were added to the garden."""
            return len(self.garden.plants)

        def total_growth(self) -> int:
            """Return accumulated growth tracked for this garden."""
            return self.garden._growth_total  # pylint: disable=protected-access

        def plant_type_counts(self) -> dict[str, int]:
            """Count regular, flowering, and prize plants in the garden."""
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return {"regular": regular, "flowering": flowering, "prize": prize}

        def garden_score(self) -> int:
            """Compute a score using plant heights and prize points."""
            height_sum = sum(plant.height for plant in self.garden.plants)
            prize_points = sum(
                getattr(plant, "prize_points", 0) for plant in self.garden.plants
            )
            return height_sum + prize_points * 4

    def __init__(self) -> None:
        """Create an empty manager ready to register gardens."""
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden) -> None:
        """Register a garden and update the managed count."""
        self.gardens.append(garden)
        GardenManager.total_gardens = len(self.gardens)

    def get_garden(self, owner: str) -> Garden:
        """Retrieve a garden by owner name or raise an error."""
        for garden in self.gardens:
            if garden.owner == owner:
                return garden
        raise ValueError(f"Garden for {owner} not found")

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Build a demo garden network with sample data."""
        manager = cls()

        alice_garden = Garden("Alice")
        alice_garden.add_plant(Plant("Oak Tree", 100))
        alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
        alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

        bob_garden = Garden("Bob")
        bob_garden.add_plant(Plant("Birch", 72))
        bob_garden.add_plant(FloweringPlant("Lily", 20, "white"))

        manager.add_garden(alice_garden)
        manager.add_garden(bob_garden)
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility validation that does not require instance data."""
        return height > 0

    def garden_scores(self) -> dict[str, int]:
        """Compute score per garden using nested stats helper."""
        scores: dict[str, int] = {}
        for garden in self.gardens:
            scores[garden.owner] = garden.stats().garden_score()
        return scores


def main() -> None:
    """Main function to demonstrate garden analytics system."""
    print("=== Garden Management System Demo ===")
    manager = GardenManager.create_garden_network()

    alice_garden = manager.get_garden("Alice")
    alice_garden.help_plants_grow()

    print("=== Alice's Garden Report ===")
    print(alice_garden.report())

    print(
        "Height validation test:",
        GardenManager.validate_height(alice_garden.plants[0].height)
    )

    scores = manager.garden_scores()
    print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
