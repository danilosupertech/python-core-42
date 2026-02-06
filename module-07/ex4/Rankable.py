"""Ranking interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Interface for entities with ranking and rating capabilities."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate the current rating.
        
        Returns:
            The calculated rating as an integer.
        """
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the number of wins.
        
        Args:
            wins: Number of wins to add.
        """
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the number of losses.
        
        Args:
            losses: Number of losses to add.
        """
        ...

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """Get ranking information.
        
        Returns:
            Dictionary containing rank information.
        """
        ...
