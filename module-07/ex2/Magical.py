"""Abstract magic interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        ...

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        ...
