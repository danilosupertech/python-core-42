#!/usr/bin/env python3
"""Achievement Hunter - Track achievements using sets."""


def main() -> None:
    """Demonstrate achievement tracking with sets."""
    alice_achievements: set[str] = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }
    bob_achievements: set[str] = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }
    charlie_achievements: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")

    print("\n=== Achievement Analytics ===")

    all_achievements = (
        alice_achievements | bob_achievements | charlie_achievements
    )
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice_achievements & bob_achievements & charlie_achievements
    print(f"Common to all players: {common_all}")

    rare_achievements = {
        ach
        for ach in all_achievements
        if (
            sum(
                [
                    ach in alice_achievements,
                    ach in bob_achievements,
                    ach in charlie_achievements,
                ]
            )
            == 1
        )
    }
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_bob_common = alice_achievements & bob_achievements
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice_achievements - bob_achievements - charlie_achievements
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob_achievements - alice_achievements - charlie_achievements
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
