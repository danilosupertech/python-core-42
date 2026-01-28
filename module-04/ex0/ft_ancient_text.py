#!/usr/bin/env python3
"""Ancient Text Recovery - Retrieve data from storage vaults."""


def recover_ancient_text() -> None:
    """Recover and display ancient data fragment from storage vault."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    try:
        with open(filename, "r") as vault:
            print("Connection established...")
            print("\nRECOVERED DATA:")
            content = vault.read()
            print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_ancient_text()
