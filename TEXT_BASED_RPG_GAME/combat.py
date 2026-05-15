import random
from .logger import Logger
from .utils import clear_screen

logger = Logger(delay=0.02)

class TurnBasedCombat:

    def __init__(self, player, enemy):

        self.player = player
        self.enemy = enemy

        self.current_turn = "Player"

        self.player_guard = False
        self.enemy_guard = False

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

        while True:

            print("\n--- Player Turn ---")

            print(self.player.get_info())
            print(f"EXP: {self.player.get_exp_info()}")
            print(self.enemy.get_info())

            print("\nChoose Action:")
            print("1. Attack")
            print("2. Use Item")
            print("3. Defend")
            print("4. Special Attack")

            choice = input("Enter choice: ").strip()
            clear_screen()
            if choice == "1":

                self.player_attack()
                self.current_turn = "Enemy"
                break

            elif choice == "2":

                used_item = self.use_item()

                if used_item:
                    self.current_turn = "Enemy"
                    break

            elif choice == "3":

                self.player_guard = True

                print(
                    f"{self.player.name} defends "
                    f"and reduces incoming damage."
                )

                self.current_turn = "Enemy"
                break
            elif choice == "4":

                if hasattr(self.player, "special_attack"):

                    if self.check_hit(self.player, self.enemy):
                        self.player.special_attack(self.enemy)
                    else:
                        logger.typewriter(
                            f"{self.player.name}'s special attack missed!"
                        )

                else:
                    logger.typewriter("No special attack available.")
                self.current_turn = "Enemy"
                break
            else:

                print("Invalid choice. Try again.")

    def player_attack(self):

        if self.check_hit(self.player, self.enemy):

            damage = max(
                1,
                self.player.attack - self.enemy.defense
            )

            if self.enemy_guard:
                damage = max(1, damage // 2)

            self.enemy.take_damage(damage)

            print(
                f"{self.player.name} hit "
                f"{self.enemy.name} for "
                f"{damage} damage!"
            )

        else:

            print(f"{self.player.name}'s attack missed!")

        self.enemy_guard = False

    def enemy_turn(self):

        print("\n--- Enemy Turn ---")

        enemy_action = random.choice(
            ["attack", "attack", "attack", "defend"]
        )

        if enemy_action == "defend":

            self.enemy_guard = True

            print(
                f"{self.enemy.name} defends "
                f"and prepares for your next attack."
            )

        else:

            if self.check_hit(self.enemy, self.player):

                if self.player_guard:
                    self.player.defense += 5

                if hasattr(self.enemy, "attack_target"):
                    self.enemy.attack_target(self.player)

                else:

                    damage = max(
                        1,
                        self.enemy.attack - self.player.defense
                    )

                    self.player.take_damage(damage)

                    print(
                        f"{self.enemy.name} hit "
                        f"{self.player.name} for "
                        f"{damage} damage!"
                    )

                if self.player_guard:
                    self.player.defense -= 5

            else:

                print(f"{self.enemy.name}'s attack missed!")

            self.player_guard = False

        self.update_temporary_buffs()

        self.current_turn = "Player"

    def use_item(self):

        consumables = [
            item for item in self.player.inventory.items
            if item.itemType == "Consumable"
        ]

        if not consumables:

            print("No usable items.")
            return False

        print("\n=== CONSUMABLES ===")

        for i, item in enumerate(consumables, 1):
            print(f"{i}. {item.name}")

        print(f"{len(consumables) + 1}. Cancel")

        try:

            choice = int(
                input("Choose item number: ")
            )

            if choice == len(consumables) + 1:
                print("Cancelled.")
                return False

            item = consumables[choice - 1]

            item.use(self.player)
            self.player.inventory.remove_item(item)

            return True

        except (ValueError, IndexError):

            print("Invalid item choice.")
            return False

    def update_temporary_buffs(self):

        if hasattr(self.player, "attack_boost_turns"):

            if self.player.attack_boost_turns > 0:

                self.player.attack_boost_turns -= 1

                if self.player.attack_boost_turns == 0:

                    self.player.attack -= self.player.temp_attack_bonus
                    self.player.temp_attack_bonus = 0

                    print("Your attack boost has worn off.")

        if hasattr(self.player, "defense_boost_turns"):

            if self.player.defense_boost_turns > 0:

                self.player.defense_boost_turns -= 1

                if self.player.defense_boost_turns == 0:

                    self.player.defense -= self.player.temp_defense_bonus
                    self.player.temp_defense_bonus = 0

                    print("Your defense boost has worn off.")

    def remove_temporary_buffs(self):

        if hasattr(self.player, "temp_attack_bonus"):

            if self.player.temp_attack_bonus > 0:

                self.player.attack -= self.player.temp_attack_bonus
                self.player.temp_attack_bonus = 0
                self.player.attack_boost_turns = 0

        if hasattr(self.player, "temp_defense_bonus"):

            if self.player.temp_defense_bonus > 0:

                self.player.defense -= self.player.temp_defense_bonus
                self.player.temp_defense_bonus = 0
                self.player.defense_boost_turns = 0

    def check_combat_end(self):

        return (
            not self.player.is_alive()
            or not self.enemy.is_alive()
        )

    def level_up_check(self):

        if hasattr(self.player, "check_level_up"):
            self.player.check_level_up()

    def end_combat(self):

        self.player_guard = False
        self.enemy_guard = False

        self.remove_temporary_buffs()

        if self.player.is_alive():

            print(
                f"\n{self.player.name} defeated "
                f"{self.enemy.name}!"
            )

            self.player.exp += self.enemy.exp_reward

            print(
                f"Gained {self.enemy.exp_reward} EXP."
            )

            self.player.gold += self.enemy.gold_reward

            print(
                f"Gained {self.enemy.gold_reward} gold."
            )

            dropped_item = self.enemy.drop_item()

            if dropped_item:

                print(
                    f"{self.enemy.name} dropped "
                    f"{dropped_item.name}!"
                )

                item_added = self.player.inventory.add_item(
                    dropped_item,
                    self.player
                )

                if not item_added:

                    print(
                        f"{dropped_item.name} was left behind."
                    )

            self.level_up_check()

            print(f"EXP: {self.player.get_exp_info()}")

            return "win"

        print("\nYou were defeated. Game Over.")
        return "dead"