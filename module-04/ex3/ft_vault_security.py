#!/usr/bin/env python3
"""Vault Security - Implement secure resource handling with context managers."""

from typing import Optional, Type
from types import TracebackType


class SecureVault:
    """Context manager for secure vault operations."""

    def __init__(self, vault_name: str) -> None:
        """Initialize vault with given name."""
        self.vault_name = vault_name
        self.is_open = False

    def __enter__(self) -> "SecureVault":
        """Enter context: open vault and return self."""
        print(f"🔓 Opening vault: {self.vault_name}")
        self.is_open = True
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> Optional[bool]:
        """Exit context: close vault and ensure cleanup."""
        print(f"🔒 Closing vault: {self.vault_name}")
        self.is_open = False
        if exc_type is not None:
            print(f"   Warning: Exception occurred - {exc_type.__name__}")

    def store_data(self, data: str) -> None:
        """Store data securely in vault."""
        if self.is_open:
            print(f"   ✓ Data stored: {data}")
        else:
            print("   ERROR: Vault is closed")


def secure_archive_operations() -> None:
    """Demonstrate secure resource handling with context managers."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    with SecureVault("Primary-Archive-001") as vault1:
        vault1.store_data("Ancient Fragment Alpha")
        vault1.store_data("Digital Artifact Beta")

    print()

    with SecureVault("Secondary-Archive-002") as vault2:
        vault2.store_data("Cyber Relic Gamma")

    print("\n✓ All vault operations completed securely.")


if __name__ == "__main__":
    secure_archive_operations()
