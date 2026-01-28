# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 11:45:28 by marvin            #+#    #+#              #
#    Updated: 2026/01/15 11:45:28 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    lwatering = int(input("Days since last watering: "))

    if lwatering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
#ft_water_reminder()
