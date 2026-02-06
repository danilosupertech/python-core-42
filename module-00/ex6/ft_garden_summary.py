# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 13:36:18 by danicort          #+#    #+#              #
#    Updated: 2026/01/15 13:36:18 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary() -> None:
    """Display a summary of garden information."""
    name = input("Enter garden name: ")
    plant = int(input("Enter number of plants: "))

    print(f"Garden: {name}")
    print(f"Plants: {plant}")
    print("Status: Growing well!")

#ft_garden_summary()
