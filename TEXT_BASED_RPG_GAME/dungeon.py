import random

from .enemy import (
    OrdinaryEnemy,
    BossEnemy,
    ENEMY_MODS,
    BOSS_MODS
)

from .combat import TurnBasedCombat
from .events import RandomEvents
from .logger import Logger
from .utils import clear_screen
from .leaderboard import save_score, calculate_score
from .movement import MovementCycle


logger = Logger(delay=0.02)


# ==============================
# UI HELPERS
# ==============================

def line(length=52):
    print("=" * length)


def small_line(length=52):
    print("-" * length)


def hp_bar(current, maximum, length=18):

    if maximum <= 0:
        maximum = 1

    filled = int((current / maximum) * length)

    if filled < 0:
        filled = 0

    if filled > length:
        filled = length

    empty = length - filled

    return "[" + ("█" * filled) + (" " * empty) + "]"


def show_header(title):

    line()
    print(title.center(52))
    line()


def show_subheader(title):

    print()
    small_line()
    print(title.center(52))
    small_line()


def wait_for_event():

    input("\nPress Enter to continue...")
    clear_screen()


# ==============================
# PATH GENERATION
# ==============================

def generate_path_states():

    path_states = {
        "Left": random.choice(["OPEN", "BLOCKED"]),
        "Center": random.choice(["OPEN", "BLOCKED"]),
        "Right": random.choice(["OPEN", "BLOCKED"])
    }

    if not any(
        state == "OPEN"
        for state in path_states.values()
    ):

        forced_path = random.choice(
            list(path_states.keys())
        )

        path_states[forced_path] = "OPEN"

    return path_states


# ==============================
# ENEMY CREATION
# ==============================

def create_random_enemy(player):

    enemy_level = max(
        1,
        player.level + random.randint(-1, 1)
    )

    enemy_name = random.choice(
        list(ENEMY_MODS.keys())
    )

    return OrdinaryEnemy(
        name=enemy_name,
        level=enemy_level
    )


def create_random_boss(player):

    boss_level = max(
        1,
        player.level + 1
    )

    boss_name = random.choice(
        list(BOSS_MODS.keys())
    )

    return BossEnemy(
        name=boss_name,
        level=boss_level
    )


# ==============================
# PLAYER DISPLAY
# ==============================

def get_required_exp(player):

    if hasattr(player, "required_exp_to_level"):
        return player.required_exp_to_level()

    return 100 + ((player.level - 1) * 50)


def show_player_status(player):

    required_exp = get_required_exp(player)

    show_subheader("PLAYER STATUS")

    print(f"Class : {player.name}")
    print(
        f"HP    : {player.hp}/{player.max_hp} "
        f"{hp_bar(player.hp, player.max_hp)}"
    )
    print(f"Level : {player.level}")
    print(f"EXP   : {player.exp}/{required_exp}")
    print(f"Gold  : {player.gold}")


def show_location_status(player, movement):

    show_subheader("CURRENT LOCATION")

    print(f"Floor : {player.current_floor} - {movement.get_floor_name()}")
    print(f"Path  : {player.current_path}/10")
    print(f"Room  : {player.current_location}")


def show_paths(path_states):

    show_subheader("AVAILABLE PATHS")

    path_names = list(path_states.keys())

    for i, path in enumerate(path_names, 1):

        state = path_states[path]

        if state == "OPEN":
            marker = "OPEN"
        else:
            marker = "BLOCKED"

        print(f"[{i}] {path:<8} : {marker}")

    return path_names


def show_commands():

    show_subheader("COMMANDS")

    print("[BAG]        Open Inventory")
    print("[SURRENDER]  End Run")


# ==============================
# GAME OVER SCREEN
# ==============================

def show_game_over_screen(player, reason):

    clear_screen()

    total_score = calculate_score(player)

    path_score = player.path_level * 100
    level_score = player.level * 50
    exp_score = player.exp
    gold_score = player.gold * 2

    line(60)
    print("GAME OVER".center(60))
    line(60)

    print(f"\nReason: {reason}")

    print()
    small_line(60)
    print("RUN SUMMARY".center(60))
    small_line(60)

    print(f"Class        : {player.name}")
    print(f"Path Reached : {player.path_level}")

    if hasattr(player, "current_floor"):
        print(f"Floor        : {player.current_floor}")

    if hasattr(player, "current_path"):
        print(f"Current Path : {player.current_path}/10")

    if hasattr(player, "current_location"):
        print(f"Room         : {player.current_location}")

    print(f"Level        : {player.level}")
    print(f"EXP          : {player.exp}")
    print(f"Gold         : {player.gold}")

    print()
    small_line(60)
    print("SCORE BREAKDOWN".center(60))
    small_line(60)

    print(f"Path Score   : {path_score}")
    print(f"Level Score  : {level_score}")
    print(f"EXP Score    : {exp_score}")
    print(f"Gold Score   : {gold_score}")

    line(60)
    print(f"TOTAL SCORE  : {total_score}")
    line(60)

    save_score(player)

    print("\nYour score has been saved.")

    input("\nPress Enter to return to Main Menu...")
    clear_screen()


