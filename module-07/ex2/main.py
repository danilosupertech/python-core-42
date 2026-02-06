"""Demonstration script for Exercise 2: Ability System."""
from ex2.EliteCard import EliteCard


def demo() -> None:
    """Demonstrate the ability system with an elite card."""
    print("=== DataDeck Ability System ===")
    elite = EliteCard("Arcane Warrior", 4, "Epic", attack=5, health=8, mana_pool=3)

    print("EliteCard capabilities:")
    print("- Card:", ["play", "get_card_info", "is_playable"])
    print("- Combatable:", ["attack", "defend", "get_combat_stats"])
    print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])

    print(f"\nPlaying {elite.name} (Elite Card):")
    print(elite.play({}))

    print("\nCombat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(5))

    print("\nMagic phase:")
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", elite.channel_mana(3))

    print("Multiple interface implementation successful!")


def main() -> None:
    """Main entry point."""
    demo()


if __name__ == "__main__":
    main()
