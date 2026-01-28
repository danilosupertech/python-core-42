"""Tournament-ready card combining combat and ranking."""
from __future__ import annotations

from typing import Dict

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int, rating: int = 1200) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: Dict) -> Dict:
        return {"card_played": self.name, "mana_used": self.cost, "effect": "Enters tournament arena"}

    def attack(self, target: str) -> Dict:
        return {"attacker": self.name, "target": target, "damage": self.attack_power}

    def defend(self, incoming_damage: int) -> Dict:
        blocked = max(self.attack_power // 3, 0)
        damage_taken = max(incoming_damage - blocked, 0)
        self.health -= damage_taken
        return {"defender": self.name, "damage_taken": damage_taken, "still_alive": self.health > 0}

    def get_combat_stats(self) -> Dict:
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        return int(self.rating + (self.wins * 16) - (self.losses * 10))

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> Dict:
        return {"name": self.name, "rating": self.rating, "wins": self.wins, "losses": self.losses}

    def get_tournament_stats(self) -> Dict:
        stats = self.get_rank_info()
        stats.update({"attack": self.attack_power, "health": self.health})
        return stats
