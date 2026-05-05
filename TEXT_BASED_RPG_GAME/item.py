# item py
class Item:
    def __init__(self, id, name, description, itemType):
        self.id = id
        self.name = name
        self.description = description
        self.itemType = itemType # for "Weapons", "Armour", and "Consumable"

    def use(self, user):
        print(f"{self.name} used by {user.name}")
        # Base item does nothing; subclasses override this.

    def get_info(self):
        return f"{self.name} ({self.itemType}) - {self.description}"
    
class Weapon(Item):
    def __init__(self, id, name, description, attackBonus, durability=10):
        super().__init__(id, name, description, "Weapon")
        self.attackBonus = attackBonus
        self.durability = durability

    def use(self, user):
        print(f"{user.name} equips {self.name}. Attack +{self.attackBonus}")
        user.attack += self.attackBonus
        self.durability -=1
        if self.durability <= 0:
            print(f"{self.name} broke!")
            # Optional: remove from inventory

class Armor(Item):
    def __init__(self, id , name, description, defenseBonus, durability=10):
        super().__init__(id, name, description, "Armor")
        self.defenseBonus = defenseBonus
        self.durability = durability

    def use(self,user):
        print(f"{user.name} equip {self.name}. Defense +{self.defenseBonus}")
        user.defense += self.defenseBonus
        self.durability -= 1
        if self.durability <= 0:
            print(f"{self.name} broke!")

class HealingItem(Item):
    def __init__(self, id, name, description, healAmount):
        super().__init__(id, name, description, "Consumable")
        self.healAmount= healAmount

    def use(self, user):
        user.hp += self.healAmount
        if user.hp > user.maxHp:
            user.hp = user.maxHp
        print(f"{user.name} healed for {self.healAmount}. Current HP: {user.hp}")