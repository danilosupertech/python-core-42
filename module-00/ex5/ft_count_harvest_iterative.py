# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 13:25:57 by danicort          #+#    #+#              #
#    Updated: 2026/01/15 13:25:57 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
    """Count down harvest days iteratively."""
    days = int(input("Enter harvest for day: "))

    for i in range(1,(days+1)):
        print("Day ", i)
    print("Harvest time!")

#ft_count_harvest_iterative()
