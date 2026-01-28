"""Exercise 2: Memory Depths - lexical scoping and closures."""
from __future__ import annotations

from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    """Return a counter function that remembers its call count."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Return a function that accumulates power over time."""
    total = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return a function that applies an enchantment type to an item."""

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, Callable[..., Any]]:
    """Return store/recall functions sharing a private memory."""
    storage: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    print(vault["recall"]("spell"))
    print(vault["recall"]("unknown"))
