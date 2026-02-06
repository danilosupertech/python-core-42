"""Abstract factory interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict

from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating themed card collections."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card.
        
        Args:
            name_or_power: Name or power level for the creature.
            
        Returns:
            A Card instance representing a creature.
        """
        ...

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card.
        
        Args:
            name_or_power: Name or power level for the spell.
            
        Returns:
            A Card instance representing a spell.
        """
        ...

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card.
        
        Args:
            name_or_power: Name or power level for the artifact.
            
        Returns:
            A Card instance representing an artifact.
        """
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        """Create a themed deck of cards.
        
        Args:
            size: Number of cards to include in the deck.
            
        Returns:
            Dictionary containing deck information and card list.
        """
        ...

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """Get the card types supported by this factory.
        
        Returns:
            Dictionary mapping card type categories to available types.
        """
        ...
