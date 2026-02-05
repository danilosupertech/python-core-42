#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_archive_creation.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicort <danicort@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/04 00:00:00 by danicort          #+#    #+#              #
#    Updated: 2026/02/04 00:00:00 by danicort         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Archive Creation - Store discovered data in secure vault."""


def archive_discoveries() -> None:
    """Create archive file with discovered data entries."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    discoveries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    vault = None
    try:
        vault = open("new_discovery.txt", "w")
        for entry in discoveries:
            vault.write(entry + "\n")
            print(entry)
        print("Data inscription complete. Storage unit sealed.\n")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError:
        print("ERROR: Permission denied to write to vault")
    finally:
        if vault is not None:
            vault.close()


if __name__ == "__main__":
    archive_discoveries()
