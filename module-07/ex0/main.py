"""Demonstration script for Exercise 0: Card Foundation."""
from ex0.CreatureCard import CreatureCard


def demo() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", attack=7, health=5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    available_mana = 6
    print(f"\nPlaying {dragon.name} with {available_mana} mana available:")
    print(f"Playable: {dragon.is_playable(available_mana)}")
    print("Play result:", dragon.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", dragon.attack_target("Goblin Warrior"))

    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")
    print("Abstract pattern successfully demonstrated!")


def main() -> None:
    demo()


if __name__ == "__main__":
    main()
