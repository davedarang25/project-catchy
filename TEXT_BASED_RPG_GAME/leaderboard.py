import json

from .utils import clear_screen


SCORE_FILE = "leaderboard.json"


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


def save_score(player, player_name=None):

    score = calculate_score(player)

    if player_name is None:
        player_name = player.name

    class_name = player.name

    floor_number = getattr(player, "current_floor", 1)
    path_number = getattr(player, "current_path", player.path_level)

    new_entry = {
        "name": player_name,
        "class": class_name,
        "score": score,
        "path_reached": player.path_level,
        "floor": floor_number,
        "path_number": path_number,
        "level": player.level,
        "exp": player.exp,
        "gold": player.gold
    }

    scores = load_scores()
    scores.append(new_entry)

    with open(SCORE_FILE, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4)


def load_scores():

    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as file:
            scores = json.load(file)

            if isinstance(scores, list):
                return scores

    except FileNotFoundError:
        pass

    except json.JSONDecodeError:
        pass

    return []


def display_scores(scores, show_all=False):

    sorted_scores = sorted(
        scores,
        key=lambda entry: entry["score"],
        reverse=True
    )

    if show_all:
        shown_scores = sorted_scores
        title = "ALL RUNS"
    else:
        shown_scores = sorted_scores[:10]
        title = "TOP 10 RUNS"

    print("\n" + "-" * 105)
    print(title.center(105))
    print("-" * 105)

    print(
        f"{'Rank':<6}"
        f"{'Name':<12}"
        f"{'Class':<12}"
        f"{'Score':<10}"
        f"{'Floor':<8}"
        f"{'Path':<8}"
        f"{'Reached':<10}"
        f"{'Level':<8}"
        f"{'EXP':<10}"
        f"{'Gold':<8}"
    )

    print("-" * 105)

    for idx, entry in enumerate(shown_scores, start=1):

        print(
            f"{idx:<6}"
            f"{entry['name']:<12}"
            f"{entry['class']:<12}"
            f"{entry['score']:<10}"
            f"{entry['floor']:<8}"
            f"{str(entry['path_number']) + '/10':<8}"
            f"{entry['path_reached']:<10}"
            f"{entry['level']:<8}"
            f"{entry['exp']:<10}"
            f"{entry['gold']:<8}"
        )

    print("-" * 105)


def show_leaderboard():

    show_all = False

    while True:

        clear_screen()

        print("\n" + "=" * 105)
        print("LEADERBOARD".center(105))
        print("=" * 105)

        scores = load_scores()

        if not scores:

            print("\nNo Result")
            print("\nPlay a run first to save your score.")

        else:

            display_scores(
                scores,
                show_all
            )

        print("\nOptions:")
        print("1. Show Top 10")
        print("2. Show All")
        print("3. Return to Main Menu")
        print("=" * 105)

        choice = input("Choose: ").strip()

        if choice == "1":

            show_all = False

        elif choice == "2":

            show_all = True

        elif choice == "3":

            clear_screen()
            print("Returning to Main Menu...")
            break

        else:

            print("Invalid choice.")
            input("Press Enter to continue...")
