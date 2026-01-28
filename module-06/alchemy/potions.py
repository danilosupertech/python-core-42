"""Advanced potion recipes for the Alchemical Laboratory."""

from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Brew healing potion from fire and water.

    Returns:
        Healing potion description
    """
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    """Brew strength potion from earth and fire.

    Returns:
        Strength potion description
    """
    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    """Brew invisibility potion from air and water.

    Returns:
        Invisibility potion description
    """
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    """Brew wisdom potion from all elements.

    Returns:
        Wisdom potion description
    """
    fire_result = create_fire()
    water_result = create_water()
    earth_result = create_earth()
    air_result = create_air()
    all_results = (f"{fire_result}, {water_result}, "
                  f"{earth_result}, {air_result}")
    return f"Wisdom potion brewed with all elements: {all_results}"
