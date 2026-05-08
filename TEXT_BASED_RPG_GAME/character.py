class Character:

    def __init__(
        self,
        name,
        level,
        hp,
        max_hp,
        attack,
        defense
    ):

        self.name = name
        self.level = level

        self.hp = hp
        self.max_hp = max_hp

        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

    def is_alive(self):

        return self.hp > 0

    def basic_attack(self, target):

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

    def get_info(self):

        return (
            f"{self.name} "
            f"(Lv {self.level}) | "
            f"HP: {self.hp}/{self.max_hp} | "
            f"ATK: {self.attack} | "
            f"DEF: {self.defense}"
        )