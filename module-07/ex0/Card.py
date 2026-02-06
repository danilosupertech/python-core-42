"""Card foundation definitions for DataDeck."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract base class defining the universal card contract."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a card with name, cost, and rarity.
        
        Args:
            name: The card's name.
            cost: The mana cost to play this card (must be non-negative).
            rarity: The rarity level of the card.
            
        Raises:
            ValueError: If cost is negative.
        """
        if cost < 0:
            raise ValueError("cost must be non-negative")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """Play the card, returning the updated game state/result."""

    def get_card_info(self) -> Dict:
        """Get comprehensive information about this card.
        
        Returns:
            A dictionary containing the card's name, cost, rarity, and type.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", "") or "Card",
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if this card can be played with the available mana.
        
        Args:
            available_mana: The amount of mana currently available.
            
        Returns:
            True if the card's cost is less than or equal to available mana.
        """
        return available_mana >= self.cost
