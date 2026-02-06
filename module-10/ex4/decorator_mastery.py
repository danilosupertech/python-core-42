"""Exercise 4: Master’s Tower - decorator mastery and static methods."""
from __future__ import annotations

import functools
import time
from typing import Any, Callable


Spell = Callable[..., Any]


def spell_timer(func: Spell) -> Spell:
    """Decorator that measures execution time of a spell."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrapper that times the decorated function execution."""
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[[Spell], Spell]:
    """Decorator factory to validate the power argument."""

    def decorator(func: Spell) -> Spell:
        """Decorator that validates power before execution."""
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Wrapper that checks if power meets minimum requirement."""
            power = kwargs.get("power")
            if power is None and args:
                power = args[-1]
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[[Spell], Spell]:
    """Decorator that retries a spell on exception up to max_attempts times."""

    def decorator(func: Spell) -> Spell:
        """Decorator that adds retry logic to a spell."""
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Wrapper that retries spell execution on failures."""
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:  # pragma: no cover - defensive
                    attempts += 1
                    if attempts >= max_attempts:
                        return f"Spell casting failed after {max_attempts} attempts"
                    print(f"Spell failed, retrying... (attempt {attempts}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Guild demonstrating static validation and decorated casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate that a mage name has at least 3 characters and only letters/spaces."""
        return len(name) >= 3 and all(ch.isalpha() or ch.isspace() for ch in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with the specified name and power level."""
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        """Cast a fireball spell with a short delay."""
        time.sleep(0.05)
        return "Fireball cast!"

    print("Testing spell timer...")
    print("Result:", fireball())

    guild = MageGuild()
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Ana"))
    print(MageGuild.validate_mage_name("A"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Shield", 5))

    @retry_spell(max_attempts=3)
    def unstable_spell(count: list[int]) -> str:
        """An unstable spell that fails the first two attempts."""
        if count[0] < 2:
            count[0] += 1
            raise RuntimeError("Spell backfire")
        return "Stable cast"

    print("\nTesting retry_spell...")
    print(unstable_spell([0]))
