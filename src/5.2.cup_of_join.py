"""Module for joining multiple lists into a single list with a separator."""

from typing import List, Any, Optional

DEFAULT_SEP = '-'


def join(*lists: list[Any], sep: Any = DEFAULT_SEP) -> Optional[list[Any]]:
    """
    Combine any number of lists into a single list separated by `sep`.

    :param lists: Variable number of lists to join
    :param sep: Separator element placed between lists (defaults to '-')
    :return: Combined list with separators, or None if no lists were provided
    """
    if not lists:
        return None

    return list(lists[0]) + [
        item for lst in lists[1:] for item in [sep] + lst
    ]


def cup_of_join(
        *lists: list[Any], sep: Any = DEFAULT_SEP
) -> Optional[List[Any]]:
    """
    Wrapper function matching the module name that delegates to `join`.

    :param lists: Variable number of lists to join
    :param sep: Separator element placed between lists (defaults to '-')
    :return: Combined list with separators, or None if no lists were provided
    """
    return join(*lists, sep=sep)


def main() -> None:
    """Verify the join function output against the exercise examples."""
    print(join([1, 2], [8], [9, 5, 6], sep="@"))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())


if __name__ == "__main__":
    main()
