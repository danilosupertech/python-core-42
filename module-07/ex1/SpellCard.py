"""Spell card concrete implementation."""
from __future__ import annotations

from enum import Enum
from typing import Dict, List, Union

from ex0.Card import Card


class EffectType(Enum):
    """Enumeration of possible spell effect types."""
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """Spell card with various effect types."""

    def __init__(self, name: str, cost: int, rarity: str, effect_type: Union[str, EffectType]) -> None:
        """Initialize a spell card.

        Args:
            name: The card name.
            cost: Mana cost to play the card.
            rarity: Card rarity level.
            effect_type: Type of effect (damage, heal, buff, debuff).
        """
        super().__init__(name, cost, rarity)
        if isinstance(effect_type, EffectType):
            self.effect_type = effect_type.value
        else:
            self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        """Play the spell card and resolve its effect.

        Args:
            game_state: Current game state dictionary.

        Returns:
            Dict containing card played, mana used, and effect description.
        """
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
        """Resolve spell effect on specified targets.

        Args:
            targets: List of target names for the spell effect.

        Returns:
            Dict with spell name, effect type, targets, and resolved status.
        """
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
