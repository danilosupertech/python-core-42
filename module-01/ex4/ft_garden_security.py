#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/26 15:48:50 by marvin            #+#    #+#              #
#    Updated: 2026/01/26 15:48:50 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:  # pylint: disable=too-few-public-methods
    """Represents a secure plant with validated height and age."""

    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self._height = 0
        self._age_days = 0

        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: int) -> None:
        """Set height if valid."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age_days: int) -> None:
        """Set age if valid."""
        if age_days < 0:
            print(
                f"Invalid operation attempted: age {age_days} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days [OK]")

    def get_height(self) -> int:
        """Return the secure height."""
        return self._height

    def get_age(self) -> int:
        """Return the secure age."""
        return self._age_days

    def get_info(self) -> str:
        """Return information of the plant."""
        return f"{self.name} ({self._height}cm, {self._age_days} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(f"Current plant: {plant.get_info()}")
