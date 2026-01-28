"""Spell recording module for the Grimoire - Using late imports to avoid circular dependency."""


def record_spell(spell_name: str, ingredients: str) -> str:
    """Record a spell after validating ingredients using late import.

    Args:
        spell_name: Name of the spell
        ingredients: Ingredient string

    Returns:
        Spell recording result
    """
    # Use absolute import to satisfy static analyzers while keeping late import.
    from alchemy.grimoire.validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    # Accept only explicitly valid outcomes; avoid substring matches on "INVALID".
    if validation_result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"

    return f"Spell rejected: {spell_name} ({validation_result})"
