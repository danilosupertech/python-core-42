#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 15:49:18 by danicort          #+#    #+#              #
#    Updated: 2026/01/26 15:49:18 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:  # pylint: disable=too-few-public-methods
    """Base class with common plant features: name, height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, height and age."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Specialized plant type: Flower."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize the flower with name, height, age and color."""
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        """Return information about the flower."""
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

    def bloom(self) -> None:
        """Simulate the blooming of the flower."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Specialized plant type: Tree."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        """Initialize the tree with name, height, age and trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        """Return information about the tree."""
        return (
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self) -> None:
        """Simulate the tree providing shade."""
        shade = self.trunk_diameter + 28
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """Specialized plant type: Vegetable."""

    def __init__(self, name: str, height: int, age: int, *harvest_data: str) -> None:
        """Initialize the vegetable with name, height, age, harvest season and nutritional value."""

        super().__init__(name, height, age)
        if len(harvest_data) != 2:
            raise ValueError("Vegetable requires harvest season and nutritional value")

        self.harvest_season, self.nutritional_value = harvest_data

    def get_info(self) -> str:
        """Return information about the vegetable."""
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season.lower()} harvest"
        )

    def show_nutrition(self) -> None:
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    ]
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 600, 2000, 40),
    ]
    vegetables = [
        Vegetable("Tomato", 80, 90, "Summer", "vitamin C"),
        Vegetable("Carrot", 15, 60, "Spring", "vitamin A"),
    ]

    print(flowers[0].get_info())
    flowers[0].bloom()

    print(trees[0].get_info())
    trees[0].produce_shade()

    print(vegetables[0].get_info())
    vegetables[0].show_nutrition()
