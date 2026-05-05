# gameplay.py
from player import Rogue, Warrior, Knight
from inventory import Inventory
from dungeon import explore_dungeon
from item import HealingItem

def start_game():
    print("\n=== Character Selection ===")
    print("1. Rogue")
    print("2. Warrior")
    print("3. Knight")

    choice = input("Choose your class: ").strip()

    if choice == "1":
        player = Rogue("Rogue")
    elif choice == "2":
        player = Warrior("Warrior")
    elif choice == "3":
        player = Knight("Knight")
    else:
        print("Invalid choice. Defaulting to Rogue.")
        player = Rogue("Rogue")

    print(f"\nYou have chosen {player.name}. Let the adventure begin!")

    # Starter potion with correct constructor call
    starter_potion = HealingItem(1, "Healing Potion", "Restores 50 HP", 50)
    player.inventory.add_item(starter_potion)

    run_game_loop(player)


def run_game_loop(player):
    while True:
        print("\n=== Gameplay Menu ===")
        print("1. Explore Dungeon")
        print("2. Check Inventory")
        print("3. Return to Main Menu")

        action = input("Choose an action: ").strip()

        if action == "1":
            explore_dungeon(player)
        elif action == "2":
            open_inventory(player)
        elif action == "3":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Try again.")

def open_inventory(player):
    while True:
        print("\n=== Inventory Menu ===")
        player.inventory.show_items()
        print("Options: ")
        print("1. Use Item")
        print("2. Exit Inventory")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if player.inventory.is_empty():
                print("No items to use.")
            else:
                item_index = int(input("Enter item number: ")) - 1
                if 0 <= item_index < len(player.inventory.items):
                    item = player.inventory.items[item_index]
                    player.inventory.use_item(item, player)
                else:
                    print("Invalid item number.")
        elif choice == "2":
            print("Exiting Inventory...")
            break
        else:
            print("Invalid choice. Try again.")

