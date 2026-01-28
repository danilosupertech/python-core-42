"""Concrete fantasy-themed card factory."""
from __future__ import annotations

from typing import Dict

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> CreatureCard:
        if isinstance(name_or_power, int):
            attack = max(1, name_or_power)
            return CreatureCard("Goblin Warrior", cost=2, rarity="Common", attack=attack, health=attack + 1)
        return CreatureCard(name_or_power or "Fire Dragon", cost=5, rarity="Legendary", attack=7, health=5)

    def create_spell(self, name_or_power: str | int | None = None) -> SpellCard:
        if isinstance(name_or_power, int):
            return SpellCard("Lightning Bolt", cost=3, rarity="Rare", effect_type="damage")
        return SpellCard(name_or_power or "Healing Light", cost=2, rarity="Uncommon", effect_type="heal")

    def create_artifact(self, name_or_power: str | int | None = None) -> ArtifactCard:
        return ArtifactCard(name_or_power or "Mana Ring", cost=2, rarity="Uncommon", durability=3, effect="+1 mana per turn")

    def create_themed_deck(self, size: int) -> Dict:
        cards = []
        for i in range(size):
            if i % 3 == 0:
                cards.append(self.create_creature())
            elif i % 3 == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {"cards": cards, "counts": {"creatures": sum(c.__class__.__name__ == "CreatureCard" for c in cards)}}

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "heal"],
            "artifacts": ["mana_ring"],
        }
