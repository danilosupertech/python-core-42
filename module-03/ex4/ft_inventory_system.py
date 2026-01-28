#!/usr/bin/env python3
"""Inventory Master - Manage game inventory with dictionaries."""

import sys


def parse_inventory(items_str: list[str]) -> dict[str, int]:
    """
    Parse inventory items from command-line format (item:quantity).

    Args:
        items_str: List of "item:quantity" strings

    Returns:
        Dictionary mapping item names to quantities
    """
    inventory: dict[str, int] = {}
    for item in items_str:
        try:
            name, qty_str = item.split(":")
            quantity = int(qty_str)
            inventory[name] = quantity
        except (ValueError, IndexError):
            print(f"Error parsing item '{item}', skipping...")
    return inventory


def main() -> None:
    """Demonstrate inventory management with dictionaries."""
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item1:qty1 item2:qty2 ...")
        return

    inventory = parse_inventory(sys.argv[1:])

    if not inventory:
        print("No valid items provided")
        return

    total_items = sum(inventory.values())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    sorted_inventory = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))
    for item, quantity in sorted_inventory.items():
        percentage = (quantity / total_items) * 100
        print(f"{item}: {quantity} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    max_item = max(inventory, key=inventory.get)
    min_item = min(inventory, key=inventory.get)
    print(f"Most abundant: {max_item} ({inventory[max_item]} units)")
    print(f"Least abundant: {min_item} ({inventory[min_item]} units)")

    print("\n=== Item Categories ===")
    moderate = {k: v for k, v in inventory.items() if v >= 5}
    scarce = {k: v for k, v in inventory.items() if v < 5}
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock_needed = [item for item, qty in inventory.items() if qty <= 2]
    if restock_needed:
        print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    sample_item = list(inventory.keys())[0]
    print(f"Sample lookup - '{sample_item}' in inventory: {sample_item in inventory}")


if __name__ == "__main__":
    main()
