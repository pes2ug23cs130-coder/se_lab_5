"""
A simple command-line inventory management system.

This module allows users to add, remove, and track items in an inventory.
The inventory data can be saved to and loaded from a JSON file.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Adds a specified quantity of an item to the inventory.

    Args:
        item: The name of the item to add.
        qty: The quantity to add.
        logs: A list to append log messages to.
              One is created if not provided.
    """
    if logs is None:
        logs = []

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Removes a specified quantity of an item from the inventory.

    If the quantity drops to 0 or below, the item is removed entirely.
    Catches KeyError if the item doesn't exist.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not found in inventory.")


def get_qty(item):
    """Returns the current quantity of a specific item."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Loads the inventory data from a JSON file."""
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: '{file}' not found. Starting with an empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file}'. Starting fresh.")
        stock_data = {}


def save_data(file="inventory.json"):
    """Saves the current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))


def print_data():
    """Prints a report of all items and their quantities."""
    print("Items Report")
    print("--------------")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")
    print("--------------")


def check_low_items(threshold=5):
    """
    Returns a list of items that are at or below the threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to run example operations."""
    load_data()  # Start by loading existing data

    logs = []
    add_item("apple", 10, logs)
    add_item("banana", 15, logs)

    # This call will now fail safely due to type errors
    # add_item(123, "ten")

    remove_item("apple", 3)
    remove_item("orange", 1)  # Will print an error message

    try:
        print("Apple stock:", get_qty("apple"))
    except KeyError:
        print("Apple stock: 0")

    print("Low items:", check_low_items())

    print_data()
    save_data()

    print("\nLogs:")
    for log_entry in logs:
        print(log_entry)


if __name__ == "__main__":
    main()

