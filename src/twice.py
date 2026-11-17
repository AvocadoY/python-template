"""Module providing a decorator that executes a wrapped function twice."""

from typing import Any, Callable

from decorator import decorator


@decorator
def twice(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Execute the decorated function twice and return the second call's result.

    :param func: The target function to execute twice
    :param args: Positional arguments forwarded to `func`
    :param kwargs: Keyword arguments forwarded to `func`
    :return: Return value from the second invocation of `func`
    """
    func(*args, **kwargs)
    return func(*args, **kwargs)


@twice
def greet(name: str) -> str:
    """
    Print and return a greeting for the given name.

    :param name: Name of the person to greet
    :return: Greeting string
    """
    message = f"Hello, {name}!"
    print(message)
    return message


def main() -> None:
    """Demonstrate the twice decorator."""
    print(f"Function name preserved: {greet.__name__}")
    result = greet("Alice")
    print(f"Returned value: {result}")


if __name__ == "__main__":
    main()
