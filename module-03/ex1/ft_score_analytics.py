#!/usr/bin/env python3
"""Score Cruncher - Analyze player scores using lists."""

import sys


def analyze_scores(score_strings: list[str]) -> None:
    """
    Analyze player scores from command-line arguments.

    Args:
        score_strings: List of score values as strings
    """
    scores: list[int] = []

    for score_str in score_strings:
        try:
            score = int(score_str)
            scores.append(score)
        except ValueError:
            print(f"Error: '{score_str}' is not a valid number, skipping...")
            continue

    if not scores:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    """Run score analytics on command-line arguments."""
    if len(sys.argv) < 2:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        analyze_scores(sys.argv[1:])


if __name__ == "__main__":
    main()
