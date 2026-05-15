import copy

from .character import Character
from .inventory import Inventory

from .item import (
    rusty_dagger,
    wooden_sword,
    cloth_helmet,
    cloth_chestplate,
    cloth_leggings,
    leather_helmet,
    leather_chestplate,
    leather_leggings,
    wooden_shield
)


class Player(Character):

    def __init__(
        self,
        name,
        hp=100,
        attack=10,
        defense=5
    ):

        super().__init__(
            name=name,
            level=1,
            hp=hp,
            max_hp=hp,
            attack=attack,
            defense=defense
        )

        self.inventory = Inventory()

        self.exp = 0
        self.gold = 0
        self.path_level = 1

        self.temp_attack_bonus = 0
        self.attack_boost_turns = 0

        self.temp_defense_bonus = 0
        self.defense_boost_turns = 0

    def required_exp_to_level(self):

        return self.level * 100

    def get_exp_info(self):

        needed = self.required_exp_to_level() - self.exp

        if needed < 0:
            needed = 0

        return (
            f"{self.exp}/"
            f"{self.required_exp_to_level()} "
            f"| Needed: {needed}"
        )

    def gain_exp(self, amount):

        self.exp += amount

        print(f"Gained {amount} EXP.")

        self.check_level_up()

    def check_level_up(self):

        while self.exp >= self.required_exp_to_level():

            required_exp = self.required_exp_to_level()

            self.exp -= required_exp
            self.level += 1

            self.max_hp += 20
            self.hp = self.max_hp

            self.attack += 3
            self.defense += 2

            print("\nLEVEL UP!")

            print(
                f"{self.name} is now "
                f"level {self.level}!"
            )

            print("+20 Max HP")
            print("+3 Attack")
            print("+2 Defense")
            print("HP fully restored.")

    def add_starting_equipment(self, equipment_list):

        for item_template in equipment_list:

            item = copy.deepcopy(item_template)

            added = self.inventory.add_item(
                item,
                self
            )

            if added:
                self.inventory.equip_item(
                    item,
                    self
                )

    def special_attack(self, target):

        damage = max(
            1,
            (self.attack * 2) - target.defense
        )

        target.take_damage(damage)

        print(
            f"{self.name} uses Special Attack "
            f"on {target.name} for {damage} damage!"
        )


class Rogue(Player):

    def __init__(self, name="Rogue"):

        super().__init__(
            name=name,
            hp=80,
            attack=15,
            defense=3
        )

        self.crit_rate = 0.2
        self.dodge = 0.15

        self.add_starting_equipment([
            rusty_dagger,
            cloth_helmet,
            cloth_chestplate,
            cloth_leggings
        ])

    def special_attack(self, target):

        damage = max(
            1,
            int((self.attack * 2.5) - target.defense)
        )

        target.take_damage(damage)

        print(
            f"{self.name} uses Shadow Strike "
            f"on {target.name} for {damage} damage!"
        )


class Warrior(Player):

    def __init__(self, name="Warrior"):

        super().__init__(
            name=name,
            hp=120,
            attack=12,
            defense=8
        )

        self.strength = 5
        self.rage = 0

        self.add_starting_equipment([
            wooden_sword,
            leather_helmet,
            leather_chestplate,
            leather_leggings
        ])

    def special_attack(self, target):

        damage = max(
            1,
            int(((self.attack + self.strength) * 2) - target.defense)
        )

        target.take_damage(damage)

        self.rage += 10

        print(
            f"{self.name} uses Crushing Slash "
            f"on {target.name} for {damage} damage!"
        )

        print(
            f"{self.name}'s rage increased to "
            f"{self.rage}."
        )


class Knight(Player):

    def __init__(self, name="Knight"):

        super().__init__(
            name=name,
            hp=150,
            attack=10,
            defense=12
        )

        self.shield_block = 0.25
        self.endurance = 10

        self.add_starting_equipment([
            wooden_sword,
            leather_helmet,
            leather_chestplate,
            leather_leggings,
            wooden_shield
        ])

    def special_attack(self, target):

        damage = max(
            1,
            int((self.attack * 1.8) + self.defense - target.defense)
        )

        target.take_damage(damage)

        self.defense += 2

        print(
            f"{self.name} uses Shield Breaker "
            f"on {target.name} for {damage} damage!"
        )

        print(
            f"{self.name} gains +2 DEF."
        )


def create_player(class_name):

    player_classes = {
        "Rogue": Rogue,
        "Warrior": Warrior,
        "Knight": Knight
    }

    if class_name not in player_classes:

        print("Invalid class. Defaulting to Rogue.")
        return Rogue()

    return player_classes[class_name]()