# leveling.py


def get_required_exp(level):
    return 100 + ((level - 1) * 50)


def get_exp_needed(player):
    required_exp = get_required_exp(player.level)
    needed = required_exp - player.exp

    if needed < 0:
        needed = 0

    return needed


def get_exp_info(player):
    required_exp = get_required_exp(player.level)
    needed = get_exp_needed(player)

    return (
        f"{player.exp}/{required_exp} EXP | "
        f"Needed: {needed} EXP"
    )


def get_level_growth(player):
    class_name = player.name

    if class_name == "Rogue":
        return {
            "hp": 15,
            "attack": 4,
            "defense": 1
        }

    elif class_name == "Warrior":
        return {
            "hp": 25,
            "attack": 3,
            "defense": 2
        }

    elif class_name == "Knight":
        return {
            "hp": 30,
            "attack": 2,
            "defense": 3
        }

    return {
        "hp": 20,
        "attack": 3,
        "defense": 2
    }


def gain_exp(player, amount):
    if amount <= 0:
        print("No EXP gained.")
        return

    player.exp += amount

    print(f"Gained {amount} EXP.")

    check_level_up(player)

    print(f"EXP: {get_exp_info(player)}")


def check_level_up(player):
    leveled_up = False

    while player.exp >= get_required_exp(player.level):

        required_exp = get_required_exp(player.level)

        player.exp -= required_exp
        player.level += 1

        increase_stats(player)

        leveled_up = True

    if leveled_up:
        print(f"Next Level: {get_exp_info(player)}")


def increase_stats(player):
    growth = get_level_growth(player)

    hp_gain = growth["hp"]
    attack_gain = growth["attack"]
    defense_gain = growth["defense"]

    player.max_hp += hp_gain
    player.hp = player.max_hp

    player.attack += attack_gain
    player.defense += defense_gain

    print("\n" + "=" * 30)
    print("          LEVEL UP!")
    print("=" * 30)
    print(f"{player.name} reached Level {player.level}!")
    print(f"Max HP +{hp_gain}")
    print(f"Attack +{attack_gain}")
    print(f"Defense +{defense_gain}")
    print("HP fully restored.")
    print("=" * 30)