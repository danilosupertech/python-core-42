"""Exercise 2: Memory Depths - lexical scoping and closures."""
from __future__ import annotations

from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    """Return a counter function that remembers its call count."""
    count = 0

    def counter() -> int:
        """Increment and return the call count."""
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Return a function that accumulates power over time."""
    total = initial_power

    def accumulator(amount: int) -> int:
        """Add amount to total power and return the new total."""
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return a function that applies an enchantment type to an item."""

    def enchant(item_name: str) -> str:
        """Apply the enchantment to the given item."""
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, Callable[..., Any]]:
    """Return store/recall functions sharing a private memory."""
    storage: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        """Store a value in the vault with the given key."""
        storage[key] = value

    def recall(key: str) -> Any:
        """Retrieve a value from the vault by key."""
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
