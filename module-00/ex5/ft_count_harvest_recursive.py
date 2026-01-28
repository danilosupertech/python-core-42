# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 13:26:10 by danicort          #+#    #+#              #
#    Updated: 2026/01/15 13:26:10 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    n = int(input("Enter number of days: "))

    def recursive_harvest(day: int):
        if day <= 0:
            return
        recursive_harvest(day - 1)
        print("Day", day)

    recursive_harvest(n)
    print("Harvest time!")
#ft_count_harvest_recursive()
