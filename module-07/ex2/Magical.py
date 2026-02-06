"""Abstract magic interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    """Abstract base class for magic-capable entities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        """Cast a spell on one or more targets."""
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """Channel mana to increase the mana pool."""
        ...

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """Get current magic statistics."""
        ...
