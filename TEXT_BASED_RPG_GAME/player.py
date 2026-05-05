# player.py
from character import Character
from inventory import Inventory

class Player(Character):
    def __init__(self, name, hp=100, attack=10, defense=5):
        super().__init__(name, hp, attack, defense)
        self.inventory = Inventory()
        self.level = 1
        self.exp = 0
        self.gold = 0

class Rogue(Player):
    def __init__(self, name="Rogue"):
        super().__init__(name, hp=80, attack=15, defense=3)
        self.crit_rate = 0.2
        self.dodge = 0.15


class Warrior(Player):
    def __init__(self, name="Warrior"):
        super().__init__(name, hp=120, attack=12, defense=8)
        self.strength = 5
        self.rage = 0


class Knight(Player):
    def __init__(self, name="Knight"):
        super().__init__(name, hp=150, attack=10, defense=12)
        self.shield_block = 0.25
        self.endurance = 10