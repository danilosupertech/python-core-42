"""The Grimoire module - Circular import handling demonstrations."""

from .spellbook import record_spell
from .validator import validate_ingredients

__all__ = ["record_spell", "validate_ingredients"]
