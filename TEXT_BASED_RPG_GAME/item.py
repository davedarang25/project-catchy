import random
import copy


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
        slot,
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
        self.slot = slot


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
        self.value = healAmount

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


class AttackBoostPotion(Item):

    def __init__(
        self,
        id,
        name,
        description,
        attackBoost,
        turns=3,
        rarity="Common"
    ):

        super().__init__(
            id,
            name,
            description,
            "Consumable",
            rarity
        )

        self.attackBoost = attackBoost
        self.turns = turns
        self.value = attackBoost

    def use(self, user):

        if not hasattr(user, "temp_attack_bonus"):
            user.temp_attack_bonus = 0

        if not hasattr(user, "attack_boost_turns"):
            user.attack_boost_turns = 0

        if user.temp_attack_bonus > 0:
            user.attack -= user.temp_attack_bonus

        user.temp_attack_bonus = self.attackBoost
        user.attack_boost_turns = self.turns
        user.attack += self.attackBoost

        print(f"{user.name} used {self.name}!")
        print(
            f"ATK increased by {self.attackBoost} "
            f"for {self.turns} turns."
        )


class DefenseBoostPotion(Item):

    def __init__(
        self,
        id,
        name,
        description,
        defenseBoost,
        turns=3,
        rarity="Common"
    ):

        super().__init__(
            id,
            name,
            description,
            "Consumable",
            rarity
        )

        self.defenseBoost = defenseBoost
        self.turns = turns
        self.value = defenseBoost

    def use(self, user):

        if not hasattr(user, "temp_defense_bonus"):
            user.temp_defense_bonus = 0

        if not hasattr(user, "defense_boost_turns"):
            user.defense_boost_turns = 0

        if user.temp_defense_bonus > 0:
            user.defense -= user.temp_defense_bonus

        user.temp_defense_bonus = self.defenseBoost
        user.defense_boost_turns = self.turns
        user.defense += self.defenseBoost

        print(f"{user.name} used {self.name}!")
        print(
            f"DEF increased by {self.defenseBoost} "
            f"for {self.turns} turns."
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

steel_sword = Weapon(
    6,
    "Steel Sword",
    "A stronger steel blade.",
    9,
    "Uncommon"
)

shadow_dagger = Weapon(
    7,
    "Shadow Dagger",
    "A sharp dagger used by fast enemies.",
    8,
    "Rare"
)

spider_fang_blade = Weapon(
    8,
    "Spider Fang Blade",
    "A blade made from a giant spider fang.",
    10,
    "Rare"
)


cloth_helmet = Armor(
    9,
    "Cloth Helmet",
    "Simple cloth head protection.",
    1,
    "helmet"
)

cloth_chestplate = Armor(
    10,
    "Cloth Chestplate",
    "Simple cloth body protection.",
    2,
    "chestplate"
)

cloth_leggings = Armor(
    11,
    "Cloth Leggings",
    "Simple cloth leg protection.",
    1,
    "leggings"
)

leather_helmet = Armor(
    12,
    "Leather Helmet",
    "Light leather head protection.",
    2,
    "helmet"
)

leather_chestplate = Armor(
    13,
    "Leather Chestplate",
    "Light leather body armor.",
    4,
    "chestplate"
)

leather_leggings = Armor(
    14,
    "Leather Leggings",
    "Light leather leg protection.",
    2,
    "leggings"
)

iron_helmet = Armor(
    15,
    "Iron Helmet",
    "Heavy iron head protection.",
    3,
    "helmet",
    "Uncommon"
)

iron_chestplate = Armor(
    16,
    "Iron Chestplate",
    "Heavy iron body armor.",
    6,
    "chestplate",
    "Uncommon"
)

iron_leggings = Armor(
    17,
    "Iron Leggings",
    "Heavy iron leg protection.",
    3,
    "leggings",
    "Uncommon"
)

wooden_shield = Armor(
    18,
    "Wooden Shield",
    "Basic wooden shield.",
    3,
    "shield"
)

iron_shield = Armor(
    19,
    "Iron Shield",
    "A stronger iron shield.",
    5,
    "shield",
    "Uncommon"
)

bone_helmet = Armor(
    20,
    "Bone Helmet",
    "Helmet made from monster bones.",
    3,
    "helmet",
    "Uncommon"
)

bone_chestplate = Armor(
    21,
    "Bone Chestplate",
    "Armor made from monster bones.",
    5,
    "chestplate",
    "Uncommon"
)

bone_leggings = Armor(
    22,
    "Bone Leggings",
    "Leg armor made from monster bones.",
    3,
    "leggings",
    "Uncommon"
)

wolf_hide_chestplate = Armor(
    23,
    "Wolf Hide Chestplate",
    "Flexible armor made from wolf hide.",
    5,
    "chestplate",
    "Uncommon"
)

royal_guard_armor = Armor(
    24,
    "Royal Guard Chestplate",
    "Armor once worn by a dungeon guard.",
    8,
    "chestplate",
    "Rare"
)


small_potion = HealingItem(
    25,
    "Small Potion",
    "Restores 25 HP.",
    25
)

medium_potion = HealingItem(
    26,
    "Medium Potion",
    "Restores 50 HP.",
    50,
    "Uncommon"
)

large_potion = HealingItem(
    27,
    "Large Potion",
    "Restores 85 HP.",
    85,
    "Rare"
)

bread = HealingItem(
    28,
    "Bread",
    "Simple food. Restores 15 HP.",
    15
)

meat = HealingItem(
    29,
    "Cooked Meat",
    "Fresh cooked meat. Restores 35 HP.",
    35,
    "Uncommon"
)

minor_attack_potion = AttackBoostPotion(
    30,
    "Minor Rage Potion",
    "Boosts attack by 3 for 3 turns.",
    3,
    3,
    "Common"
)

attack_potion = AttackBoostPotion(
    31,
    "Rage Potion",
    "Boosts attack by 5 for 3 turns.",
    5,
    3,
    "Uncommon"
)

greater_attack_potion = AttackBoostPotion(
    32,
    "Greater Rage Potion",
    "Boosts attack by 8 for 3 turns.",
    8,
    3,
    "Rare"
)

minor_defense_potion = DefenseBoostPotion(
    33,
    "Minor Guard Potion",
    "Boosts defense by 3 for 3 turns.",
    3,
    3,
    "Common"
)

defense_potion = DefenseBoostPotion(
    34,
    "Guard Potion",
    "Boosts defense by 5 for 3 turns.",
    5,
    3,
    "Uncommon"
)

greater_defense_potion = DefenseBoostPotion(
    35,
    "Greater Guard Potion",
    "Boosts defense by 8 for 3 turns.",
    8,
    3,
    "Rare"
)


cloth_armor = cloth_chestplate
leather_armor = leather_chestplate
iron_armor = iron_chestplate
bone_armor = bone_chestplate
wolf_hide_armor = wolf_hide_chestplate


SLIME_DROPS = [
    small_potion,
    bread,
    minor_defense_potion
]

GOBLIN_DROPS = [
    wooden_sword,
    leather_helmet,
    leather_chestplate,
    leather_leggings,
    medium_potion,
    minor_attack_potion,
    attack_potion
]

SKELETON_DROPS = [
    iron_sword,
    bone_club,
    bone_helmet,
    bone_chestplate,
    bone_leggings,
    large_potion,
    defense_potion
]

BAT_DROPS = [
    small_potion,
    bread,
    shadow_dagger,
    minor_attack_potion
]

SPIDER_DROPS = [
    medium_potion,
    spider_fang_blade,
    defense_potion,
    attack_potion
]

WOLF_DROPS = [
    meat,
    wolf_hide_chestplate,
    minor_attack_potion,
    minor_defense_potion
]

GOBLIN_KING_DROPS = [
    steel_sword,
    royal_guard_armor,
    greater_attack_potion,
    large_potion
]

SKELETON_LORD_DROPS = [
    bone_club,
    bone_helmet,
    bone_chestplate,
    bone_leggings,
    greater_defense_potion,
    large_potion
]

SLIME_MONARCH_DROPS = [
    large_potion,
    greater_defense_potion,
    greater_attack_potion
]


def random_drop(drop_pool):

    if random.random() <= 0.45:

        return copy.deepcopy(
            random.choice(drop_pool)
        )

    return None