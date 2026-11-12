# main.py
# Run this file to start the Expense Tracker:
#     python main.py

from expense_tracker.menu import run


def main():
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or Ctrl+D: leave quietly instead of showing an error
        print("\n\nGoodbye!")


if __name__ == '__main__':
    main()