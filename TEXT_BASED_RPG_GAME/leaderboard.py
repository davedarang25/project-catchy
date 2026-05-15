# leaderboard.py

try:
    from .utils import clear_screen
except ImportError:
    from utils import clear_screen


SCORE_FILE = "leaderboard.txt"


def calculate_score(player):
    path_score = player.path_level * 100
    level_score = player.level * 50
    exp_score = player.exp
    gold_score = player.gold * 2

    total_score = (
        path_score
        + level_score
        + exp_score
        + gold_score
    )

    return total_score


def save_score(player):
    score = calculate_score(player)

    with open(SCORE_FILE, "a") as file:
        file.write(
            f"{player.name}|"
            f"{score}|"
            f"{player.path_level}|"
            f"{player.level}|"
            f"{player.exp}|"
            f"{player.gold}\n"
        )


def load_scores():
    scores = []

    try:
        with open(SCORE_FILE, "r") as file:

            for line in file:
                data = line.strip().split("|")

                if len(data) == 6:

                    name = data[0]
                    score = int(data[1])
                    path_level = int(data[2])
                    level = int(data[3])
                    exp = int(data[4])
                    gold = int(data[5])

                    scores.append({
                        "name": name,
                        "score": score,
                        "path_level": path_level,
                        "level": level,
                        "exp": exp,
                        "gold": gold
                    })

    except FileNotFoundError:
        pass

    return scores


def show_leaderboard():
    while True:

        clear_screen()

        print("\n=== Leaderboard ===")

        scores = load_scores()

        if not scores:

            print("No Result")

        else:

            sorted_scores = sorted(
                scores,
                key=lambda entry: entry["score"],
                reverse=True
            )

            for idx, entry in enumerate(sorted_scores, start=1):

                print(
                    f"{idx}. {entry['name']} | "
                    f"Score: {entry['score']} | "
                    f"Path: {entry['path_level']} | "
                    f"Level: {entry['level']} | "
                    f"EXP: {entry['exp']} | "
                    f"Gold: {entry['gold']}"
                )

        choice = input("\nExit Leaderboard? (y/n): ").strip().lower()

        if choice == "y":

            print("Returning to Main Menu...")
            break