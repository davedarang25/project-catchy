from item import Item


class Inventory:

    def __init__(self, capacity=10):

        self.capacity = capacity
        self.items = []

        self.weapon = None
        self.helmet = None
        self.chestplate = None
        self.leggings = None

    def is_empty(self):

        return len(self.items) == 0

    def is_full(self):

        return len(self.items) >= self.capacity

    def add_item(self, item: Item):

        if self.is_full():

            print("Inventory is full.")
            return False

        self.items.append(item)

        print(f"{item.name} added to inventory.")

        return True

    def remove_item(self, item: Item):

        if item in self.items:

            self.items.remove(item)

            print(f"{item.name} removed.")

            return True

        print("Item not found.")
        return False

    def show_items(self):

        if self.is_empty():

            print("Inventory is empty.")
            return

        print("\n=== INVENTORY ===")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.get_info()}")

    def equip_item(self, item, player):

        if item.itemType == "Weapon":

            if self.weapon:
                player.attack -= self.weapon.value

            self.weapon = item
            player.attack += item.value

            print(f"{item.name} equipped.")

        elif item.itemType == "Armor":

            if self.chestplate:
                player.defense -= self.chestplate.value

            self.chestplate = item
            player.defense += item.value

            print(f"{item.name} equipped.")

        else:

            print("This item cannot be equipped.")

    def use_item(self, item, player):

        if item not in self.items:

            print("Item not found.")
            return

        if item.itemType != "Consumable":

            print("You cannot use that item.")
            return

        item.use(player)
        self.remove_item(item)

    def inventory_menu(self, player):

        while True:

            print("\n" + "=" * 30)
            print("         PLAYER STATS")
            print("=" * 30)

            print(f"HP: {player.hp}/{player.max_hp}")
            print(f"ATK: {player.attack}")
            print(f"DEF: {player.defense}")
            print(f"GOLD: {player.gold}")
            print(f"EXP: {player.exp}")
            print(f"LEVEL: {player.level}")

            print("\n" + "=" * 30)
            print("      EQUIPPED ITEMS")
            print("=" * 30)

            print(f"Weapon: {self.weapon.name if self.weapon else 'Empty'}")
            print(f"Helmet: {self.helmet.name if self.helmet else 'Empty'}")
            print(f"Chest : {self.chestplate.name if self.chestplate else 'Empty'}")
            print(f"Legs  : {self.leggings.name if self.leggings else 'Empty'}")

            print("\n" + "=" * 30)
            print("1. Weapon")
            print("2. Armor")
            print("3. Items")
            print("4. View All Items")
            print("5. Exit")
            print("=" * 30)

            choice = input("Choose: ").strip()

            if choice == "1":
                self.weapon_menu(player)

            elif choice == "2":
                self.armor_menu(player)

            elif choice == "3":
                self.item_menu(player)

            elif choice == "4":
                self.show_items()

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

    def weapon_menu(self, player):

        weapons = [
            i for i in self.items
            if i.itemType == "Weapon"
        ]

        print("\n=== WEAPONS ===")

        if not weapons:
            print("No weapons available.")
            return

        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon.name} (+{weapon.value} ATK)")

        print(f"{len(weapons) + 1}. Exit")

        choice = input("Choose: ").strip()

        if choice == str(len(weapons) + 1):
            return

        try:

            weapon = weapons[int(choice) - 1]
            self.equip_item(weapon, player)

        except (ValueError, IndexError):

            print("Invalid choice.")

    def armor_menu(self, player):

        armors = [
            i for i in self.items
            if i.itemType == "Armor"
        ]

        print("\n=== ARMOR ===")
        print("1. Helmet")
        print("2. Chestplate")
        print("3. Legs")
        print("4. Exit")

        slot = input("Choose slot: ").strip()

        if slot == "4":
            return

        slot_map = {
            "1": "helmet",
            "2": "chestplate",
            "3": "leggings"
        }

        if slot not in slot_map:
            print("Invalid slot.")
            return

        slot_name = slot_map[slot]
        current = getattr(self, slot_name)

        print(f"\nCurrent: {current.name if current else 'Empty'}")

        if not armors:
            print("No armor available.")
            return

        for i, armor in enumerate(armors, 1):
            print(f"{i}. {armor.name} (+{armor.value} DEF)")

        print(f"{len(armors) + 1}. Exit")

        choice = input("Choose: ").strip()

        if choice == str(len(armors) + 1):
            return

        try:

            armor = armors[int(choice) - 1]

            if current:
                player.defense -= current.value

            setattr(self, slot_name, armor)
            player.defense += armor.value

            print(f"{armor.name} equipped.")

        except (ValueError, IndexError):

            print("Invalid choice.")

    def item_menu(self, player):

        items = [
            i for i in self.items
            if i.itemType == "Consumable"
        ]

        print("\n=== ITEMS ===")

        if not items:
            print("No items available.")
            return

        for i, item in enumerate(items, 1):
            print(f"{i}. {item.name}")

        print(f"{len(items) + 1}. Exit")

        choice = input("Choose: ").strip()

        if choice == str(len(items) + 1):
            return

        try:

            item = items[int(choice) - 1]

            item.use(player)

            self.remove_item(item)

        except (ValueError, IndexError):

            print("Invalid choice.")