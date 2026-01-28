"""Tournament management platform."""
from __future__ import annotations

import random
from typing import Dict, List

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registry: Dict[str, TournamentCard] = {}

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.lower().replace(' ', '_')}_{len(self.registry) + 1:03}"
        self.registry[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.registry[card1_id]
        card2 = self.registry[card2_id]

        winner = card1
        loser = card2
        if card2.calculate_rating() > card1.calculate_rating():
            winner, loser = card2, card1
        elif card2.calculate_rating() == card1.calculate_rating():
            winner, loser = random.sample([card1, card2], 2)

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": self._get_card_id(winner),
            "loser": self._get_card_id(loser),
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List[Dict]:
        ranked = sorted(self.registry.items(), key=lambda item: item[1].rating, reverse=True)
        return [
            {"id": card_id, **card.get_rank_info()}
            for card_id, card in ranked
        ]

    def generate_tournament_report(self) -> Dict:
        ratings = [card.rating for card in self.registry.values()]
        return {
            "total_cards": len(self.registry),
            "matches_played": sum(card.wins + card.losses for card in self.registry.values()) // 2,
            "avg_rating": round(sum(ratings) / len(ratings), 2) if ratings else 0,
            "platform_status": "active" if self.registry else "idle",
        }

    def _get_card_id(self, card: TournamentCard) -> str:
        for cid, stored in self.registry.items():
            if stored is card:
                return cid
        raise ValueError("Card not registered")
