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

    return f"{player.exp}/{required_exp} EXP | Needed: {needed} EXP"


def gain_exp(player, amount):
    player.exp += amount

    print(f"Gained {amount} EXP.")

    check_level_up(player)


def check_level_up(player):
    while player.exp >= get_required_exp(player.level):

        required_exp = get_required_exp(player.level)

        player.exp -= required_exp
        player.level += 1

        increase_stats(player)


def increase_stats(player):
    hp_gain = 20
    attack_gain = 3
    defense_gain = 2

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
    print("=" * 30)