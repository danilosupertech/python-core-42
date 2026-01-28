"""Concrete aggressive strategy implementation."""
from __future__ import annotations

from typing import Dict, List

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        hand_sorted = sorted(hand, key=lambda c: getattr(c, "cost", 0))
        cards_played = [card.name for card in hand_sorted[:2]] if hand_sorted else []
        mana_used = sum(getattr(card, "cost", 0) for card in hand_sorted[:2])
        targets_attacked = ["Enemy Player"] if cards_played else []
        damage_dealt = sum(getattr(card, "attack", 2) for card in hand_sorted[:1]) or 0
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        return available_targets[:1] if available_targets else []
