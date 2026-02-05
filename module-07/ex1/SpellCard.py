"""Spell card concrete implementation."""
from __future__ import annotations

from enum import Enum
from typing import Dict, List, Union

from ex0.Card import Card


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: Union[str, EffectType]) -> None:
        super().__init__(name, cost, rarity)
        if isinstance(effect_type, EffectType):
            self.effect_type = effect_type.value
        else:
            self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        effect_map = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Grant +1 attack to ally",
            "debuff": "Reduce enemy attack by 1",
        }
        effect = effect_map.get(self.effect_type, f"{self.effect_type.capitalize()} spell resolved")
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect,
        }

    def resolve_effect(self, targets: List[str]) -> Dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
