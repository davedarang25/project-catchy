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

        return (
            f"{self.exp}/"
            f"{self.required_exp_to_level()}"
        )

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


PLAYER_CLASSES = {

    "Rogue": {
        "hp": 80,
        "attack": 15,
        "defense": 3,
        "extra_stats": {
            "crit_rate": 0.2,
            "dodge": 0.15
        },
        "equipment": [
            rusty_dagger,
            cloth_helmet,
            cloth_chestplate,
            cloth_leggings
        ]
    },

    "Warrior": {
        "hp": 120,
        "attack": 12,
        "defense": 8,
        "extra_stats": {
            "strength": 5,
            "rage": 0
        },
        "equipment": [
            wooden_sword,
            leather_helmet,
            leather_chestplate,
            leather_leggings
        ]
    },

    "Knight": {
        "hp": 150,
        "attack": 10,
        "defense": 12,
        "extra_stats": {
            "shield_block": 0.25,
            "endurance": 10
        },
        "equipment": [
            wooden_sword,
            leather_helmet,
            leather_chestplate,
            leather_leggings,
            wooden_shield
        ]
    }
}


def create_player(class_name):

    data = PLAYER_CLASSES[class_name]

    player = Player(
        name=class_name,
        hp=data["hp"],
        attack=data["attack"],
        defense=data["defense"]
    )

    for stat_name, stat_value in data["extra_stats"].items():
        setattr(player, stat_name, stat_value)

    for item_template in data["equipment"]:

        item = copy.deepcopy(item_template)

        player.inventory.add_item(item, player)
        player.inventory.equip_item(item, player)

    return player