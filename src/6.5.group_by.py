"""Module for grouping iterable elements by a key-generating function."""

from collections.abc import Callable, Iterable
from typing import Any


def group_by(
        func: Callable[[Any], Any], iterable: Iterable[Any]
) -> dict[Any, list[Any]]:
    """
    Group elements of an iterable into a dictionary based on a key function.

    :param func: Function applied to each element to determine its group key
    :param iterable: Iterable containing the elements to group
    :return: Dictionary mapping each key to a list of matching elements
    """
    grouped_items: dict[Any, list[Any]] = {}
    for item in iterable:
        key = func(item)
        grouped_items.setdefault(key, []).append(item)
    return grouped_items


def main() -> None:
    """Verify group_by output against the exercise example."""
    result = group_by(len, ["hi", "bye", "yo", "try"])
    print(f"Grouped result: {result}")


if __name__ == "__main__":
    main()
