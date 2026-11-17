"""Module for interleaving elements from multiple iterables."""

from collections.abc import Iterable, Iterator
from typing import Any


def generator_interleaves(*iterables: Iterable[Any]) -> Iterator[Any]:
    """
    Yield elements from multiple iterables interleaved one by one.

    :param iterables: One or more iterable objects to interleave
    :return: Iterator yielding interleaved elements
    """
    iterators = [iter(iterable) for iterable in iterables]
    while iterators:
        active_iterators = []
        for iterator in iterators:
            try:
                yield next(iterator)
            except StopIteration:
                continue
            active_iterators.append(iterator)
        iterators = active_iterators


def interleaves(*iterables: Iterable[Any]) -> list[Any]:
    """
    Return a list of elements from multiple iterables interleaved together.

    :param iterables: One or more iterable objects to interleave
    :return: List containing the interleaved elements
    """
    return list(generator_interleaves(*iterables))


def main() -> None:
    """Verify interleaves output against the exercise example."""
    result = interleaves("abc", [1, 2, 3], ("!", "@", "#"))
    print(f"Interleaved result: {result}")


if __name__ == "__main__":
    main()
