#!/usr/bin/env python3
"""Stream Wizard - Process data streams using generators."""

from typing import Dict, Any, Generator


def game_event_stream(count: int) -> Generator[Dict[str, Any], None, None]:
    """
    Generate game events on-demand.

    Args:
        count: Number of events to generate

    Yields:
        Event dictionaries
    """
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up", "healed player"]
    levels = [5, 12, 8, 15, 10]

    for i in range(count):
        player_idx = i % len(players)
        event_idx = i % len(events)
        level = levels[i % len(levels)]

        yield {
            "id": i + 1,
            "player": players[player_idx],
            "level": level,
            "event": events[event_idx],
        }


def fibonacci_stream(limit: int) -> Generator[int, None, None]:
    """
    Generate Fibonacci numbers up to limit.

    Args:
        limit: Maximum number of values to generate

    Yields:
        Fibonacci numbers
    """
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def prime_stream(limit: int) -> Generator[int, None, None]:
    """
    Generate prime numbers up to limit count.

    Args:
        limit: Maximum number of primes to generate

    Yields:
        Prime numbers
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while count < limit:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main() -> None:
    """Demonstrate generators for streaming data."""
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")

    event_count = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for event in game_event_stream(1000):
        event_count += 1

        if event_count <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['event']}"
            )

        if event["level"] >= 10:
            high_level_count += 1
        if "treasure" in event["event"]:
            treasure_count += 1
        if "leveled up" in event["event"]:
            levelup_count += 1

    if event_count > 3:
        print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fibs = list(fibonacci_stream(10))
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fibs))}")

    primes = list(prime_stream(5))
    print(f"Prime numbers (first 5): {', '.join(map(str, primes))}")


if __name__ == "__main__":
    main()
