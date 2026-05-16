from .player import create_player
from .dungeon import explore_dungeon
from .item import HealingItem
from .utils import clear_screen


def line(length=60):
    print("=" * length)


def small_line(length=60):
    print("-" * length)


def pause():
    input("\nPress Enter to continue...")
    clear_screen()


def show_character_selection():

    clear_screen()

    line()
    print("                  CHARACTER SELECTION")
    line()

    print("\nChoose your class:\n")

    print("[1] Rogue")
    small_line()
    print("HP              : 80")
    print("Attack          : 15")
    print("Defense         : 3")
    print("Special Attack  : Backstab")
    print("Effect          : Deals attack x2 damage")
    print("Extra Stats     : Crit Rate + Dodge")

    print()

    print("[2] Warrior")
    small_line()
    print("HP              : 120")
    print("Attack          : 12")
    print("Defense         : 8")
    print("Special Attack  : Power Strike")
    print("Effect          : Deals attack + strength damage")
    print("Bonus           : Rage +5")

    print()

    print("[3] Knight")
    small_line()
    print("HP              : 150")
    print("Attack          : 10")
    print("Defense         : 12")
    print("Special Attack  : Shield Bash")
    print("Effect          : Deals damage and increases DEF by 1")
    print("Extra Stats     : Shield Block + Endurance")

    print()
    line()

    choice = input("Choose your class: ").strip()
    clear_screen()

    return choice


def show_special_attack_info(player):

    if player.name == "Rogue":

        print("Special Attack  : Backstab")
        print("Effect          : Deals attack x2 damage")

    elif player.name == "Warrior":

        print("Special Attack  : Power Strike")
        print("Effect          : Deals attack + strength damage")
        print("Bonus           : Rage +5")

    elif player.name == "Knight":

        print("Special Attack  : Shield Bash")
        print("Effect          : Deals damage and increases DEF by 1")

    else:

        print("Special Attack  : Special Attack")
        print("Effect          : Deals bonus damage")


def show_extra_stats(player):

    if player.name == "Rogue":

        print(f"Crit Rate       : {player.crit_rate}")
        print(f"Dodge           : {player.dodge}")

    elif player.name == "Warrior":

        print(f"Strength        : {player.strength}")
        print(f"Rage            : {player.rage}")

    elif player.name == "Knight":

        print(f"Shield Block    : {player.shield_block}")
        print(f"Endurance       : {player.endurance}")


def show_player_start_summary(player):

    line()
    print("                    ADVENTURE BEGINS")
    line()

    print(f"\nClass Chosen : {player.name}")

    print("\nStarting Stats")
    small_line()
    print(f"HP              : {player.hp}/{player.max_hp}")
    print(f"Attack          : {player.attack}")
    print(f"Defense         : {player.defense}")
    print(f"Level           : {player.level}")
    print(f"EXP             : {player.get_exp_info()}")
    print(f"Gold            : {player.gold}")

    print("\nClass Stats")
    small_line()
    show_extra_stats(player)

    print("\nClass Ability")
    small_line()
    show_special_attack_info(player)

    print("\nStarter Item")
    small_line()
    print("Healing Potion added to inventory.")

    line()

    pause()


def give_starter_item(player):

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


def start_game():

    choice = show_character_selection()

    if choice == "1":

        player = create_player("Rogue")

    elif choice == "2":

        player = create_player("Warrior")

    elif choice == "3":

        player = create_player("Knight")

    else:

        print("Invalid choice. Defaulting to Rogue.")
        pause()

        player = create_player("Rogue")

    give_starter_item(player)

    show_player_start_summary(player)

    run_game_loop(player)


def show_gameplay_menu(player):

    line()
    print("                     GAMEPLAY MENU")
    line()

    print(f"Class           : {player.name}")
    print(f"HP              : {player.hp}/{player.max_hp}")
    print(f"Attack          : {player.attack}")
    print(f"Defense         : {player.defense}")
    print(f"Level           : {player.level}")
    print(f"EXP             : {player.get_exp_info()}")
    print(f"Gold            : {player.gold}")
    print(f"Path            : {player.path_level}")

    if hasattr(player, "current_floor"):
        print(f"Floor           : {player.current_floor}")

    if hasattr(player, "current_location"):
        print(f"Room            : {player.current_location}")

    print()
    small_line()
    show_special_attack_info(player)
    small_line()

    print("[1] Explore Dungeon")
    print("[2] Check Inventory")
    print("[3] Return to Main Menu")

    line()

    action = input("Choose an action: ").strip()
    clear_screen()

    return action


def run_game_loop(player):

    while True:

        clear_screen()

        action = show_gameplay_menu(player)

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
            pause()
            break

        else:

            print("Invalid choice. Try again.")
            pause()