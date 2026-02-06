"""Tournament-ready card combining combat and ranking."""
from __future__ import annotations

from typing import Dict

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Tournament-ready card combining combat and ranking capabilities."""

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int, rating: int = 1200) -> None:
        """Initialize a tournament card.
        
        Args:
            name: Card name.
            cost: Mana cost.
            rarity: Card rarity.
            attack: Attack power.
            health: Health points.
            rating: Initial tournament rating (default 1200).
        """
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: Dict) -> Dict:
        """Play this card in the tournament arena.
        
        Args:
            game_state: Current game state dictionary.
            
        Returns:
            Dictionary with play results.
        """
        return {"card_played": self.name, "mana_used": self.cost, "effect": "Enters tournament arena"}

    def attack(self, target: str) -> Dict:
        """Attack a target.
        
        Args:
            target: The target to attack.
            
        Returns:
            Dictionary with attack results.
        """
        return {"attacker": self.name, "target": target, "damage": self.attack_power}

    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage.
        
        Args:
            incoming_damage: Amount of incoming damage.
            
        Returns:
            Dictionary with defense results.
        """
        blocked = max(self.attack_power // 3, 0)
        damage_taken = max(incoming_damage - blocked, 0)
        self.health -= damage_taken
        return {"defender": self.name, "damage_taken": damage_taken, "still_alive": self.health > 0}

    def get_combat_stats(self) -> Dict:
        """Get current combat statistics.
        
        Returns:
            Dictionary with attack and health values.
        """
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        """Calculate rating based on wins and losses.
        
        Returns:
            The calculated rating.
        """
        return int(self.rating + (self.wins * 16) - (self.losses * 10))

    def update_wins(self, wins: int) -> None:
        """Update wins and recalculate rating.
        
        Args:
            wins: Number of wins to add.
        """
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        """Update losses and recalculate rating.
        
        Args:
            losses: Number of losses to add.
        """
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> Dict:
        """Get ranking information for this card.
        
        Returns:
            Dictionary with name, rating, wins, and losses.
        """
        return {"name": self.name, "rating": self.rating, "wins": self.wins, "losses": self.losses}

    def get_tournament_stats(self) -> Dict:
        """Get comprehensive tournament statistics.
        
        Returns:
            Dictionary with ranking info and combat stats.
        """
        stats = self.get_rank_info()
        stats.update({"attack": self.attack_power, "health": self.health})
        return stats
