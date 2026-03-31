# Lesson 1: Arrays Implementation (Python lists)
from __future__ import annotations

from typing import List, Any


def print_section(title: str) -> None:
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title))


def init_array() -> List[str]:
    """Create a simple list (dynamic array)."""
    return ["apple", "banana", "cherry"]


def access_elements(items: List[str]) -> None:
    print_section("Accessing Elements")
    print(f"First element: {items[0]}")  # O(1)
    print(f"Last element: {items[-1]}")  # O(1)


def update_elements(items: List[str]) -> None:
    print_section("Updating Elements")
    items[1] = "blueberry"  # O(1)
    print(f"After update: {items}")


def add_elements(items: List[str]) -> None:
    print_section("Adding Elements")
    items.append("date")  # Amortized O(1)
    items.insert(1, "avocado")  # O(n)
    print(f"After add: {items}")


def delete_elements(items: List[str]) -> None:
    print_section("Deleting Elements")
    removed = items.pop(2)  # O(n)
    print(f"Removed: {removed}")
    print(f"After delete: {items}")


def find_index(items: List[str], target: Any) -> int:
    """Return index of target, or -1 if not found."""
    try:
        return items.index(target)  # O(n)
    except ValueError:
        return -1


def search_elements(items: List[str]) -> None:
    print_section("Searching Elements")
    target = "cherry"
    idx = find_index(items, target)
    if idx == -1:
        print(f"{target} not found")
    else:
        print(f"Found {target} at index {idx}")


def traverse_elements(items: List[str]) -> None:
    print_section("Traversing Elements")
    for i, item in enumerate(items):
        print(f"Index {i}: {item}")


def slicing_example(items: List[str]) -> None:
    print_section("Slicing Example")
    print(f"First two: {items[:2]}")
    print(f"Last two: {items[-2:]}")


def array_basics() -> None:
    print_section("Initialization")
    fruits = init_array()
    print(f"Initial array: {fruits}")

    access_elements(fruits)
    update_elements(fruits)
    add_elements(fruits)
    delete_elements(fruits)
    search_elements(fruits)
    traverse_elements(fruits)
    slicing_example(fruits)


if __name__ == "__main__":
    array_basics()
