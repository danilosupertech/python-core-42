# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 11:22:34 by marvin            #+#    #+#              #
#    Updated: 2026/01/15 11:22:34 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
    """Calculate and print the total harvest from three days."""
    day1 = int(input("Enter harvest for day 1: "))
    day2 = int(input("Enter harvest for day 2: "))
    day3 = int(input("Enter harvest for day 3: "))
    total = day1 + day2 + day3
    print("Total harvest:", total)

#ft_harvest_total()
