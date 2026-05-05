import random
from events import RandomEvents   # <-- import your event system
from enemy import OrdinaryEnemy
from combat import TurnBasedCombat


def explore_dungeon(player):
    print("\n=== Dungeo Exploration ===")
    paths = ["Left", "Center", "Right"]
    random.shuffle(paths)

    print("Available paths:")
    for idx, path in enumerate(paths, start=1):
        print(f"{idx}. {path}")
    print("4. Exit Dungeon")

    choice = input("Choose a path to explore (1-4): ").strip()

    if choice in ["1", "2", "3"]:
        chosen_path = paths[int(choice) - 1]
        print(f"{player.name} takes the chosen {chosen_path} path...")
        # Placeholder: encounter logic
        encounter(player)
    else:
        print("Invalid choice. Returning to gameplay menu.")    


def encounter(player):
    # Placeholder for encounter logic
    print(f"{player.name} encounters a mysterious enemy (combat placeholder).")
    # Call combat(player) here when implemented later