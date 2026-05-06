import random
from enemy import Slime, Goblin, Skeleton  # Import the specific entities
from combat import TurnBasedCombat
from events import RandomEvents

def explore_dungeon(player):
    print("\n" + "="*25)
    print("   DUNGEON EXPLORATION   ")
    print("="*25)

    paths = ["Left", "Center", "Right"]
    random.shuffle(paths)

    print("Available paths:")
    for idx, path in enumerate(paths, start=1):
        print(f"{idx}. {path}")

    choice = input("Choose a path to explore (1-3): ").strip()

    if choice in ["1", "2", "3"]:
        chosen_path = paths[int(choice) - 1]
        print(f"\n{player.name} cautiously walks down the {chosen_path} path...")
        encounter(player)
    else:
        print("Invalid choice. You stay put, wary of the shadows.")

def encounter(player):
    roll = random.random()
    
    # 40% chance → Enemy Encounter
    if roll < 0.4:
        # Determine enemy level based on player level (with a little variance)
        enemy_level = max(1, player.level + random.randint(-1, 1))
        
        # Pick a random enemy class from your module
        enemy_pool = [Slime, Goblin, Skeleton]
        chosen_class = random.choice(enemy_pool)
        
        # Instantiate the enemy
        enemy = chosen_class(level=enemy_level)
        
        print(f"\n*** A wild {enemy.name} (Lv. {enemy.level}) appears! ***")
        print(enemy.get_info())

        # Start the combat loop
        combat = TurnBasedCombat(player, enemy)
        combat.start_combat()

    # 30% chance → Random Event (Traps, Shrines, etc.)
    elif roll < 0.7:
        event_system = RandomEvents()
        event_system.trigger_event(player)

    # 30% chance → Nothing happens
    else:
        print("\nThe corridor is eerily silent. You find nothing but dust.")