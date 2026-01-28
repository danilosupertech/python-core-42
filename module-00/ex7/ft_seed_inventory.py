# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 22:13:09 by danicort          #+#    #+#              #
#    Updated: 2026/01/16 22:13:09 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    print(f'{seed_type.capitalize()} seeds: {quantity} packets "{unit}"')

# ft_seed_inventory("tomato", 15, "packets")
# ft_seed_inventory("carrot", 8, "grams")
# ft_seed_inventory("lettuce", 12, "area")
