"""Spell validation module for the Grimoire."""


def validate_ingredients(ingredients: str) -> str:
    """Validate spell ingredients.

    Args:
        ingredients: Ingredient string to validate

    Returns:
        Validation result as string
    """
    valid_elements = {"fire", "water", "earth", "air"}
    ingredient_list = ingredients.lower().split()

    is_valid = all(ing in valid_elements for ing in ingredient_list)

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
