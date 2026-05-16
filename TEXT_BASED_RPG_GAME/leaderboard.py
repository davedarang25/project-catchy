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


def save_score(player, player_name=None):

    score = calculate_score(player)

    if player_name is None:
        player_name = player.name

    class_name = player.name

    floor_number = getattr(player, "current_floor", 1)
    path_number = getattr(player, "current_path", player.path_level)

    with open(SCORE_FILE, "a") as file:
        file.write(
            f"{player_name}|"
            f"{class_name}|"
            f"{score}|"
            f"{player.path_level}|"
            f"{floor_number}|"
            f"{path_number}|"
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

                # New format:
                # name|class|score|path_reached|floor|path_number|level|exp|gold
                if len(data) == 9:

                    name = data[0]
                    class_name = data[1]
                    score = int(data[2])
                    path_reached = int(data[3])
                    floor_number = int(data[4])
                    path_number = int(data[5])
                    level = int(data[6])
                    exp = int(data[7])
                    gold = int(data[8])

                    scores.append({
                        "name": name,
                        "class": class_name,
                        "score": score,
                        "path_reached": path_reached,
                        "floor": floor_number,
                        "path_number": path_number,
                        "level": level,
                        "exp": exp,
                        "gold": gold
                    })

                # Old format:
                # name|class|score|path|level|exp|gold
                elif len(data) == 7:

                    name = data[0]
                    class_name = data[1]
                    score = int(data[2])
                    path_reached = int(data[3])
                    level = int(data[4])
                    exp = int(data[5])
                    gold = int(data[6])

                    floor_number = ((path_reached - 1) // 10) + 1
                    path_number = ((path_reached - 1) % 10) + 1

                    scores.append({
                        "name": name,
                        "class": class_name,
                        "score": score,
                        "path_reached": path_reached,
                        "floor": floor_number,
                        "path_number": path_number,
                        "level": level,
                        "exp": exp,
                        "gold": gold
                    })

                # Older format:
                # name|score|path|level|exp|gold
                elif len(data) == 6:

                    name = data[0]
                    score = int(data[1])
                    path_reached = int(data[2])
                    level = int(data[3])
                    exp = int(data[4])
                    gold = int(data[5])

                    floor_number = ((path_reached - 1) // 10) + 1
                    path_number = ((path_reached - 1) % 10) + 1

                    scores.append({
                        "name": name,
                        "class": "Unknown",
                        "score": score,
                        "path_reached": path_reached,
                        "floor": floor_number,
                        "path_number": path_number,
                        "level": level,
                        "exp": exp,
                        "gold": gold
                    })

    except FileNotFoundError:
        pass

    return scores


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