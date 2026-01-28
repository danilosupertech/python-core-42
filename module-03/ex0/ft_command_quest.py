#!/usr/bin/env python3
"""Command Quest - Master command-line argument processing."""

import sys


def main() -> None:
    """Display command-line arguments received by the program."""
    print("=== Command Quest ===")

    program_name = sys.argv[0].split("/")[-1]

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
