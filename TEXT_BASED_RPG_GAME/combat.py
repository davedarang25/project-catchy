# combat.py
import random


class TurnBasedCombat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_turn = "Player"

    def start_combat(self):
        print(f"\nA {self.enemy.name} appears!")

        while not self.check_combat_end():
            if self.current_turn == "Player":
                self.player_turn()
            else:
                self.enemy_turn()

        return self.end_combat()

    def check_hit(self, attacker, defender):
        base_hit_chance = 0.75

        attacker_accuracy = getattr(attacker, "accuracy", 0)
        defender_dodge = getattr(defender, "dodge", 0)

        hit_chance = base_hit_chance + attacker_accuracy - defender_dodge
        hit_chance = max(0.05, min(hit_chance, 0.95))

        return random.random() <= hit_chance

    def player_turn(self):
        print("\n--- Player Turn ---")
        print(self.player.get_info())
        print(self.enemy.get_info())

        print("\nChoose Action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Defend")

        choice = input("Enter choice: ")

        if choice == "1":
            if self.check_hit(self.player, self.enemy):
                damage = max(1, self.player.attack - self.enemy.defense)
                self.enemy.take_damage(damage)
                print(f"{self.player.name} hit {self.enemy.name} for {damage} damage!")
            else:
                print(f"{self.player.name}'s attack missed!")

        elif choice == "2":
            self.use_item()

        elif choice == "3":
            print(f"{self.player.name} defends and gains temporary defense.")
            self.player.defense += 2

        else:
            print("Invalid choice. Turn skipped.")

        self.current_turn = "Enemy"

    def enemy_turn(self):
        print("\n--- Enemy Turn ---")

        if self.check_hit(self.enemy, self.player):
            damage = max(1, self.enemy.attack - self.player.defense)
            self.player.take_damage(damage)
            print(f"{self.enemy.name} hit {self.player.name} for {damage} damage!")
        else:
            print(f"{self.enemy.name}'s attack missed!")

        self.current_turn = "Player"

    def use_item(self):
        if not self.player.inventory.items:
            print("Inventory is empty.")
            return

        self.player.inventory.show_items()

        try:
            choice = int(input("Choose item number: ")) - 1
            item = self.player.inventory.items[choice]
            item.use(self.player)
            self.player.inventory.remove_item(item)
            print(f"{self.player.name} used {item.name}.")
        except (ValueError, IndexError):
            print("Invalid item choice.")

    def check_combat_end(self):
        return not self.player.is_alive() or not self.enemy.is_alive()

    def end_combat(self):
        if self.player.is_alive():
            print(f"\n{self.player.name} defeated {self.enemy.name}!")

            if hasattr(self.enemy, "exp_reward"):
                self.player.exp += self.enemy.exp_reward
                print(f"Gained {self.enemy.exp_reward} EXP.")

            if hasattr(self.enemy, "gold_reward"):
                self.player.gold += self.enemy.gold_reward
                print(f"Gained {self.enemy.gold_reward} gold.")

            if hasattr(self.enemy, "drop_item"):
                dropped_item = self.enemy.drop_item()

                if dropped_item:
                    self.player.inventory.add_item(dropped_item)
                    print(f"Item received: {dropped_item.name}")

        else:
            print("\nYou were defeated. Game Over.")
            input("\nPress Enter to return to the main menu...")
            return "menu"