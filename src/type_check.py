"""Module providing a type-checking decorator factory for single-argument
functions."""

from functools import wraps
from typing import Callable, Type, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class InvalidArgumentTypeError(TypeError):
    """Raised when a decorated function receives an argument of the wrong
    type."""


def type_check(
        expected_type: Type[T],
) -> Callable[[Callable[[T], R]], Callable[[T], R]]:
    """
    Create a decorator that validates the type of a single-argument function.

    :param expected_type: The expected type of the function's sole parameter
    :return: A decorator enforcing the specified argument type
    """

    def decorator(func: Callable[[T], R]) -> Callable[[T], R]:
        @wraps(func)
        def wrapper(arg: T) -> R:
            if not isinstance(arg, expected_type) or (
                    expected_type is int and isinstance(arg, bool)
            ):
                raise InvalidArgumentTypeError(
                    f"Expected argument of type {expected_type.__name__}, "
                    f"got {type(arg).__name__} instead."
                )
            return func(arg)

        return wrapper

    return decorator


@type_check(int)
def square(number: int) -> int:
    """
    Return the square of an integer.

    :param number: The integer to square
    :return: The squared integer
    """
    return number * number


def main() -> None:
    """Demonstrate type_check behavior on valid and invalid inputs."""
    print(f"Function name preserved: {square.__name__}")
    print(f"Valid call square(5): {square(5)}")

    try:
        square("not_an_int")  # type: ignore[arg-type]
    except InvalidArgumentTypeError as error:
        print(f"Caught expected error: {error}")


if __name__ == "__main__":
    main()
