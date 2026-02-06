"""Abstract game strategy interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class GameStrategy(ABC):
    """Abstract strategy interface for game turn execution."""

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """Execute a game turn with given hand and battlefield.
        
        Args:
            hand: List of cards in hand.
            battlefield: List of cards on battlefield.
            
        Returns:
            Dictionary with turn execution results.
        """
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Get the name of this strategy.
        
        Returns:
            The strategy name as a string.
        """
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        """Prioritize targets for attacks.
        
        Args:
            available_targets: List of available targets.
            
        Returns:
            Prioritized list of targets.
        """
        ...
