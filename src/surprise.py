"""Module providing a decorator that replaces function execution with a
surprise message."""

from functools import wraps
from typing import Any, Callable


def surprise(func: Callable[..., Any]) -> Callable[..., None]:
    """
    Decorate a function so it prints 'surprise!' instead of running its body.

    :param func: The target function to override
    :return: A wrapper function that prints 'surprise!'
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:  # pylint: disable=unused-argument
        print("surprise!")

    return wrapper


@surprise
def calculate_sum(first: int, second: int) -> int:
    """
    Return the sum of two integers.

    :param first: First integer
    :param second: Second integer
    :return: Sum of the two integers
    """
    return first + second


def main() -> None:
    """Demonstrate the surprise decorator."""
    print(f"Function name preserved: {calculate_sum.__name__}")
    calculate_sum(3, 4)


if __name__ == "__main__":
    main()
