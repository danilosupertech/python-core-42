"""Creature card concrete implementation."""
from __future__ import annotations

from typing import Dict

from ex0.Card import Card


class CreatureCard(Card):
    """Creature card implementation with attack and health attributes."""
    
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        """Initialize a creature card with combat stats.
        
        Args:
            name: The creature's name.
            cost: The mana cost to play this creature.
            rarity: The rarity level of the creature.
            attack: The creature's attack power (must be positive).
            health: The creature's health points (must be positive).
            
        Raises:
            ValueError: If attack or health is not positive.
        """
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("attack and health must be positive")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        """Play this creature card to the battlefield.
        
        Args:
            game_state: The current game state dictionary.
            
        Returns:
            A dictionary with play results including card name, mana used, and effect.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: str) -> Dict:
        """Attack a target with this creature.
        
        Args:
            target: The name of the target being attacked.
            
        Returns:
            A dictionary with combat results including attacker, target, damage, and resolution status.
        """
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> Dict:
        """Get comprehensive creature card information including combat stats.
        
        Returns:
            A dictionary with card info plus attack and health values.
        """
        info = super().get_card_info()
        info.update({"attack": self.attack, "health": self.health, "type": "Creature"})
        return info
