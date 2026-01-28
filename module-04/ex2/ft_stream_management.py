#!/usr/bin/env python3
"""Stream Management - Handle input/output stream control."""

import sys


def demonstrate_streams() -> None:
    """Demonstrate sys.stdout, sys.stderr, sys.stdin streams."""
    print("=== CYBER ARCHIVES - STREAM MANAGEMENT SYSTEM ===", file=sys.stdout)

    sys.stdout.write("Standard output stream activated.\n")
    sys.stderr.write("Standard error stream ready (not for errors now).\n")

    data_to_write = ["Stream 1: Data transmission protocol", "Stream 2: Archive protocol", "Stream 3: Verification protocol"]

    sys.stdout.write("\nWriting to standard output:\n")
    for data in data_to_write:
        sys.stdout.write(f"  ► {data}\n")

    sys.stderr.write("\nNotice: Using stderr for supplementary information.\n")
    sys.stderr.write("System: Stream buffer ready for next operation.\n")

    print("\n✓ All streams synchronized and flushed.", file=sys.stdout)


if __name__ == "__main__":
    demonstrate_streams()
