from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(
        self,
        name,
        level,
        hp,
        max_hp,
        attack,
        defense
    ):

        self._name = name
        self._level = max(1, level)

        self._max_hp = max(1, max_hp)
        self._hp = max(0, min(hp, self._max_hp))

        self._attack = max(0, attack)
        self._defense = max(0, defense)

    # =========================
    # PROPERTIES
    # =========================

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = max(1, value)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._max_hp))

    @property
    def max_hp(self):
        return self._max_hp

    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = max(1, value)

        if self._hp > self._max_hp:
            self._hp = self._max_hp

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = max(0, value)

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = max(0, value)

    # =========================
    # SHARED METHODS
    # =========================

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

    def get_info(self):
        return (
            f"{self.name} "
            f"(Lv {self.level}) | "
            f"HP: {self.hp}/{self.max_hp} | "
            f"ATK: {self.attack} | "
            f"DEF: {self.defense}"
        )

    # =========================
    # ABSTRACT METHOD
    # =========================

    @abstractmethod
    def attack_target(self, target):
        pass