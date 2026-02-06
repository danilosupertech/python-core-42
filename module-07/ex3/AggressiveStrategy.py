"""Concrete aggressive strategy implementation."""
from __future__ import annotations

from typing import Dict, List

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Aggressive strategy that prioritizes fast attacks and damage."""

    def __init__(self) -> None:
        """Initialize the aggressive strategy."""
        super().__init__()

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """Execute an aggressive turn by playing cards and attacking.
        
        Args:
            hand: List of cards available to play.
            battlefield: List of cards currently on the battlefield.
            
        Returns:
            Dictionary with turn execution results.
        """
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
        """Get the name of this strategy.
        
        Returns:
            The strategy name as a string.
        """
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        """Prioritize targets for aggressive attacks.
        
        Args:
            available_targets: List of available targets.
            
        Returns:
            List with the highest priority target (first in list).
        """
        return available_targets[:1] if available_targets else []
