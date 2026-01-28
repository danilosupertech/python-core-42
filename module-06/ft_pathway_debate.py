"""Demonstration of Pathway Debate - Absolute vs Relative Imports."""

from alchemy.transmutation import basic
import alchemy.transmutation as transmutation


def main() -> None:
    """Demonstrate absolute vs relative import pathways."""
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {basic.lead_to_gold()}")
    print(f"stone_to_gem(): {basic.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {transmutation.philosophers_stone()}")
    print(f"elixir_of_life(): {transmutation.elixir_of_life()}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{transmutation.philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
