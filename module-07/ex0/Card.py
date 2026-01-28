"""Card foundation definitions for DataDeck."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract base class defining the universal card contract."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if cost < 0:
            raise ValueError("cost must be non-negative")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """Play the card, returning the updated game state/result."""

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", "") or "Card",
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
