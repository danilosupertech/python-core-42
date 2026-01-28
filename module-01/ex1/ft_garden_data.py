#!/usr/bin/env python3
# **************************************************************************** #                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 12:50:34 by marvin            #+#    #+#              #
#    Updated: 2026/01/26 12:50:34 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:  # pylint: disable=too-few-public-methods
    """Represents a plant in the garden with its biological characteristics."""

    def __init__(self, name:str, height:float, age:int) -> None:
        """
        Initialize the plant with name, height and age.

        Args:
            name (str): The name of the plant.
            height (float): The height of the plant in cm.
            age (int): The age of the plant in days.
            
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    garden = [rose, sunflower, cactus]
    print("=== Garden Plant Registry ===")
    for i in range(len(garden)):
        print(f"{garden[i].name}: {garden[i].height}cm, {garden[i].age} days old")
