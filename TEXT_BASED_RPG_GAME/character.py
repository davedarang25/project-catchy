# character.py

class Character:
    def __init__(self, name, level=1, hp=100, maxHp=None, attack=10, defense=5):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = maxHp if maxHp is not None else hp
        self.attack = attack
        self.defense = defense
        #self.inventory = Inventory()   # <-- add inventory here # <-- edit out for enemy to inherit, I moved it in player

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def get_info(self):
        return f"{self.name} | HP: {self.hp}/{self.max_hp} | ATK: {self.attack} | DEF: {self.defense}"


"""class Rogue(player):
    def __init__(self, name="Rogue"):
        super().__init__(name, hp=80, attack=15, defense=3)
        self.crit_rate = 0.2
        self.dodge = 0.15


class Warrior(Character):
    def __init__(self, name="Warrior"):
        super().__init__(name, hp=120, attack=12, defense=8)
        self.strength = 5
        self.rage = 0


class Knight(Character):
    def __init__(self, name="Knight"):
        super().__init__(name, hp=150, attack=10, defense=12)
        self.shield_block = 0.25
        self.endurance = 10""" #<--- moved out to player
