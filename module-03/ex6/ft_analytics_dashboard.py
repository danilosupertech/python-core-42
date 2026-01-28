#!/usr/bin/env python3
"""Data Alchemist - Transform data with comprehensions."""


def main() -> None:
    """Demonstrate list, dict, and set comprehensions."""
    players_data = [
        {"name": "alice", "score": 2300, "achievements": 5},
        {"name": "bob", "score": 1800, "achievements": 3},
        {"name": "charlie", "score": 2150, "achievements": 7},
        {"name": "diana", "score": 2050, "achievements": 4},
    ]

    scores = [p["score"] for p in players_data]
    achievements_list = [p["achievements"] for p in players_data]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players_data if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [s * 2 for s in scores]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [p["name"] for p in players_data if p["achievements"] > 2]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players_data}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": len([s for s in scores if s > 2100]),
        "medium": len([s for s in scores if 1900 <= s <= 2100]),
        "low": len([s for s in scores if s < 1900]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p["name"]: p["achievements"] for p in players_data}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players_data}
    print(f"Unique players: {unique_players}")

    unique_achievements = {"first_kill", "level_10", "boss_slayer"}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {"north", "east", "central"}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(players_data)
    total_unique_achievements = len(unique_achievements) * 4
    average_score = sum(scores) / len(scores)
    top_player = max(players_data, key=lambda p: p["score"])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {top_player['name']} "
        f"({top_player['score']} points, {top_player['achievements']} achievements)"
    )


if __name__ == "__main__":
    main()
