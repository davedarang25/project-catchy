try:
    from .item import Item
except ImportError:
    from item import Item

try:
    from .utils import clear_screen
except ImportError:
    try:
        from utils import clear_screen
    except ImportError:
        def clear_screen():
            pass


class Inventory:

    def __init__(self, capacity=20):

        self.capacity = capacity
        self.items = []

        self.weapon = None
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.shield = None

    def is_empty(self):

        return len(self.items) == 0

    def is_full(self):

        return len(self.items) >= self.capacity

    def add_item(self, item: Item, player=None):

        if self.is_full():

            print("\nWARNING: Your bag is full!")
            print(f"You cannot carry {item.name}.")
            print("Do you want to discard an item to make space?")
            print("1. Yes")
            print("2. No")

            choice = input("Choose: ").strip()
            clear_screen()

            if choice != "1":

                print(f"{item.name} was left behind.")
                return False

            removed = self.discard_from_full_inventory(player)

            if not removed:

                print(f"{item.name} was left behind.")
                return False

        self.items.append(item)

        print(f"{item.name} added to inventory.")

        if self.is_full():
            print("\nWARNING: Your bag is now full!")

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
        print(f"Capacity: {len(self.items)}/{self.capacity}")

        if self.is_full():
            print("WARNING: Bag is full!")

        for i, item in enumerate(self.items, 1):

            equipped_text = ""

            if self.is_equipped(item):
                equipped_text = " [EQUIPPED]"

            print(f"{i}. {item.get_info()}{equipped_text}")

    def view_all_items_menu(self, player):

        while True:

            print("\n" + "=" * 30)
            print("        ALL ITEMS")
            print("=" * 30)

            print(f"Capacity: {len(self.items)}/{self.capacity}")

            if self.is_full():
                print("WARNING: Bag is full!")

            if self.is_empty():

                print("\nInventory is empty.")
                input("\nPress Enter to return...")
                clear_screen()
                return

            for i, item in enumerate(self.items, 1):

                equipped_text = ""

                if self.is_equipped(item):
                    equipped_text = " [EQUIPPED]"

                print(
                    f"{i}. {item.get_info()}"
                    f"{equipped_text}"
                )

            print(f"{len(self.items) + 1}. Exit")

            choice = input("\nChoose item: ").strip()
            clear_screen()

            if choice == str(len(self.items) + 1):
                return

            try:

                item = self.items[int(choice) - 1]

                print("\n" + "=" * 30)
                print(f"Selected: {item.name}")
                print("=" * 30)

                if item.itemType == "Weapon":

                    print("1. Equip")
                    print("2. Discard")
                    print("3. Cancel")

                    action = input("Choose: ").strip()
                    clear_screen()

                    if action == "1":
                        self.equip_item(item, player)

                    elif action == "2":
                        self.discard_item(item, player)

                    elif action == "3":
                        continue

                    else:
                        print("Invalid choice.")

                elif item.itemType == "Armor":

                    print("1. Equip")
                    print("2. Discard")
                    print("3. Cancel")

                    action = input("Choose: ").strip()
                    clear_screen()

                    if action == "1":
                        self.equip_item(item, player)

                    elif action == "2":
                        self.discard_item(item, player)

                    elif action == "3":
                        continue

                    else:
                        print("Invalid choice.")

                elif item.itemType == "Consumable":

                    print("1. Use")
                    print("2. Discard")
                    print("3. Cancel")

                    action = input("Choose: ").strip()
                    clear_screen()

                    if action == "1":
                        self.use_item(item, player)

                    elif action == "2":
                        self.discard_item(item, player)

                    elif action == "3":
                        continue

                    else:
                        print("Invalid choice.")

                else:

                    print("Unknown item type.")
                    input("\nPress Enter to continue...")
                    clear_screen()

            except (ValueError, IndexError):

                print("Invalid choice.")

    def is_equipped(self, item):

        return (
            item == self.weapon
            or item == self.helmet
            or item == self.chestplate
            or item == self.leggings
            or item == self.shield
        )

    def unequip_item(self, item, player):

        if item == self.weapon:

            if player:
                player.attack -= item.value

            self.weapon = None
            print(f"{item.name} unequipped.")

        elif item == self.helmet:

            if player:
                player.defense -= item.value

            self.helmet = None
            print(f"{item.name} unequipped.")

        elif item == self.chestplate:

            if player:
                player.defense -= item.value

            self.chestplate = None
            print(f"{item.name} unequipped.")

        elif item == self.leggings:

            if player:
                player.defense -= item.value

            self.leggings = None
            print(f"{item.name} unequipped.")

        elif item == self.shield:

            if player:
                player.defense -= item.value

            self.shield = None
            print(f"{item.name} unequipped.")

    def discard_item(self, item, player=None):

        if item not in self.items:

            print("Item not found.")
            return False

        confirm = input(
            f"Discard {item.name}? (YES/NO): "
        ).strip().upper()

        clear_screen()

        if confirm != "YES":

            print("Discard cancelled.")
            return False

        if self.is_equipped(item):
            self.unequip_item(item, player)

        self.items.remove(item)

        print(f"{item.name} discarded.")

        return True

    def discard_from_full_inventory(self, player=None):

        if self.is_empty():

            print("No items to discard.")
            return False

        while True:

            print("\n=== DISCARD ITEM ===")
            print(f"Capacity: {len(self.items)}/{self.capacity}")

            if self.is_full():
                print("WARNING: Bag is full!")

            for i, item in enumerate(self.items, 1):

                equipped_text = ""

                if self.is_equipped(item):
                    equipped_text = " [EQUIPPED]"

                print(f"{i}. {item.name}{equipped_text}")

            print(f"{len(self.items) + 1}. Cancel")

            choice = input("Choose item to discard: ").strip()
            clear_screen()

            if choice == str(len(self.items) + 1):
                return False

            try:

                item = self.items[int(choice) - 1]
                return self.discard_item(item, player)

            except (ValueError, IndexError):

                print("Invalid choice.")

    def equip_item(self, item, player):

        if item.itemType == "Weapon":

            if self.weapon:
                player.attack -= self.weapon.value

            self.weapon = item
            player.attack += item.value

            print(f"{item.name} equipped.")

        elif item.itemType == "Armor":

            slot_name = item.slot

            if not hasattr(self, slot_name):

                print("Invalid armor slot.")
                return

            current = getattr(self, slot_name)

            if current:
                player.defense -= current.value

            setattr(self, slot_name, item)
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
            print(f"Shield: {self.shield.name if self.shield else 'Empty'}")

            print("\n" + "=" * 30)
            print(f"Capacity: {len(self.items)}/{self.capacity}")

            if self.is_full():
                print("WARNING: Bag is full!")

            print("1. Weapon")
            print("2. Armor")
            print("3. Items")
            print("4. View All Items")
            print("5. Discard Item")
            print("6. Exit")
            print("=" * 30)

            choice = input("Choose: ").strip()
            clear_screen()

            if choice == "1":
                self.weapon_menu(player)

            elif choice == "2":
                self.armor_menu(player)

            elif choice == "3":
                self.item_menu(player)

            elif choice == "4":
                self.view_all_items_menu(player)

            elif choice == "5":
                self.discard_from_full_inventory(player)

            elif choice == "6":
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

            equipped_text = ""

            if weapon == self.weapon:
                equipped_text = " [EQUIPPED]"

            print(
                f"{i}. {weapon.name} "
                f"(+{weapon.value} ATK)"
                f"{equipped_text}"
            )

        print(f"{len(weapons) + 1}. Exit")

        choice = input("Choose weapon: ").strip()
        clear_screen()

        if choice == str(len(weapons) + 1):
            return

        try:

            weapon = weapons[int(choice) - 1]

            print(f"\nSelected: {weapon.name}")
            print("1. Equip")
            print("2. Discard")
            print("3. Cancel")

            action = input("Choose: ").strip()
            clear_screen()

            if action == "1":
                self.equip_item(weapon, player)

            elif action == "2":
                self.discard_item(weapon, player)

            elif action == "3":
                return

            else:
                print("Invalid choice.")

        except (ValueError, IndexError):

            print("Invalid choice.")

    def armor_menu(self, player):

        print("\n=== ARMOR ===")
        print("1. Helmet")
        print("2. Chestplate")
        print("3. Leggings")
        print("4. Shield")
        print("5. Discard Armor")
        print("6. Exit")

        slot = input("Choose: ").strip()
        clear_screen()

        if slot == "6":
            return

        if slot == "5":
            self.discard_armor_menu(player)
            return

        slot_map = {
            "1": "helmet",
            "2": "chestplate",
            "3": "leggings",
            "4": "shield"
        }

        if slot not in slot_map:
            print("Invalid slot.")
            return

        slot_name = slot_map[slot]
        current = getattr(self, slot_name)

        armors = [
            i for i in self.items
            if i.itemType == "Armor"
            and i.slot == slot_name
        ]

        print(f"\nCurrent: {current.name if current else 'Empty'}")

        if not armors:
            print("No armor available for this slot.")
            return

        for i, armor in enumerate(armors, 1):

            equipped_text = ""

            if self.is_equipped(armor):
                equipped_text = " [EQUIPPED]"

            print(
                f"{i}. {armor.name} "
                f"(+{armor.value} DEF)"
                f"{equipped_text}"
            )

        print(f"{len(armors) + 1}. Exit")

        choice = input("Choose armor: ").strip()
        clear_screen()

        if choice == str(len(armors) + 1):
            return

        try:

            armor = armors[int(choice) - 1]

            print(f"\nSelected: {armor.name}")
            print("1. Equip")
            print("2. Discard")
            print("3. Cancel")

            action = input("Choose: ").strip()
            clear_screen()

            if action == "1":
                self.equip_item(armor, player)

            elif action == "2":
                self.discard_item(armor, player)

            elif action == "3":
                return

            else:
                print("Invalid choice.")

        except (ValueError, IndexError):

            print("Invalid choice.")

    def discard_armor_menu(self, player):

        armors = [
            i for i in self.items
            if i.itemType == "Armor"
        ]

        print("\n=== DISCARD ARMOR ===")

        if not armors:
            print("No armor available.")
            return

        for i, armor in enumerate(armors, 1):

            equipped_text = ""

            if self.is_equipped(armor):
                equipped_text = " [EQUIPPED]"

            print(
                f"{i}. {armor.name} "
                f"(+{armor.value} DEF)"
                f"{equipped_text}"
            )

        print(f"{len(armors) + 1}. Exit")

        choice = input("Choose armor to discard: ").strip()
        clear_screen()

        if choice == str(len(armors) + 1):
            return

        try:

            armor = armors[int(choice) - 1]
            self.discard_item(armor, player)

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

        choice = input("Choose item: ").strip()
        clear_screen()

        if choice == str(len(items) + 1):
            return

        try:

            item = items[int(choice) - 1]

            print(f"\nSelected: {item.name}")
            print("1. Use")
            print("2. Discard")
            print("3. Cancel")

            action = input("Choose: ").strip()
            clear_screen()

            if action == "1":
                self.use_item(item, player)

            elif action == "2":
                self.discard_item(item, player)

            elif action == "3":
                return

            else:
                print("Invalid choice.")

        except (ValueError, IndexError):

            print("Invalid choice.")