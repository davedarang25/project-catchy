from player import Rogue, Warrior, Knight
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

    print(
        f"\nYou have chosen {player.name}. "
        f"Let the adventure begin!"
    )

    starter_potion = HealingItem(
        100,
        "Healing Potion",
        "Restores 50 HP",
        50
    )

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

            result = explore_dungeon(player)

            if result is False:
                return

            if not player.is_alive():
                return

        elif action == "2":

            player.inventory.inventory_menu(player)

        elif action == "3":

            print("Returning to Main Menu...")
            break

        else:

            print("Invalid choice. Try again.")