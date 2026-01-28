"""Demonstration script for Exercise 3: Game Engine."""
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def demo() -> None:
    print("=== DataDeck Game Engine ===")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("Simulating aggressive turn...")
    turn_result = engine.simulate_turn()
    print("Turn execution:")
    print(turn_result)

    print("Game Report:")
    print(engine.get_engine_status())

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


def main() -> None:
    demo()


if __name__ == "__main__":
    main()
