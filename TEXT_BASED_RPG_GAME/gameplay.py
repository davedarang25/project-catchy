# gamplay py
from character import Rogue, Warrior, Knight

def start_game():
    print("\n=== Character Selection ===")
    print("Choose your character: ")
    print("1. Rogue")
    print("2. Warrior")
    print("3. Knight")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        player = Rogue("You've choose as a Rogue, a nimble and stealthy character with agility and cunning.")
    elif choice == "2":
        player = Warrior("You've choose as a Warrior, a strong and resilient character with high health and powerful attacks.")
    elif choice == "3":
        player = Knight("You've choose as a Knight, a heavily armoured character with balanced stats and strong defense.")
    else:
        print("Invalid choice. You will be assigned as a Rogue by default.")
        player = Rogue("You've choose as a Rogue, a nimble and stealthy character with agility and cunning.")

    print(f"\nYou have chosen {player.name}. Let the adventure begin!")

    # Enter gameplay loop
    run_game_loop(player)

def run_game_loop(player):
    while True:
        print("\n=== Gameplay Menu ===")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Return to main menu")

        action = input("Enter your action: ").strip()

        if action == "1":
            print(f"{player.name} explores the dungeon... (placeholder)")
            # later call dungeo logic
        elif action == "2":
            print(f"{player.name} checks inventory... (placeholder)")
        elif action == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
            