# ==============================
# MOVEMENT SETUP
# ==============================

def setup_movement(player):

    if not hasattr(player, "movement"):
        player.movement = MovementCycle()

    player.movement.sync_with_player_path(
        player.path_level,
        player
    )


# ==============================
# DUNGEON EXPLORATION
# ==============================

def explore_dungeon(player):

    if not hasattr(player, "path_level"):
        player.path_level = 1

    setup_movement(player)

    movement = player.movement

    path_states = generate_path_states()

    while True:

        movement.sync_with_player_path(
            player.path_level,
            player
        )

        show_header("DUNGEON EXPLORATION")

        show_location_status(
            player,
            movement
        )

        show_player_status(player)

        path_names = show_paths(path_states)

        show_commands()

        line()
        choice = input("Choose path or command: ").strip().upper()
        clear_screen()

        # ==============================
        # INVENTORY
        # ==============================

        if choice == "BAG":

            player.inventory.inventory_menu(player)
            continue

        # ==============================
        # SURRENDER
        # ==============================

        if choice == "SURRENDER":

            show_header("SURRENDER RUN")

            confirm = input("Are you sure? (YES/NO): ").strip().upper()

            clear_screen()

            if confirm == "YES":

                logger.loading("Ending run")

                show_game_over_screen(
                    player,
                    "You surrendered."
                )

                return False

            print("Surrender cancelled.")
            continue

        # ==============================
        # PATH SELECTION
        # ==============================

        if choice in ["1", "2", "3"]:

            selected = path_names[int(choice) - 1]

            if path_states[selected] == "BLOCKED":

                show_header("BLOCKED PATH")

                logger.typewriter(
                    f"The {selected} path is blocked."
                )

                continue

            movement.move_path(
                selected,
                player.path_level,
                player
            )

            logger.log(
                f"\n{player.name} enters the "
                f"{selected} path..."
            )

            logger.log(
                f"Floor {player.current_floor} - "
                f"{movement.get_floor_name()}"
            )

            logger.log(
                f"Path {player.current_path}/10"
            )

            logger.log(
                f"Room: {player.current_location}"
            )

            logger.log(
                movement.get_room_flavor()
            )

            logger.display_buffer()

            logger.loading("Exploring")

            result = encounter(player)

            if result == "dead":

                show_game_over_screen(
                    player,
                    "You were defeated."
                )

                return False

            player.path_level += 1

            floor_changed = movement.sync_with_player_path(
                player.path_level,
                player
            )

            if floor_changed:

                show_header("NEW FLOOR")

                logger.log("The dungeon shifts violently.")
                logger.log(
                    f"You descend into Floor "
                    f"{player.current_floor}."
                )

                logger.log(
                    f"Section: {movement.get_floor_name()}"
                )

                logger.log(
                    f"Path reset to {player.current_path}/10."
                )

                logger.display_buffer()

            path_states = generate_path_states()

            continue

        show_header("INVALID INPUT")
        print("Please choose 1, 2, 3, BAG, or SURRENDER.")


# ==============================
# ENCOUNTERS
# ==============================

def encounter(player):

    if player.current_path == 10:

        boss = create_random_boss(player)

        show_header("BOSS ENCOUNTER")

        logger.log("The dungeon trembles...")
        logger.log("A powerful enemy blocks your path!")

        logger.log(
            f"{boss.name} "
            f"(Lv {boss.level}) appears!"
        )

        logger.log("Boss combat begins.")
        logger.display_buffer()

        input("\nPress Enter to enter combat...")
        clear_screen()

        combat = TurnBasedCombat(
            player,
            boss
        )

        result = combat.start_combat()

        if result == "dead":
            return "dead"

        return "continue"

    roll = random.random()

    if roll < 0.4:

        enemy = create_random_enemy(player)

        show_header("ENEMY ENCOUNTER")

        logger.log(
            f"A {enemy.name} "
            f"(Lv {enemy.level}) appears!"
        )

        logger.log("Combat begins.")
        logger.display_buffer()

        input("\nPress Enter to enter combat...")
        clear_screen()

        combat = TurnBasedCombat(
            player,
            enemy
        )

        result = combat.start_combat()

        if result == "dead":
            return "dead"

        return "continue"

    elif roll < 0.7:

        show_header("RANDOM EVENT")

        logger.log("Something unusual happens...")
        logger.log("A random event has been triggered.")
        logger.display_buffer()

        RandomEvents().trigger_event(player)

        if not player.is_alive():
            return "dead"

        wait_for_event()

        return "continue"

    else:

        show_header("EMPTY AREA")

        logger.loading("Searching the area")
        print("Nothing happens...")
        logger.loading("")
        clear_screen()

        return "continue"