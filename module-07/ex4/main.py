"""Demonstration script for Exercise 4: Tournament Platform."""
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def demo() -> None:
    """Demonstrate the tournament platform with ranking system."""
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", attack=7, health=5, rating=1200)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", attack=5, health=4, rating=1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print("Registering Tournament Cards...")
    for cid in [dragon_id, wizard_id]:
        card = platform.registry[cid]
        print(f"{card.name} (ID: {cid}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print("Match result:", result)

    print("Tournament Leaderboard:")
    for position, entry in enumerate(platform.get_leaderboard(), start=1):
        print(f"{position}. {entry['name']} - Rating: {entry['rating']} ({entry['wins']}-{entry['losses']})")

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print("=== Tournament Platform Successfully Deployed! ===")


def main() -> None:
    """Main entry point."""
    demo()


if __name__ == "__main__":
    main()
