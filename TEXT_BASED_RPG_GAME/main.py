import sys
from .menu import show_menu
from .gameplay import start_game
from .leaderboard import show_leaderboard
from .utils import clear_screen


def main():

    print("=== Welcome to the Exiled Below RPG Game ===")

    while True:
        clear_screen()
        choice = show_menu()

        if choice == "1":
            start_game()

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":

            confirm = input("Exit Game? (y/n): ").strip().lower()

            if confirm == "y":

                print("Thanks for Playing!")
                sys.exit(0)

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()