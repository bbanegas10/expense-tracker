# exporter.py
# This file saves expenses to a CSV file that Microsoft Excel can open.

import csv


def make_safe_for_excel(text):
    """Stop Excel from treating text as a formula.

    Excel runs anything that starts with = + - or @ as a formula,
    so we put a ' in front of those.
    """
    if text != "" and text[0] in "=+-@":
        return "'" + text
    return text


def export_to_csv(expenses, filename):
    """Write the list of expenses to a CSV file."""
    # utf-8-sig adds a small marker at the start of the file so Excel
    # shows special characters (like accents) correctly.
    # newline="" stops blank lines from appearing between rows on Windows.
    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        # first row is the column titles
        writer.writerow(["Date", "Category", "Description", "Amount"])

        # then one row for each expense
        for expense in expenses:
            writer.writerow([
                expense["date"],
                make_safe_for_excel(expense["category"]),
                make_safe_for_excel(expense["description"]),
                "{:.2f}".format(expense["amount"]),
            ])