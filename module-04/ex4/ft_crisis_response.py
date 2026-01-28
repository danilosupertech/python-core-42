#!/usr/bin/env python3
"""Crisis Response - Comprehensive error handling with context managers."""


class DataRecoveryVault:
    """Context manager for data recovery with error handling."""

    def __init__(self, filename: str) -> None:
        """Initialize vault for file recovery."""
        self.filename = filename
        self.file_handle = None

    def __enter__(self) -> "DataRecoveryVault":
        """Enter context: attempt to open file."""
        print(f"🚨 CRISIS MODE: Attempting recovery from {self.filename}")
        try:
            self.file_handle = open(self.filename, "r")
            print("   ✓ File accessed successfully")
        except FileNotFoundError:
            print(f"   ⚠ File not found: {self.filename}")
            self.file_handle = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context: ensure proper resource cleanup."""
        if self.file_handle:
            self.file_handle.close()
            print("   ✓ File safely closed")
        if exc_type is not None:
            print(f"   ERROR: {exc_type.__name__} - {exc_val}")
        print("   ✓ Crisis response protocol completed")

    def read_safely(self) -> str:
        """Read file content with error handling."""
        if self.file_handle is None:
            return "ERROR: No file to read"
        try:
            return self.file_handle.read()
        except IOError as e:
            return f"ERROR: IO operation failed - {e}"


def handle_data_crisis() -> None:
    """Demonstrate comprehensive error handling with context managers."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("Scenario 1: Attempting to recover existing file")
    with DataRecoveryVault("ancient_fragment.txt") as vault:
        content = vault.read_safely()
        if not content.startswith("ERROR"):
            print(f"   Recovered {len(content)} bytes")
        else:
            print(f"   Recovery status: {content}")

    print("\nScenario 2: Attempting to recover missing file")
    with DataRecoveryVault("missing_vault.txt") as vault:
        content = vault.read_safely()
        print(f"   Recovery status: {content}")

    print("\n✓ All crisis scenarios handled gracefully.")


if __name__ == "__main__":
    handle_data_crisis()
