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
from .leaderboard import save_score


logger = Logger(delay=0.02)


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


def explore_dungeon(player):

    if not hasattr(player, "path_level"):
        player.path_level = 1

    path_states = generate_path_states()

    while True:

        print("\n" + "=" * 30)
        print(f"        PATH {player.path_level}")
        print("=" * 30)

        print(f"HP: {player.hp}/{player.max_hp}")
        print(f"Gold: {player.gold}")
        print(f"EXP: {player.get_exp_info()}")
        print(f"Level: {player.level}")

        print("\nAvailable Paths:")

        path_names = list(path_states.keys())

        for i, path in enumerate(path_names, 1):
            print(f"{i}. {path} [{path_states[path]}]")

        print("\nBAG = Inventory")
        print("SURRENDER = Quit Run")

        choice = input("\nChoose path (1-3): ").strip().upper()

        clear_screen()

        if choice == "BAG":

            player.inventory.inventory_menu(player)
            continue

        if choice == "SURRENDER":

            confirm = input("Are you sure? (YES/NO): ").strip().upper()

            clear_screen()

            if confirm == "YES":

                logger.loading("Ending run")

                save_score(player)

                print("GAME OVER")
                print("Your score has been saved.")

                return False

            print("Surrender cancelled.")
            continue

        if choice in ["1", "2", "3"]:

            selected = path_names[int(choice) - 1]

            if path_states[selected] == "BLOCKED":

                logger.typewriter(
                    f"The {selected} path is blocked."
                )

                continue

            logger.log(
                f"\n{player.name} enters "
                f"the {selected} path..."
            )

            logger.log(
                "The darkness shifts around you."
            )

            logger.display_buffer()

            logger.loading("Exploring")

            result = encounter(player)

            if result == "dead":

                save_score(player)

                print("Your score has been saved.")

                return False

            player.path_level += 1

            path_states = generate_path_states()

            continue

        print("Invalid input.")


def encounter(player):

    if player.path_level % 10 == 0:

        boss = create_random_boss(player)

        logger.log("\nThe dungeon trembles...")
        logger.log("A powerful enemy blocks your path!")

        logger.log(
            f"{boss.name} "
            f"(Lv {boss.level}) appears!"
        )

        logger.log("Boss combat begins.")
        logger.display_buffer()

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

        logger.log(
            f"\nA {enemy.name} "
            f"(Lv {enemy.level}) appears!"
        )

        logger.log("Combat begins.")
        logger.display_buffer()

        combat = TurnBasedCombat(
            player,
            enemy
        )

        result = combat.start_combat()

        if result == "dead":
            return "dead"

        return "continue"

    elif roll < 0.7:

        logger.log("\nSomething unusual happens...")
        logger.log("A random event has been triggered.")
        logger.display_buffer()

        RandomEvents().trigger_event(player)

        if not player.is_alive():

            print("\nYou died from the event.")
            print("GAME OVER")

            return "dead"

        return "continue"

    else:

        logger.loading("Searching the area")
        print("Nothing happens...")

        return "continue"