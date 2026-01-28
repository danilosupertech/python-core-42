"""Demonstration of Sacred Scroll mastery - __init__.py mysteries."""

import alchemy
from alchemy import elements


def main() -> None:
    """Demonstrate Sacred Scroll concepts."""
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {elements.create_water()}")
    print(f"alchemy.elements.create_earth(): {elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        alchemy.create_earth()
        print("alchemy.create_earth(): accessible")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        alchemy.create_air()
        print("alchemy.create_air(): accessible")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
