"""Module for calculating the total cost of recipe ingredients."""

from typing import List, Optional

GRAMS_PER_UNIT = 100


def get_recipe_price(
        prices: dict[str, float],
        optionals: Optional[List[str]] = None,
        **quantities: float,
) -> float:
    """
    Calculate the total price of ingredients needed for a recipe.

    :param prices: Dictionary mapping ingredient names to their price per
    100g
    :param optionals: Optional list of ingredient names to exclude from
    purchase
    :param quantities: Keyword arguments mapping ingredient names to grams
    needed
    :return: Total cost of the required ingredients
    """
    ignored_items = set(optionals) if optionals else set()
    return sum(
        price * (quantities.get(item, 0) / GRAMS_PER_UNIT)
        for item, price in prices.items()
        if item not in ignored_items
    )


def piece_of_cake(
        prices: dict[str, float],
        optionals: Optional[List[str]] = None,
        **quantities: float,
) -> float:
    """
    Wrapper function matching the module name that delegates to
    `get_recipe_price`.

    :param prices: Dictionary mapping ingredient names to their price per 100g
    :param optionals: Optional list of ingredient names to exclude from
    purchase
    :param quantities: Keyword arguments mapping ingredient names to grams
    needed
    :return: Total cost of the required ingredients
    """
    return get_recipe_price(prices, optionals=optionals, **quantities)


def main() -> None:
    """Verify get_recipe_price and piece_of_cake output against the examples."""
    print(get_recipe_price(
        {"chocolate": 18, "milk": 8}, chocolate=200, milk=100))
    print(
        piece_of_cake(
            {"chocolate": 18, "milk": 8}, optionals=["milk"], chocolate=300
        )
    )
    print(get_recipe_price({}))


if __name__ == "__main__":
    main()
