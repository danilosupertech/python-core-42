# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 11:45:21 by marvin            #+#    #+#              #
#    Updated: 2026/01/15 11:45:21 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_plant_age() -> None:
    """Check if a plant is ready to harvest based on its age in days."""
    days = int(input("Enter plant age in days: "))

    if days >= 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

#ft_plant_age()
