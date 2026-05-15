import random

from .character import Character

from .item import (
    random_drop,
    SLIME_DROPS,
    GOBLIN_DROPS,
    SKELETON_DROPS,
    BAT_DROPS,
    SPIDER_DROPS,
    WOLF_DROPS,
    ZOMBIE_DROPS,
    ORC_DROPS,
    DARK_MAGE_DROPS,
    BANDIT_DROPS,
    GIANT_RAT_DROPS,
    TROLL_DROPS,
    WRAITH_DROPS,
    LIZARDMAN_DROPS,
    HARPY_DROPS,
    GOBLIN_KING_DROPS,
    SKELETON_LORD_DROPS,
    SLIME_MONARCH_DROPS,
    ORC_WARLORD_DROPS,
    ANCIENT_WRAITH_DROPS
)


ENEMY_MODS = {
    "Slime": {
        "hp_bonus": 15,
        "attack_bonus": -2,
        "defense_bonus": 0,
        "exp_bonus": 0,
        "gold_bonus": 0
    },

    "Goblin": {
        "hp_bonus": 0,
        "attack_bonus": 0,
        "defense_bonus": 0,
        "exp_bonus": 0,
        "gold_bonus": 5
    },

    "Skeleton": {
        "hp_bonus": -10,
        "attack_bonus": 4,
        "defense_bonus": 0,
        "exp_bonus": 0,
        "gold_bonus": 0
    },

    "Bat": {
        "hp_bonus": -15,
        "attack_bonus": 3,
        "defense_bonus": -1,
        "exp_bonus": 5,
        "gold_bonus": 2
    },

    "Spider": {
        "hp_bonus": 5,
        "attack_bonus": 2,
        "defense_bonus": 1,
        "exp_bonus": 8,
        "gold_bonus": 3
    },

    "Wolf": {
        "hp_bonus": 10,
        "attack_bonus": 5,
        "defense_bonus": 0,
        "exp_bonus": 12,
        "gold_bonus": 5
    },

    "Zombie": {
        "hp_bonus": 25,
        "attack_bonus": 1,
        "defense_bonus": 2,
        "exp_bonus": 10,
        "gold_bonus": 4
    },

    "Orc": {
        "hp_bonus": 30,
        "attack_bonus": 6,
        "defense_bonus": 2,
        "exp_bonus": 18,
        "gold_bonus": 10
    },

    "Dark Mage": {
        "hp_bonus": -5,
        "attack_bonus": 8,
        "defense_bonus": -1,
        "exp_bonus": 20,
        "gold_bonus": 12
    },

    "Bandit": {
        "hp_bonus": 5,
        "attack_bonus": 4,
        "defense_bonus": 1,
        "exp_bonus": 12,
        "gold_bonus": 15
    },

    "Giant Rat": {
        "hp_bonus": -12,
        "attack_bonus": 2,
        "defense_bonus": -1,
        "exp_bonus": 6,
        "gold_bonus": 2
    },

    "Troll": {
        "hp_bonus": 45,
        "attack_bonus": 5,
        "defense_bonus": 4,
        "exp_bonus": 25,
        "gold_bonus": 12
    },

    "Wraith": {
        "hp_bonus": -5,
        "attack_bonus": 7,
        "defense_bonus": 3,
        "exp_bonus": 22,
        "gold_bonus": 10
    },

    "Lizardman": {
        "hp_bonus": 18,
        "attack_bonus": 4,
        "defense_bonus": 3,
        "exp_bonus": 16,
        "gold_bonus": 8
    },

    "Harpy": {
        "hp_bonus": -8,
        "attack_bonus": 6,
        "defense_bonus": 0,
        "exp_bonus": 17,
        "gold_bonus": 9
    }
}


BOSS_MODS = {
    "Goblin King": {
        "hp_bonus": 20,
        "attack_bonus": 3,
        "defense_bonus": 1,
        "exp_bonus": 25,
        "gold_bonus": 25
    },

    "Skeleton Lord": {
        "hp_bonus": 10,
        "attack_bonus": 5,
        "defense_bonus": 2,
        "exp_bonus": 35,
        "gold_bonus": 30
    },

    "Slime Monarch": {
        "hp_bonus": 35,
        "attack_bonus": 2,
        "defense_bonus": 3,
        "exp_bonus": 30,
        "gold_bonus": 25
    },

    "Orc Warlord": {
        "hp_bonus": 45,
        "attack_bonus": 7,
        "defense_bonus": 4,
        "exp_bonus": 45,
        "gold_bonus": 40
    },

    "Ancient Wraith": {
        "hp_bonus": 25,
        "attack_bonus": 9,
        "defense_bonus": 5,
        "exp_bonus": 55,
        "gold_bonus": 45
    }
}


