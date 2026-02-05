"""Deck management system."""
from __future__ import annotations

import random
from typing import Dict, List

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for idx, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(idx)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
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
