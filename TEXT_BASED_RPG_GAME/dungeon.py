# dungeon.py
import random
from events import RandomEvents   # <-- import your event system
from enemy import OrdinaryEnemy
from combat import TurnBasedCombat


def explore_dungeon(player):
    
    print("\n=== Dungeon Exploration ===")

    paths = ["Left", "Center", "Right"]
    random.shuffle(paths)

    print("Available paths:")
    for idx, path in enumerate(paths, start=1):
        print(f"{idx}. {path}")

    choice = input("Choose a path to explore (1-3): ").strip()

    if choice in ["1", "2", "3"]:
        chosen_path = paths[int(choice) - 1]
        print(f"{player.name} takes the {chosen_path} path...")

        # After moving, trigger what happens next
        encounter(player)

    else:
        print("Invalid choice. Returning to gameplay menu.")


def encounter(player):
    roll = random.random()
    print("DEBUG: encounter function started")

    # 40% chance → enemy
    if roll < 0.4:
        print("\nAn enemy appears!")

        enemy = OrdinaryEnemy("Goblin", level=1)

        combat = TurnBasedCombat(player, enemy)
        result = combat.start_combat()
        if result == "menu":
            return

    # 30% chance → random event
    elif roll < 0.7:
        print("\nA random event occurs!")
        print("DEBUG: before trigger_event")

        event_system = RandomEvents()
        event_system.trigger_event(player)

        print("DEBUG: after trigger_event")
    # 30% chance → nothing
    else:
        print("\nThe area is quiet... nothing happens.")


"""import random

ALL_PATHS = ["Left", "Center", "Right"]

def explore_dungeon(player):
    print("\n=== Dungeon Exploration ===")

    # Randomly decide which paths are available (1–3)
    available_count = random.randint(1, 3)
    available_paths = random.sample(ALL_PATHS, k=available_count)

    # Fixed display order
    fixed_menu = {
        "1": "Left",
        "2": "Center",
        "3": "Right"
    }

    print("Available paths:")
    for num, path in fixed_menu.items():
        status = "OPEN" if path in available_paths else "BLOCKED"
        print(f"{num}. {path} [{status}]")

    choice = input("Choose a path (1-3): ").strip()

    if choice not in fixed_menu:
        print("Invalid input. You remain in the dungeon.")
        return

    chosen_path = fixed_menu[choice]

    if chosen_path not in available_paths:
        print("The path is blocked. You return to your current position.")
        return

    print(f"{player.name} takes the {chosen_path} path...")
    encounter(player)


def encounter(player):
    print(f"{player.name} encounters a mysterious enemy (combat placeholder).")"""