import copy
from abc import abstractmethod

from .character import Character
from .inventory import Inventory
from .logger import Logger

logger = Logger(delay=0.02)

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

        self._inventory = Inventory()

        self._exp = 0
        self._gold = 0
        self._path_level = 1

        self._temp_attack_bonus = 0
        self._attack_boost_turns = 0

        self._temp_defense_bonus = 0
        self._defense_boost_turns = 0

    # =========================
    # ENCAPSULATED PROPERTIES
    # =========================

    @property
    def inventory(self):
        return self._inventory

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = max(0, value)

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = max(0, value)

    @property
    def path_level(self):
        return self._path_level

    @path_level.setter
    def path_level(self, value):
        self._path_level = max(1, value)

    @property
    def temp_attack_bonus(self):
        return self._temp_attack_bonus

    @temp_attack_bonus.setter
    def temp_attack_bonus(self, value):
        self._temp_attack_bonus = max(0, value)

    @property
    def attack_boost_turns(self):
        return self._attack_boost_turns

    @attack_boost_turns.setter
    def attack_boost_turns(self, value):
        self._attack_boost_turns = max(0, value)

    @property
    def temp_defense_bonus(self):
        return self._temp_defense_bonus

    @temp_defense_bonus.setter
    def temp_defense_bonus(self, value):
        self._temp_defense_bonus = max(0, value)

    @property
    def defense_boost_turns(self):
        return self._defense_boost_turns

    @defense_boost_turns.setter
    def defense_boost_turns(self, value):
        self._defense_boost_turns = max(0, value)

    # =========================
    # PLAYER METHODS
    # =========================

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

    # =========================
    # ABSTRACTION
    # =========================

    @abstractmethod
    def special_attack(self, target):
        pass


class Rogue(Player):

    def __init__(self, name="Rogue"):

        super().__init__(
            name=name,
            hp=80,
            attack=15,
            defense=3
        )

        self._crit_rate = 0.2
        self._dodge = 0.15

        self.add_starting_equipment([
            rusty_dagger,
            cloth_helmet,
            cloth_chestplate,
            cloth_leggings
        ])

    @property
    def crit_rate(self):
        return self._crit_rate

    @crit_rate.setter
    def crit_rate(self, value):
        self._crit_rate = max(0, value)

    @property
    def dodge(self):
        return self._dodge

    @dodge.setter
    def dodge(self, value):
        self._dodge = max(0, value)

    def special_attack(self, enemy):

        damage = self.attack * 2
        enemy.take_damage(damage)

        logger.typewriter(
            f"{self.name} uses Backstab! "
            f"It deals {damage} damage."
        )


class Warrior(Player):

    def __init__(self, name="Warrior"):

        super().__init__(
            name=name,
            hp=120,
            attack=12,
            defense=8
        )

        self._strength = 5
        self._rage = 0

        self.add_starting_equipment([
            wooden_sword,
            leather_helmet,
            leather_chestplate,
            leather_leggings
        ])

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = max(0, value)

    @property
    def rage(self):
        return self._rage

    @rage.setter
    def rage(self, value):
        self._rage = max(0, value)

    def special_attack(self, enemy):

        damage = self.attack + self.strength
        enemy.take_damage(damage)

        self.rage += 5

        logger.typewriter(
            f"{self.name} uses Power Strike! "
            f"It deals {damage} damage."
        )


class Knight(Player):

    def __init__(self, name="Knight"):

        super().__init__(
            name=name,
            hp=150,
            attack=10,
            defense=12
        )

        self._shield_block = 0.25
        self._endurance = 10

        self.add_starting_equipment([
            wooden_sword,
            leather_helmet,
            leather_chestplate,
            leather_leggings,
            wooden_shield
        ])

    @property
    def shield_block(self):
        return self._shield_block

    @shield_block.setter
    def shield_block(self, value):
        self._shield_block = max(0, value)

    @property
    def endurance(self):
        return self._endurance

    @endurance.setter
    def endurance(self, value):
        self._endurance = max(0, value)

    def special_attack(self, enemy):

        damage = max(
            1,
            self.attack - enemy.defense
        )

        enemy.take_damage(damage)

        self.defense += 1

        logger.typewriter(
            f"{self.name} uses Shield Bash! "
            f"It deals {damage} damage and increases defense by 1."
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