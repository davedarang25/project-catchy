import random


class Item:

    def __init__(
        self,
        id,
        name,
        description,
        itemType,
        rarity="Common"
    ):

        self.id = id
        self.name = name
        self.description = description
        self.itemType = itemType
        self.rarity = rarity

        self.value = 0

    def use(self, user):

        print(
            f"{self.name} used by "
            f"{user.name}."
        )

    def get_info(self):

        return (
            f"{self.name} "
            f"[{self.rarity}] "
            f"({self.itemType}) - "
            f"{self.description}"
        )


class Weapon(Item):

    def __init__(
        self,
        id,
        name,
        description,
        attackBonus,
        rarity="Common"
    ):

        super().__init__(
            id,
            name,
            description,
            "Weapon",
            rarity
        )

        self.attackBonus = attackBonus
        self.value = attackBonus


class Armor(Item):

    def __init__(
        self,
        id,
        name,
        description,
        defenseBonus,
        rarity="Common"
    ):

        super().__init__(
            id,
            name,
            description,
            "Armor",
            rarity
        )

        self.defenseBonus = defenseBonus
        self.value = defenseBonus


class HealingItem(Item):

    def __init__(
        self,
        id,
        name,
        description,
        healAmount,
        rarity="Common"
    ):

        super().__init__(
            id,
            name,
            description,
            "Consumable",
            rarity
        )

        self.healAmount = healAmount

    def use(self, user):

        old_hp = user.hp

        user.hp += self.healAmount

        if user.hp > user.max_hp:
            user.hp = user.max_hp

        healed = user.hp - old_hp

        print(
            f"{user.name} used "
            f"{self.name} "
            f"and restored "
            f"{healed} HP!"
        )


rusty_dagger = Weapon(
    1,
    "Rusty Dagger",
    "A weak rusty dagger.",
    3
)

wooden_sword = Weapon(
    2,
    "Wooden Sword",
    "Basic training sword.",
    4
)

iron_sword = Weapon(
    3,
    "Iron Sword",
    "Reliable iron blade.",
    6
)

hunter_bow = Weapon(
    4,
    "Hunter Bow",
    "Simple ranged weapon.",
    5
)

bone_club = Weapon(
    5,
    "Bone Club",
    "Heavy monster bone.",
    7
)

cloth_armor = Armor(
    6,
    "Cloth Armor",
    "Simple cloth protection.",
    2
)

leather_armor = Armor(
    7,
    "Leather Armor",
    "Light leather armor.",
    4
)

iron_armor = Armor(
    8,
    "Iron Armor",
    "Heavy iron armor.",
    6
)

wooden_shield = Armor(
    9,
    "Wooden Shield",
    "Basic shield.",
    3
)

small_potion = HealingItem(
    10,
    "Small Potion",
    "Restores 20 HP.",
    20
)

medium_potion = HealingItem(
    11,
    "Medium Potion",
    "Restores 40 HP.",
    40
)

large_potion = HealingItem(
    12,
    "Large Potion",
    "Restores 75 HP.",
    75
)

bread = HealingItem(
    13,
    "Bread",
    "Simple food.",
    10
)

meat = HealingItem(
    14,
    "Cooked Meat",
    "Fresh cooked meat.",
    25
)

SLIME_DROPS = [
    small_potion,
    bread
]

GOBLIN_DROPS = [
    wooden_sword,
    leather_armor,
    medium_potion
]

SKELETON_DROPS = [
    iron_sword,
    bone_club,
    large_potion
]


def random_drop(drop_pool):

    if random.random() <= 0.40:
        return random.choice(drop_pool)

    return None