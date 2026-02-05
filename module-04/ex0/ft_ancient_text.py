#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/04 00:00:00 by danicort          #+#    #+#              #
#    Updated: 2026/02/04 00:00:00 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Ancient Text Recovery - Retrieve data from storage vaults."""


def recover_ancient_text() -> None:
    """Recover and display ancient data fragment from storage vault."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    vault = None
    try:
        vault = open(filename, "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        content = vault.read()
        print(content)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if vault is not None:
            vault.close()
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    recover_ancient_text()
