import random

def explore_dungeon(player):
    while True:  # <-- dungeon loop
        print("\n=== Dungeon Exploration ===")
        paths = ["Left", "Center", "Right"]
        random.shuffle(paths)

        print("Available paths:")
        for idx, path in enumerate(paths, start=1):
            print(f"{idx}. {path}")
        print("4. Exit Dungeon")

        choice = input("Choose a path to explore (1-4): ").strip()

        if choice in ["1", "2", "3"]:
            chosen_path = paths[int(choice) - 1]
            print(f"{player.name} takes the {chosen_path} path...")
            encounter(player)
        elif choice == "4":
            print("Leaving the dungeon...")
            break   # <-- return to gameplay menu
        else:
            print("Invalid choice. Try again.")    

def encounter(player):
    # Placeholder for encounter logic
    print(f"{player.name} encounters a mysterious enemy (combat placeholder).")
    # Later: call combat(player) here
