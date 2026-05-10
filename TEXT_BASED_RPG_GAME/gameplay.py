from .player import create_player
from .dungeon import explore_dungeon
from .item import HealingItem

try:
    from .utils import clear_screen
except ImportError:

    def clear_screen():
        pass


def start_game():

    print("\n=== Character Selection ===")
    print("1. Rogue")
    print("2. Warrior")
    print("3. Knight")

    choice = input("Choose your class: ").strip()
    clear_screen()

    if choice == "1":
        player = create_player("Rogue")

    elif choice == "2":
        player = create_player("Warrior")

    elif choice == "3":
        player = create_player("Knight")

    else:
        print("Invalid choice. Defaulting to Rogue.")
        player = create_player("Rogue")

    print(
        f"\nYou have chosen {player.name}. "
        f"Let the adventure begin!"
    )

    starter_potion = HealingItem(
        100,
        "Healing Potion",
        "Restores 50 HP.",
        50
    )

    player.inventory.add_item(
        starter_potion,
        player
    )

    run_game_loop(player)


def run_game_loop(player):

    while True:

        print("\n=== Gameplay Menu ===")
        print("1. Explore Dungeon")
        print("2. Check Inventory")
        print("3. Return to Main Menu")

        action = input("Choose an action: ").strip()
        clear_screen()

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