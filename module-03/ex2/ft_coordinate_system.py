#!/usr/bin/env python3
"""Position Tracker - 3D coordinate system using tuples."""

import math
import sys


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    """
    Parse coordinate string in format 'x,y,z' to tuple.

    Args:
        coord_str: Coordinate string like "3,4,0"

    Returns:
        Tuple of (x, y, z) coordinates

    Raises:
        ValueError: If parsing fails
    """
    parts = coord_str.split(",")
    if len(parts) != 3:
        raise ValueError(f"Expected 3 coordinates, got {len(parts)}")
    return tuple(int(p.strip()) for p in parts)  # type: ignore


def distance_3d(pos1: tuple[int, int, int], pos2: tuple[int, int, int]) -> float:
    """
    Calculate 3D Euclidean distance between two positions.

    Args:
        pos1: First position (x, y, z)
        pos2: Second position (x, y, z)

    Returns:
        Distance between the two positions
    """
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    """Demonstrate 3D coordinate system using tuples."""
    print("=== Game Coordinate System ===")

    position1: tuple[int, int, int] = (10, 20, 5)
    origin: tuple[int, int, int] = (0, 0, 0)

    print(f"Position created: {position1}")
    dist1 = distance_3d(origin, position1)
    print(f"Distance between {origin} and {position1}: {dist1:.2f}")

    print("\nParsing coordinates: \"3,4,0\"")
    try:
        position2 = parse_coordinates("3,4,0")
        print(f"Parsed position: {position2}")
        dist2 = distance_3d(origin, position2)
        print(f"Distance between {origin} and {position2}: {dist2:.1f}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")

    print("\nParsing invalid coordinates: \"abc,def,ghi\"")
    try:
        invalid_pos = parse_coordinates("abc,def,ghi")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, Args: {error.args}")

    print("\nUnpacking demonstration:")
    x, y, z = position2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
