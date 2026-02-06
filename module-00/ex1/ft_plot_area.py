# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 11:20:18 by marvin            #+#    #+#              #
#    Updated: 2026/01/15 11:20:18 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
    """Calculate and print the area of a plot based on user input."""
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Area:", area)

#ft_plot_area()
