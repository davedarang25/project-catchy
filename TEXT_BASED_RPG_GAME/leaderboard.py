from .utils import clear_screen


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

        print("\n" + "=" * 60)
        print("                      LEADERBOARD")
        print("=" * 60)

        scores = load_scores()

        if not scores:

            print("\nNo Result")
            print("\nPlay a run first to save your score.")

        else:

            sorted_scores = sorted(
                scores,
                key=lambda entry: entry["score"],
                reverse=True
            )

            top_scores = sorted_scores[:10]

            print("\nTop 10 Runs")
            print("-" * 60)

            print(
                f"{'Rank':<6}"
                f"{'Class':<12}"
                f"{'Score':<10}"
                f"{'Path':<8}"
                f"{'Level':<8}"
                f"{'EXP':<8}"
                f"{'Gold':<8}"
            )

            print("-" * 60)

            for idx, entry in enumerate(top_scores, start=1):

                print(
                    f"{idx:<6}"
                    f"{entry['name']:<12}"
                    f"{entry['score']:<10}"
                    f"{entry['path_level']:<8}"
                    f"{entry['level']:<8}"
                    f"{entry['exp']:<8}"
                    f"{entry['gold']:<8}"
                )

            print("-" * 60)

        print("\n1. Return to Main Menu")
        print("=" * 60)

        choice = input("Choose: ").strip()

        if choice == "1":

            clear_screen()
            print("Returning to Main Menu...")
            break

        else:

            print("Invalid choice.")
            input("Press Enter to continue...")