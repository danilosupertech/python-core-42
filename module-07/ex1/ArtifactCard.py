"""Artifact card concrete implementation."""
from __future__ import annotations

from typing import Dict

from ex0.Card import Card


class ArtifactCard(Card):
    """Artifact card with durability and persistent effects."""

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        """Initialize an artifact card.

        Args:
            name: The card name.
            cost: Mana cost to play the card.
            rarity: Card rarity level.
            durability: Number of times the artifact can be activated.
            effect: The artifact's effect description.

        Raises:
            ValueError: If durability is not positive.
        """
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("durability must be positive")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        """Play the artifact card.

        Args:
            game_state: Current game state dictionary.

        Returns:
            Dict containing card played, mana used, and effect description.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> Dict:
        """Activate the artifact's ability, consuming one durability.

        Returns:
            Dict with artifact name, active status, remaining uses, and effect.
        """
        if self.durability <= 0:
            return {"artifact": self.name, "active": False, "effect": "Broken"}
        self.durability -= 1
        return {"artifact": self.name, "active": True, "remaining_uses": self.durability, "effect": self.effect}
