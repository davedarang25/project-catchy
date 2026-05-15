from .item import Item
from .utils import clear_screen


class Inventory:

    def __init__(self, capacity=20):

        self.capacity = capacity
        self.items = []

        self.weapon = None
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.shield = None

    # =========================
    # UI HELPERS
    # =========================

    def line(self, length=50):

        print("=" * length)

    def small_line(self, length=50):

        print("-" * length)

    def pause(self):

        input("\nPress Enter to continue...")
        clear_screen()

    def slot_display(self, item):

        if item:
            return item.name

        return "Empty"

    def item_display(self, item):

        equipped_text = ""

        if self.is_equipped(item):
            equipped_text = " [EQUIPPED]"

        return f"{item.get_info()}{equipped_text}"

    # =========================
    # BASIC CHECKS
    # =========================

    def is_empty(self):

        return len(self.items) == 0

    def is_full(self):

        return len(self.items) >= self.capacity

    # =========================
    # ADD / REMOVE
    # =========================

    def add_item(self, item: Item, player=None):

        if self.is_full():

            clear_screen()

            self.line()
            print("              BAG FULL")
            self.line()

            print(f"\nYou cannot carry: {item.name}")
            print(f"Capacity: {len(self.items)}/{self.capacity}")

            print("\nDo you want to discard an item?")
            print("1. Yes")
            print("2. No")

            choice = input("\nChoose: ").strip()
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

    # =========================
    # DISPLAY ITEMS
    # =========================

    def show_items(self):

        clear_screen()

        self.line()
        print("              INVENTORY")
        self.line()

        print(f"Capacity: {len(self.items)}/{self.capacity}")

        if self.is_full():
            print("WARNING: Bag is full!")

        if self.is_empty():

            print("\nInventory is empty.")
            self.pause()
            return

        print()

        for i, item in enumerate(self.items, 1):

            print(f"{i}. {self.item_display(item)}")

        self.pause()

    def view_all_items_menu(self, player):

        while True:

            clear_screen()

            self.line()
            print("              ALL ITEMS")
            self.line()

            print(f"Capacity: {len(self.items)}/{self.capacity}")

            if self.is_full():
                print("WARNING: Bag is full!")

            if self.is_empty():

                print("\nInventory is empty.")
                self.pause()
                return

            print()

            for i, item in enumerate(self.items, 1):

                print(f"{i}. {self.item_display(item)}")

            print(f"{len(self.items) + 1}. Back")

            choice = input("\nChoose item: ").strip()
            clear_screen()

            if choice == str(len(self.items) + 1):
                return

            try:

                item = self.items[int(choice) - 1]

            except (ValueError, IndexError):

                print("Invalid choice.")
                self.pause()
                continue

            self.selected_item_menu(item, player)

    def selected_item_menu(self, item, player):

        while True:

            clear_screen()

            self.line()
            print("             SELECTED ITEM")
            self.line()

            print(f"Name   : {item.name}")
            print(f"Type   : {item.itemType}")
            print(f"Rarity : {item.rarity}")
            print(f"Info   : {item.description}")

            if item.itemType == "Weapon":
                print(f"ATK    : +{item.value}")

            elif item.itemType == "Armor":
                print(f"DEF    : +{item.value}")
                print(f"Slot   : {item.slot}")

            elif item.itemType == "Consumable":
                print(f"Value  : {item.value}")

            if self.is_equipped(item):
                print("Status : EQUIPPED")

            self.small_line()

            if item.itemType in ["Weapon", "Armor"]:

                print("1. Equip")
                print("2. Discard")
                print("3. Back")

                choice = input("\nChoose: ").strip()

                if choice == "1":
                    clear_screen()
                    self.equip_item(item, player)
                    self.pause()
                    return

                elif choice == "2":
                    clear_screen()
                    self.discard_item(item, player)
                    self.pause()
                    return

                elif choice == "3":
                    return

                else:
                    print("Invalid choice.")
                    self.pause()

            elif item.itemType == "Consumable":

                print("1. Use")
                print("2. Discard")
                print("3. Back")

                choice = input("\nChoose: ").strip()

                if choice == "1":
                    clear_screen()
                    self.use_item(item, player)
                    self.pause()
                    return

                elif choice == "2":
                    clear_screen()
                    self.discard_item(item, player)
                    self.pause()
                    return

                elif choice == "3":
                    return

                else:
                    print("Invalid choice.")
                    self.pause()

            else:

                print("Unknown item type.")
                self.pause()
                return

    # =========================
    # EQUIPPED CHECK
    # =========================

    def is_equipped(self, item):

        return (
            item == self.weapon
            or item == self.helmet
            or item == self.chestplate
            or item == self.leggings
            or item == self.shield
        )

    # =========================
    # EQUIP / UNEQUIP
    # =========================

    def equip_item(self, item, player):

        if item not in self.items:

            print("Item not found in inventory.")
            return

        if item.itemType == "Weapon":

            if item == self.weapon:

                print(f"{item.name} is already equipped.")
                return

            if self.weapon:
                player.attack -= self.weapon.value

            self.weapon = item
            player.attack += item.value

            print(f"{item.name} equipped as weapon.")

        elif item.itemType == "Armor":

            slot_name = item.slot

            if not hasattr(self, slot_name):

                print("Invalid armor slot.")
                return

            current = getattr(self, slot_name)

            if current == item:

                print(f"{item.name} is already equipped.")
                return

            if current:
                player.defense -= current.value

            setattr(self, slot_name, item)
            player.defense += item.value

            print(f"{item.name} equipped to {slot_name}.")

        else:

            print("This item cannot be equipped.")

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

    # =========================
    # DISCARD
    # =========================

    def discard_item(self, item, player=None):

        if item not in self.items:

            print("Item not found.")
            return False

        self.line()
        print("             DISCARD ITEM")
        self.line()

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

            clear_screen()

            self.line()
            print("             DISCARD ITEM")
            self.line()

            print(f"Capacity: {len(self.items)}/{self.capacity}")

            if self.is_full():
                print("WARNING: Bag is full!")

            print()

            for i, item in enumerate(self.items, 1):

                equipped_text = ""

                if self.is_equipped(item):
                    equipped_text = " [EQUIPPED]"

                print(f"{i}. {item.name}{equipped_text}")

            print(f"{len(self.items) + 1}. Cancel")

            choice = input("\nChoose item to discard: ").strip()

            if choice == str(len(self.items) + 1):
                return False

            try:

                item = self.items[int(choice) - 1]
                clear_screen()
                return self.discard_item(item, player)

            except (ValueError, IndexError):

                print("Invalid choice.")
                self.pause()

    # =========================
    # USE ITEM
    # =========================

    def use_item(self, item, player):

        if item not in self.items:

            print("Item not found.")
            return

        if item.itemType != "Consumable":

            print("You cannot use that item.")
            return

        item.use(player)
        self.remove_item(item)

    # =========================
    # MAIN INVENTORY MENU
    # =========================

    def inventory_menu(self, player):

        while True:

            clear_screen()

            self.line()
            print("              INVENTORY")
            self.line()

            print("PLAYER STATS")
            self.small_line()
            print(f"HP    : {player.hp}/{player.max_hp}")
            print(f"ATK   : {player.attack}")
            print(f"DEF   : {player.defense}")
            print(f"GOLD  : {player.gold}")
            print(f"EXP   : {player.get_exp_info()}")
            print(f"LEVEL : {player.level}")

            print()
            print("EQUIPPED ITEMS")
            self.small_line()
            print(f"Weapon : {self.slot_display(self.weapon)}")
            print(f"Helmet : {self.slot_display(self.helmet)}")
            print(f"Chest  : {self.slot_display(self.chestplate)}")
            print(f"Legs   : {self.slot_display(self.leggings)}")
            print(f"Shield : {self.slot_display(self.shield)}")

            print()
            print(f"Bag Capacity: {len(self.items)}/{self.capacity}")

            if self.is_full():
                print("WARNING: Bag is full!")

            self.line()
            print("1. Weapon")
            print("2. Armor")
            print("3. Items")
            print("4. View All Items")
            print("5. Discard Item")
            print("6. Exit")
            self.line()

            choice = input("Choose: ").strip()

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
                clear_screen()
                break

            else:
                print("Invalid choice.")
                self.pause()

    # =========================
    # WEAPON MENU
    # =========================

    def weapon_menu(self, player):

        while True:

            clear_screen()

            weapons = [
                item for item in self.items
                if item.itemType == "Weapon"
            ]

            self.line()
            print("               WEAPONS")
            self.line()

            print(f"Current Weapon: {self.slot_display(self.weapon)}")
            self.small_line()

            if not weapons:

                print("No weapons available.")
                self.pause()
                return

            for i, weapon in enumerate(weapons, 1):

                equipped_text = ""

                if weapon == self.weapon:
                    equipped_text = " [EQUIPPED]"

                print(
                    f"{i}. {weapon.name:<25} "
                    f"ATK +{weapon.value:<3}"
                    f"{equipped_text}"
                )

            print(f"{len(weapons) + 1}. Back")

            choice = input("\nChoose weapon: ").strip()

            if choice == str(len(weapons) + 1):
                return

            try:

                weapon = weapons[int(choice) - 1]

            except (ValueError, IndexError):

                print("Invalid choice.")
                self.pause()
                continue

            self.selected_item_menu(weapon, player)

    # =========================
    # ARMOR MENU
    # =========================

    def armor_menu(self, player):

        while True:

            clear_screen()

            self.line()
            print("                ARMOR")
            self.line()

            print(f"Helmet     : {self.slot_display(self.helmet)}")
            print(f"Chestplate : {self.slot_display(self.chestplate)}")
            print(f"Leggings   : {self.slot_display(self.leggings)}")
            print(f"Shield     : {self.slot_display(self.shield)}")

            self.small_line()
            print("1. Helmet")
            print("2. Chestplate")
            print("3. Leggings")
            print("4. Shield")
            print("5. Discard Armor")
            print("6. Back")
            self.line()

            slot = input("Choose: ").strip()

            if slot == "6":
                return

            if slot == "5":
                self.discard_armor_menu(player)
                continue

            slot_map = {
                "1": "helmet",
                "2": "chestplate",
                "3": "leggings",
                "4": "shield"
            }

            if slot not in slot_map:

                print("Invalid slot.")
                self.pause()
                continue

            self.armor_slot_menu(
                player,
                slot_map[slot]
            )

    def armor_slot_menu(self, player, slot_name):

        while True:

            clear_screen()

            current = getattr(self, slot_name)

            armors = [
                item for item in self.items
                if item.itemType == "Armor"
                and item.slot == slot_name
            ]

            self.line()
            print(f"              {slot_name.upper()}")
            self.line()

            print(f"Current: {self.slot_display(current)}")
            self.small_line()

            if not armors:

                print("No armor available for this slot.")
                self.pause()
                return

            for i, armor in enumerate(armors, 1):

                equipped_text = ""

                if self.is_equipped(armor):
                    equipped_text = " [EQUIPPED]"

                print(
                    f"{i}. {armor.name:<25} "
                    f"DEF +{armor.value:<3}"
                    f"{equipped_text}"
                )

            print(f"{len(armors) + 1}. Back")

            choice = input("\nChoose armor: ").strip()

            if choice == str(len(armors) + 1):
                return

            try:

                armor = armors[int(choice) - 1]

            except (ValueError, IndexError):

                print("Invalid choice.")
                self.pause()
                continue

            self.selected_item_menu(armor, player)

    def discard_armor_menu(self, player):

        while True:

            clear_screen()

            armors = [
                item for item in self.items
                if item.itemType == "Armor"
            ]

            self.line()
            print("            DISCARD ARMOR")
            self.line()

            if not armors:

                print("No armor available.")
                self.pause()
                return

            for i, armor in enumerate(armors, 1):

                equipped_text = ""

                if self.is_equipped(armor):
                    equipped_text = " [EQUIPPED]"

                print(
                    f"{i}. {armor.name:<25} "
                    f"DEF +{armor.value:<3}"
                    f"{equipped_text}"
                )

            print(f"{len(armors) + 1}. Back")

            choice = input("\nChoose armor to discard: ").strip()

            if choice == str(len(armors) + 1):
                return

            try:

                armor = armors[int(choice) - 1]
                clear_screen()
                self.discard_item(armor, player)
                self.pause()
                return

            except (ValueError, IndexError):

                print("Invalid choice.")
                self.pause()

    # =========================
    # ITEM MENU
    # =========================

    def item_menu(self, player):

        while True:

            clear_screen()

            items = [
                item for item in self.items
                if item.itemType == "Consumable"
            ]

            self.line()
            print("                ITEMS")
            self.line()

            if not items:

                print("No usable items available.")
                self.pause()
                return

            for i, item in enumerate(items, 1):

                print(f"{i}. {item.get_info()}")

            print(f"{len(items) + 1}. Back")

            choice = input("\nChoose item: ").strip()

            if choice == str(len(items) + 1):
                return

            try:

                item = items[int(choice) - 1]

            except (ValueError, IndexError):

                print("Invalid choice.")
                self.pause()
                continue

            self.selected_item_menu(item, player)