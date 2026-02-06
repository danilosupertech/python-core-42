"""Deck management system."""
from __future__ import annotations

import random
from typing import Dict, List

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    """Card deck management system for organizing and manipulating cards."""

    def __init__(self) -> None:
        """Initialize an empty deck."""
        """Initialize an empty deck."""
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck.

        Args:
            card: The Card instance to add.

        Raises:
            TypeError: If the object is not a Card instance.
        """
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name.

        Args:
            card_name: Name of the card to remove.

        Returns:
            True if card was found and removed, False otherwise.
        """
        for idx, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(idx)
                return True
        return False

    def shuffle(self) -> None:
        """Randomly shuffle the deck."""
        """Randomly shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw the top card from the deck.

        Returns:
            The top card from the deck.

        Raises:
            ValueError: If the deck is empty.
        """
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        """Calculate and return deck statistics.

        Returns:
            Dict with total cards, creature/spell/artifact counts, and average cost.
        """
        total = len(self.cards)
        creatures = sum(isinstance(c, CreatureCard) for c in self.cards)
        spells = sum(isinstance(c, SpellCard) for c in self.cards)
        artifacts = sum(isinstance(c, ArtifactCard) for c in self.cards)
        avg_cost = sum(c.cost for c in self.cards) / total if total else 0
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 2),
        }
