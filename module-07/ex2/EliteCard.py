"""EliteCard with multiple abilities."""
from __future__ import annotations

from typing import Dict, List

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Elite card with combat and magical abilities."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana_pool: int = 0,
    ) -> None:
        """Initialize an elite card with combat and magic stats."""
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("attack and health must be positive")
        self.attack_power = attack
        self.health = health
        self.mana_pool = mana_pool

    def play(self, _game_state: Dict) -> Dict:
        """Play the elite card onto the field."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters with combat and magic readiness",
        }

    def attack(self, target: str) -> Dict:
        """Perform a melee attack on a target."""
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage, using attack power to block some damage."""
        blocked = max(self.attack_power // 2, 0)
        damage_taken = max(incoming_damage - blocked, 0)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        """Cast a spell on one or more targets, consuming mana."""
        mana_used = min(4, self.mana_pool + 4)  # simple example mana usage
        self.mana_pool = max(self.mana_pool - mana_used, 0)
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> Dict:
        """Channel mana to increase the mana pool."""
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_combat_stats(self) -> Dict:
        """Get current combat statistics."""
        return {"attack": self.attack_power, "health": self.health}

    def get_magic_stats(self) -> Dict:
        """Get current magic statistics."""
        return {"mana_pool": self.mana_pool}
