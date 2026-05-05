# inventory py
from item import Item

class Inventory:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len (self.items) == 0
    
    def is_full(self):
        return len(self.items) >= self.capacity
    
    def add_item(self, item: Item):
        if self.is_full():
            print("Inventory is full. Cannot add item.")
            return False
        self.items.append(item)
        print(f"{item.name} added to inventory.")
        return True
    
    def remove_item(self, item: Item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} removed from inventory")
            return True
        print(f"{item.name} not found in inventory.")

    def use_item(self, item: Item, user):
        if item in self.items:
            item.use(user)
            # if consumable, remove after use
            if item.itemType == "Consumable":
                self.remove_item(item)
        else:
            print(f"{item.name} not found in inventory.")

    def show_items(self):
        if self.is_empty():
            print("No Items")
        else:
            print("\=== Inventory ===")
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item.get_info()}")