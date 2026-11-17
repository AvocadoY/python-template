"""Module for measuring the execution time of a given function."""

import time
from typing import Any, Callable


def timer(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """
    Measure and return the execution time of `func` with the given arguments.

    :param func: The callable to execute and time
    :param args: Positional arguments to pass to `func`
    :param kwargs: Keyword arguments to pass to `func`
    :return: Execution duration in seconds
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


def running_2000(func: Callable[..., Any], *args: Any, **kwargs: Any) -> (
        float):
    """
    Wrapper function matching the module name that delegates to `timer`.

    :param func: The callable to execute and time
    :param args: Positional arguments to pass to `func`
    :param kwargs: Keyword arguments to pass to `func`
    :return: Execution duration in seconds
    """
    return timer(func, *args, **kwargs)


def main() -> None:
    """Verify timer and running_2000 against the exercise examples."""
    print(f"print duration: {timer(print, 'Hello')}s")
    print(f"zip duration: {timer(zip, [1, 2, 3], [4, 5, 6])}s")
    print(
        f"sorted duration: "
        f"{running_2000(sorted, [3, 1, 2], reverse=True)}s"
    )


if __name__ == "__main__":
    main()
