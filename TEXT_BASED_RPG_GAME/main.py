# main.py
import sys
from menu import show_menu
from gameplay import start_game
from leaderboard import show_leaderboard

def main():
    print("=== Welcome to the Dungeon RPG ===")

    while True:
        choice = show_menu()

        if choice == "1":  # Start Game
            start_game()

        elif choice == "2":  # Leaderboard
            show_leaderboard()

        elif choice == "3":  # Exit
            confirm = input("Exit Game? (y/n): ").strip().lower()
            if confirm == "y":
                print("Thanks for Playing!")
                sys.exit(0)
            else:
                continue

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()