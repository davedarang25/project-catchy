from character import Character
from inventory import Inventory

from item import (
    rusty_dagger,
    wooden_sword,
    cloth_armor,
    leather_armor,
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

        self.inventory.add_item(rusty_dagger)
        self.inventory.add_item(cloth_armor)

        self.inventory.equip_item(
            rusty_dagger,
            self
        )

        self.inventory.equip_item(
            cloth_armor,
            self
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

        self.inventory.add_item(wooden_sword)
        self.inventory.add_item(leather_armor)

        self.inventory.equip_item(
            wooden_sword,
            self
        )

        self.inventory.equip_item(
            leather_armor,
            self
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

        self.inventory.add_item(wooden_sword)
        self.inventory.add_item(wooden_shield)

        self.inventory.equip_item(
            wooden_sword,
            self
        )

        self.inventory.equip_item(
            wooden_shield,
            self
        )