"""Abstract combat interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    """Abstract base class for combat-capable entities."""

    @abstractmethod
    def attack(self, target: str) -> Dict:
        """Perform an attack on a target."""
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage."""
        ...

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """Get current combat statistics."""
        ...
