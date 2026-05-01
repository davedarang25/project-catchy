# leaderboard.py

# For now, we'll just use a simple list to simulate scores.
# Later you can replace this with file storage or a database.
scores = []

def show_leaderboard():
    print("\n=== Leaderboard ===")

    if not scores:
        print("No Result")
    else:
        # Sort scores from highest to lowest
        sorted_scores = sorted(scores, reverse=True)
        for idx, score in enumerate(sorted_scores, start=1):
            print(f"{idx}. {score}")

    # Allow player to exit leaderboard
    choice = input("\nExit Leaderboard? (y/n): ").strip().lower()
    if choice == "y":
        print("Returning to Main Menu...")
    else:
        show_leaderboard()  # Loop until they choose to exit
