#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 12:52:41 by marvin            #+#    #+#              #
#    Updated: 2026/01/26 12:52:41 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Plant factory for creating and managing multiple plant instances."""


class Plant:  # pylint: disable=too-few-public-methods
    """Represents a plant with a name, height (cm) and age (days)."""

    def __init__(self, name: str, height: float, age_day: int) -> None:
        """
        Initialize the plant with name, height and age.

        Args:
            name (str): The name of the plant.
            height (float): The height of the plant in cm.
            age_day (int): The age of the plant in days.
            
        """
        self.name = name
        self.height = height
        self.age_day = age_day

    def grow(self) -> None:
        """Increases the height of the plant by one cm."""
        self.height += 1

    def age(self) -> None:
        """Increases the age of the plant by one day."""
        self.age_day += 1

    def get_info(self) -> str:
        """
        Get the information about the plant.

        Returns:
            str: The information about the plant.
        """
        return(f"Created: {self.name} ({self.height}cm, {self.age_day} days)")           

if __name__ == "__main__":
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    garden = []
    print("=== Plant Factory Output ===")
    for plant in plants:
        garden.append(Plant(plant[0], plant[1], plant[2]))
    
    for i in garden:
        print(i.get_info())
    print(f"Total plants created: {len(garden)}")
