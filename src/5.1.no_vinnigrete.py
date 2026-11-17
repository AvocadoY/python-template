"""Module for generating a random date between two user-provided dates."""

from datetime import date, datetime, timedelta
import random
from typing import Optional

DATE_FORMAT = "%Y-%m-%d"
EPOCH_DATE = date(1970, 1, 1)
MONDAY_WEEKDAY = 0
NO_VINAIGRETTE_MESSAGE = "אין לי ויניגרט!"


def parse_date(date_str: str) -> date:
    """
    Convert a date string in YYYY-MM-DD format into a date object.

    :param date_str: Date string formatted as YYYY-MM-DD
    :return: Parsed date object
    """
    return datetime.strptime(date_str.strip(), DATE_FORMAT).date()


def no_vinnigrete() -> Optional[date]:
    """
    Prompt for two dates, generate a random date between them, and check
    if it is Monday.

    :return: The generated random date, or None if input format is invalid
    """
    first_date_str = input("Enter first date (YYYY-MM-DD): ")
    second_date_str = input("Enter second date (YYYY-MM-DD): ")

    try:
        first_date = parse_date(first_date_str)
        second_date = parse_date(second_date_str)
    except ValueError:
        print(f"Invalid date format. Please use {DATE_FORMAT}.")
        return None

    start_date = min(first_date, second_date)
    end_date = max(first_date, second_date)

    start_days_from_epoch = (start_date - EPOCH_DATE).days
    end_days_from_epoch = (end_date - EPOCH_DATE).days

    random_days = random.randint(start_days_from_epoch, end_days_from_epoch)
    generated_date = EPOCH_DATE + timedelta(days=random_days)

    print(generated_date.strftime(DATE_FORMAT))
    if generated_date.weekday() == MONDAY_WEEKDAY:
        print(NO_VINAIGRETTE_MESSAGE)

    return generated_date


if __name__ == "__main__":
    no_vinnigrete()
