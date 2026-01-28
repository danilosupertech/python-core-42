"""Advanced transmutation spells - using relative imports."""

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create philosopher's stone using transmutation and potions.

    Returns:
        Philosopher's stone creation result
    """
    transmutation_result = lead_to_gold()
    potion_result = healing_potion()
    return (f"Philosopher's stone created using {transmutation_result} "
            f"and {potion_result}")


def elixir_of_life() -> str:
    """Create elixir of life.

    Returns:
        Elixir of life creation result
    """
    return "Elixir of life: eternal youth achieved!"
