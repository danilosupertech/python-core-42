"""Exercise 1: Higher Realm - functions operating on functions."""
from __future__ import annotations

from typing import Callable, List, Tuple, Any


Spell = Callable[..., Any]


def spell_combiner(spell1: Spell, spell2: Spell) -> Spell:
    """Return a spell that calls both spells with same args and returns their results."""

    def combined(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        """Execute both spells with the same arguments."""
        return spell1(*args, **kwargs), spell2(*args, **kwargs)

    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """Return a spell that multiplies the base spell result."""

    def amplified(*args: Any, **kwargs: Any) -> Any:
        """Amplify the spell result by the multiplier."""
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: Spell, spell: Spell) -> Spell:
    """Return a spell that casts only when condition passes."""

    def caster(*args: Any, **kwargs: Any) -> Any:
        """Cast the spell only if the condition is met."""
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: List[Spell]) -> Spell:
    """Return a spell that casts all spells in order and returns list of results."""

    def sequenced(*args: Any, **kwargs: Any) -> List[Any]:
        """Execute all spells in sequence with the same arguments."""
        return [spell(*args, **kwargs) for spell in spells]

    return sequenced


if __name__ == "__main__":
    def fireball(target: str) -> str:
        """Cast a fireball spell at the target."""
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        """Cast a healing spell on the target."""
        return f"Heals {target}"

    combo = spell_combiner(fireball, heal)
    print("Testing spell combiner...")
    print("Combined spell result:", combo("Dragon"))

    mega_fireball = power_amplifier(lambda dmg: dmg, 3)
    print("\nTesting power amplifier...")
    print("Original: 10, Amplified:", mega_fireball(10))

    safe_cast = conditional_caster(lambda ok: ok, fireball)
    print("\nTesting conditional caster...")
    print(safe_cast(True))
    print(safe_cast(False))

    sequence = spell_sequence([fireball, heal])
    print("\nTesting spell sequence...")
    print(sequence("Golem"))
