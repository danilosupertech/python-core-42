"""Exercise 0: Lambda Sanctum - mastering anonymous functions."""
from __future__ import annotations

from typing import Dict, List


def artifact_sorter(artifacts: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """Sort artifacts by power descending using a lambda key."""
    return sorted(artifacts, key=lambda item: item.get("power", 0), reverse=True)


def power_filter(mages: List[Dict[str, int | str]], min_power: int) -> List[Dict[str, int | str]]:
    """Filter mages with power >= min_power using a lambda predicate."""
    return list(filter(lambda mage: mage.get("power", 0) >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Wrap spell names with decorative markers using map + lambda."""
    return list(map(lambda name: f"* {name} *", spells))


def mage_stats(mages: List[Dict[str, int | str]]) -> Dict[str, float]:
    """Compute max, min, and average power using lambdas with built-ins."""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    power_values = list(map(lambda m: m.get("power", 0), mages))
    max_power = max(power_values)
    min_power = min(power_values)
    avg_power = round(sum(power_values) / len(power_values), 2)
    return {"max_power": max_power, "min_power": min_power, "avg_power": avg_power}


if __name__ == "__main__":
    # Quick sanity examples
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
    ]
    mages = [
        {"name": "Alex", "power": 70, "element": "fire"},
        {"name": "Riley", "power": 40, "element": "water"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for a in sorted_artifacts:
        print(a)

    print("\nTesting power filter (>=50)...")
    print(power_filter(mages, 50))

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nMage stats:")
    print(mage_stats(mages))
