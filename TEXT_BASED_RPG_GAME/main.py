# main.py
import sys
from menu import show_menu
from gameplay import start_game
from leaderboard import show_leaderboard
from character import Character


def main():
    print("=== Welcome to the Exiled Below RPG Game ===")

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

    # --- Test Inventory Access ---
    from character import Warrior
    from item import HealingItem

    player = Warrior("Test Warrior")
    potion = HealingItem(1, "Health Potion", "Restores 50 HP", 50)

    player.inventory.add_item(potion)
    player.inventory.show_items()