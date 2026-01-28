"""Exercise 3: Ancient Library - functools treasures."""
from __future__ import annotations

import functools
import operator
from typing import Callable, Dict, List, Any


OperationMap = Dict[str, Callable[[Any, Any], Any]]


def spell_reducer(spells: List[int], operation: str) -> int:
    """Reduce spell powers using the requested operation."""
    ops: OperationMap = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }
    if operation not in ops:
        raise ValueError("Unsupported operation")
    if not spells:
        return 0

    func = ops[operation]
    initial = spells[0]
    return functools.reduce(func, spells[1:], initial)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> Dict[str, Callable[[str], str]]:
    """Create partial enchantments with fixed power and element."""
    fire = functools.partial(base_enchantment, 50, "fire")
    ice = functools.partial(base_enchantment, 50, "ice")
    lightning = functools.partial(base_enchantment, 50, "lightning")
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


def memoized_fibonacci(n: int) -> int:
    """Compute fibonacci with LRU cache for performance."""

    @functools.lru_cache(maxsize=None)
    def fib(k: int) -> int:
        if k < 0:
            raise ValueError("n must be non-negative")
        if k in (0, 1):
            return k
        return fib(k - 1) + fib(k - 2)

    return fib(n)


def spell_dispatcher() -> Callable[[Any], Any]:
    """Create a single-dispatch spell handler."""
    @functools.singledispatch
    def dispatch(arg: Any) -> str:
        raise TypeError(f"Unsupported spell type: {type(arg).__name__}")

    @dispatch.register
    def _(arg: int) -> str:
        return f"Damage spell dealing {arg} points"

    @dispatch.register
    def _(arg: str) -> str:
        return f"Enchantment spell: {arg}"

    @dispatch.register
    def _(arg: list) -> List[str]:
        return [dispatch(item) for item in arg]

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print("Sum:", spell_reducer(powers, "add"))
    print("Product:", spell_reducer(powers, "multiply"))
    print("Max:", spell_reducer(powers, "max"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting partial enchanter...")
    def base(power: int, element: str, target: str) -> str:
        return f"{element.title()} enchantment of power {power} on {target}"

    enchants = partial_enchanter(base)
    print(enchants["fire_enchant"]("Blade"))

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(25))
    print(dispatch("Shield"))
    print(dispatch([10, "Haste"]))
