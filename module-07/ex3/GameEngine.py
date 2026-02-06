"""Game orchestrator using strategy and factory patterns."""
from __future__ import annotations

from typing import Dict, List, Optional

from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator using strategy and factory patterns."""

    def __init__(self) -> None:
        """Initialize the game engine with empty state."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.hand: List[Card] = []
        self.battlefield: List[Card] = []
        self.report: Dict = {"turns_simulated": 0, "strategy_used": None, "total_damage": 0, "cards_created": 0}

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        """Configure the game engine with a factory and strategy.
        
        Args:
            factory: CardFactory instance for creating cards.
            strategy: GameStrategy instance for turn execution.
        """
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature(),
            factory.create_creature("Goblin Warrior"),
            factory.create_spell(3),
        ]
        self.report["cards_created"] = len(self.hand)
        self.report["strategy_used"] = strategy.get_strategy_name()

    def simulate_turn(self) -> Dict:
        """Simulate a game turn using the configured strategy.
        
        Returns:
            Dictionary with turn simulation results.
            
        Raises:
            RuntimeError: If engine is not configured.
        """
        if not self.factory or not self.strategy:
            raise RuntimeError("Engine not configured")

        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.report["turns_simulated"] += 1
        self.report["total_damage"] += turn_result.get("damage_dealt", 0)
        return turn_result

    def get_engine_status(self) -> Dict:
        """Get the current status of the game engine.
        
        Returns:
            Dictionary with engine statistics and current state.
        """
        return {
            "turns_simulated": self.report["turns_simulated"],
            "strategy_used": self.report["strategy_used"],
            "total_damage": self.report["total_damage"],
            "hand_size": len(self.hand),
        }
