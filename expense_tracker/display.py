# display.py
# This file prints expenses to the console as a table.


def get_total(expenses):
    """Add up the amount of every expense."""
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return round(total, 2)


def print_expenses(expenses):
    """Print the expenses in a table, sorted by date, with a total at the end."""
    if len(expenses) == 0:
        print("\nNo expenses to show.")
        return

    # sort by date (oldest first)
    sorted_expenses = sorted(expenses, key=lambda expense: expense["date"])

    # find how wide the Category and Description columns need to be
    category_width = len("Category")
    description_width = len("Description")
    for expense in sorted_expenses:
        if len(expense["category"]) > category_width:
            category_width = len(expense["category"])
        if len(expense["description"]) > description_width:
            description_width = len(expense["description"])

    # build one row of text for the table
    row_format = "{:<3} {:<10}  {:<" + str(category_width) + "}  {:<" + str(description_width) + "}  {:>10}"

    header = row_format.format("#", "Date", "Category", "Description", "Amount")
    line = "-" * len(header)

    print()
    print(header)
    print(line)

    number = 1
    for expense in sorted_expenses:
        amount_text = "${:,.2f}".format(expense["amount"])
        print(row_format.format(number, expense["date"], expense["category"],
                                expense["description"], amount_text))
        number = number + 1

    print(line)
    total_text = "${:,.2f}".format(get_total(sorted_expenses))
    print(row_format.format("", "", "", "TOTAL", total_text))
    print(str(len(sorted_expenses)) + " expense(s) shown.")