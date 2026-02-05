"""Demonstration script for Exercise 1: Deck Builder."""
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def demo() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", attack=7, health=5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", effect_type="damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Uncommon", durability=3, effect="+1 mana per turn"))

    deck.shuffle()

    print("Deck stats:", deck.get_deck_stats())
    print("Drawing and playing cards:")

    while True:
        try:
            card = deck.draw_card()
        except ValueError:
            break
        card_info = card.get_card_info()
        print(f"Drew: {card.name} ({card_info.get('type', 'Card')})")
        print("Play result:", card.play({}))

    print("Polymorphism in action: Same interface, different card behaviors!")


def main() -> None:
    demo()


if __name__ == "__main__":
    main()
