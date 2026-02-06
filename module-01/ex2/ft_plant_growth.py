#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 10:35:36 by marvin            #+#    #+#              #
#    Updated: 2026/01/26 10:35:40 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """Represents a plant in the garden with its biological characteristics."""

    def __init__(self, name: str, height: float, age_days: int):
        """
        Initialize the plant with name, height and age.

        Args:
            name (str): The name of the plant.
            height (float): The height of the plant in cm.
            age_days (int): The age of the plant in days.
            
        """
        self.name = name
        self.height = height
        self.age_day = age_days

    def grow(self) -> None:
        """Increases the height of the plant by one cm."""
        self.height += 1

    def age(self) -> None:
        """Increases the age of the plant by one day."""
        self.age_day += 1

    def get_info(self) -> str:
        """Return information of the plant"""
        return f"{self.name}: {self.height}cm, {self.age_day} days old"


def main() -> None:
    """Main function to demonstrate plant growth simulation."""
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())
    start_height = rose.height

    for _ in range(6):
        rose.grow()
        rose.age()

    print("=== Day 7 ===")
    print(rose.get_info())

    weekly_growth = rose.height - start_height
    print(f"Growth this week: +{weekly_growth}cm")


if __name__ == "__main__":
    main()
