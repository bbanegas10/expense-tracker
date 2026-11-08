# storage.py
# This file saves expenses to a JSON file and loads them back.

import json
import os

from expense_tracker.expense import make_expense


def save_expenses(expenses, filename):
    """Write the list of expenses to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def load_expenses(filename):
    """Read expenses from a JSON file and return them as a list.

    If the file does not exist yet, return an empty list.
    Raises a ValueError if the file is not a valid expense file.
    """
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("That file is not valid JSON.")

    if not isinstance(data, list):
        raise ValueError("That file does not contain a list of expenses.")

    # Check every record so a bad file can't sneak in bad data
    expenses = []
    for number, record in enumerate(data, start=1):
        try:
            expense = make_expense(
                str(record["date"]),
                str(record["category"]),
                str(record.get("description", "")),
                str(record["amount"]),
            )
        except (KeyError, TypeError, AttributeError):
            raise ValueError("Expense number " + str(number) + " is missing information.")
        except ValueError as error:
            raise ValueError("Expense number " + str(number) + ": " + str(error))
        expenses.append(expense)

    return expenses