DROP_TABLES = {
    "Slime": SLIME_DROPS,
    "Goblin": GOBLIN_DROPS,
    "Skeleton": SKELETON_DROPS,
    "Bat": BAT_DROPS,
    "Spider": SPIDER_DROPS,
    "Wolf": WOLF_DROPS,
    "Zombie": ZOMBIE_DROPS,
    "Orc": ORC_DROPS,
    "Dark Mage": DARK_MAGE_DROPS,
    "Bandit": BANDIT_DROPS,
    "Giant Rat": GIANT_RAT_DROPS,
    "Troll": TROLL_DROPS,
    "Wraith": WRAITH_DROPS,
    "Lizardman": LIZARDMAN_DROPS,
    "Harpy": HARPY_DROPS,

    "Goblin King": GOBLIN_KING_DROPS,
    "Skeleton Lord": SKELETON_LORD_DROPS,
    "Slime Monarch": SLIME_MONARCH_DROPS,
    "Orc Warlord": ORC_WARLORD_DROPS,
    "Ancient Wraith": ANCIENT_WRAITH_DROPS
}


class Enemy(Character):

    def __init__(
        self,
        name,
        level,
        hp,
        max_hp,
        attack,
        defense,
        exp_reward,
        gold_reward,
        enemy_type
    ):

        super().__init__(
            name,
            level,
            hp,
            max_hp,
            attack,
            defense
        )

        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        self.enemy_type = enemy_type

    def drop_item(self):

        drop_pool = DROP_TABLES.get(self.name)

        if not drop_pool:
            return None

        return random_drop(drop_pool)

    def get_info(self):

        return (
            f"{self.name} "
            f"(Lv {self.level}) | "
            f"Type: {self.enemy_type} | "
            f"HP: {self.hp}/{self.max_hp} | "
            f"ATK: {self.attack} | "
            f"DEF: {self.defense}"
        )


class OrdinaryEnemy(Enemy):

    def __init__(self, name, level):

        hp = 40 + (level * 10)
        attack = 6 + (level * 2)
        defense = 2 + level

        exp_reward = 20 + (level * 5)
        gold_reward = 10 + (level * 3)

        mods = ENEMY_MODS.get(
            name,
            {
                "hp_bonus": 0,
                "attack_bonus": 0,
                "defense_bonus": 0,
                "exp_bonus": 0,
                "gold_bonus": 0
            }
        )

        hp += mods["hp_bonus"]
        attack += mods["attack_bonus"]
        defense += mods["defense_bonus"]
        exp_reward += mods["exp_bonus"]
        gold_reward += mods["gold_bonus"]

        hp = max(1, hp)
        attack = max(1, attack)
        defense = max(0, defense)

        super().__init__(
            name=name,
            level=level,
            hp=hp,
            max_hp=hp,
            attack=attack,
            defense=defense,
            exp_reward=exp_reward,
            gold_reward=gold_reward,
            enemy_type="Ordinary"
        )

    def attack_target(self, target):

        damage = max(
            1,
            self.attack - target.defense
        )

        target.take_damage(damage)

        print(
            f"{self.name} attacks "
            f"{target.name} for "
            f"{damage} damage!"
        )


class BossEnemy(Enemy):

    def __init__(
        self,
        name,
        level,
        phase=1
    ):

        hp = 80 + (level * 20)
        attack = 10 + (level * 3)
        defense = 4 + level

        exp_reward = 80 + (level * 15)
        gold_reward = 50 + (level * 8)

        mods = BOSS_MODS.get(
            name,
            {
                "hp_bonus": 0,
                "attack_bonus": 0,
                "defense_bonus": 0,
                "exp_bonus": 0,
                "gold_bonus": 0
            }
        )

        hp += mods["hp_bonus"]
        attack += mods["attack_bonus"]
        defense += mods["defense_bonus"]
        exp_reward += mods["exp_bonus"]
        gold_reward += mods["gold_bonus"]

        hp = max(1, hp)
        attack = max(1, attack)
        defense = max(0, defense)

        super().__init__(
            name=name,
            level=level,
            hp=hp,
            max_hp=hp,
            attack=attack,
            defense=defense,
            exp_reward=exp_reward,
            gold_reward=gold_reward,
            enemy_type="Boss"
        )

        self.phase = phase
        self.special_chance = 0.30

    def normal_attack(self, target):

        damage = max(
            1,
            self.attack - target.defense
        )

        target.take_damage(damage)

        print(
            f"{self.name} attacks "
            f"{target.name} for "
            f"{damage} damage!"
        )

    def special_attack(self, target):

        damage = max(
            1,
            int(self.attack * 1.5) - target.defense
        )

        target.take_damage(damage)

        print(
            f"{self.name} uses a heavy attack on "
            f"{target.name} for "
            f"{damage} damage!"
        )

    def attack_target(self, target):

        if (
            self.hp <= self.max_hp // 2
            and self.phase == 1
        ):

            self.phase = 2

            print(
                f"{self.name} enters Phase 2!"
            )

        if (
            self.phase == 2
            and random.random() <= self.special_chance
        ):

            self.special_attack(target)

        else:

            self.normal_attack(target)


def create_ordinary_enemy(name, level):

    return OrdinaryEnemy(
        name=name,
        level=level
    )


def create_boss_enemy(name, level):

    return BossEnemy(
        name=name,
        level=level
    )