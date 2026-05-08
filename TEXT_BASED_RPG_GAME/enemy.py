from .character import Character


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

        from item import (
            random_drop,
            SLIME_DROPS,
            GOBLIN_DROPS,
            SKELETON_DROPS
        )

        if self.name == "Slime":
            return random_drop(SLIME_DROPS)

        elif self.name == "Goblin":
            return random_drop(GOBLIN_DROPS)

        elif self.name == "Skeleton":
            return random_drop(SKELETON_DROPS)

        return None

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

        hp = 100 + (level * 25)
        attack = 12 + (level * 4)
        defense = 5 + (level * 2)

        exp_reward = 80 + (level * 20)
        gold_reward = 50 + (level * 10)

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

    def special_attack(self, target):

        damage = max(
            1,
            (self.attack * 2) - target.defense
        )

        target.take_damage(damage)

        print(
            f"{self.name} uses "
            f"a special attack on "
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

        if self.phase == 2:

            self.special_attack(target)

        else:

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


class Slime(OrdinaryEnemy):

    def __init__(self, level=1):

        super().__init__(
            name="Slime",
            level=level
        )

        self.hp += 15
        self.max_hp += 15

        self.attack = max(
            1,
            self.attack - 2
        )


class Goblin(OrdinaryEnemy):

    def __init__(self, level=1):

        super().__init__(
            name="Goblin",
            level=level
        )

        self.gold_reward += 5


class Skeleton(OrdinaryEnemy):

    def __init__(self, level=1):

        super().__init__(
            name="Skeleton",
            level=level
        )

        self.attack += 4

        self.hp = max(1, self.hp - 10)
        self.max_hp = max(1, self.max_hp - 10)