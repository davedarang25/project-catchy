# gameplay py
def start_game():
    print("\n=== Starting New Game ===")
    print("Choose your character class:")
    print("1. Rogue")
    print("2. Warrior")
    print("3. Knight")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("You chose Rogue. Let the adventure begin!")
    elif choice == "2":
        print("You chose Warrior. Let the adventure begin!")
    elif choice == "3":
        print("You chose Knight. Let the adventure begin!")
    else:
        print("Invalid choice. Starting with default character (Rogue)>")
        print("You chose Rogue. Let the adventure begin!")

    # Later you can expand this into the full game loop