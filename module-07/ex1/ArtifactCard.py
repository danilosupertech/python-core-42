"""Artifact card concrete implementation."""
from __future__ import annotations

from typing import Dict

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("durability must be positive")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {"artifact": self.name, "active": False, "effect": "Broken"}
        self.durability -= 1
        return {"artifact": self.name, "active": True, "remaining_uses": self.durability, "effect": self.effect}
