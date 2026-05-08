# combat.py
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

        logger.typewriter(f"\nA {self.enemy.name} appears!")

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

    def calculate_damage(self, attacker, defender, defender_guard):

        damage = max(
            1,
            attacker.attack - defender.defense
        )

        if defender_guard:
            damage = max(1, damage // 2)

        return damage

    def player_turn(self):

        print("\n--- Player Turn ---")

        print(self.player.get_info())
        print(self.enemy.get_info())

        print("\nChoose Action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Defend")

        choice = input("Enter choice: ").strip()
        clear_screen()
        if choice == "1":

            if self.check_hit(self.player, self.enemy):

                damage = self.calculate_damage(
                    self.player,
                    self.enemy,
                    self.enemy_guard
                )

                self.enemy.take_damage(damage)

                logger.typewriter(
                    f"{self.player.name} hit "
                    f"{self.enemy.name} for "
                    f"{damage} damage!"
                )

            else:

                logger.typewriter(f"{self.player.name}'s attack missed!")

            self.enemy_guard = False

        elif choice == "2":

            self.use_item()

        elif choice == "3":

            self.player_guard = True

            logger.typewriter(
                f"{self.player.name} defends "
                f"and reduces incoming damage."
            )

        else:

            logger.typewriter("Invalid choice. Turn skipped.")

        self.current_turn = "Enemy"

    def enemy_turn(self):

        print("\n--- Enemy Turn ---")

        enemy_action = random.choice(["attack", "attack", "defend"])

        if enemy_action == "defend":

            self.enemy_guard = True

            logger.typewriter(
                f"{self.enemy.name} defends "
                f"and prepares for your next attack."
            )

        else:

            if self.check_hit(self.enemy, self.player):

                damage = self.calculate_damage(
                    self.enemy,
                    self.player,
                    self.player_guard
                )

                self.player.take_damage(damage)

                logger.typewriter(
                    f"{self.enemy.name} hit "
                    f"{self.player.name} for "
                    f"{damage} damage!"
                )

            else:

                logger.typewriter(f"{self.enemy.name}'s attack missed!")

            self.player_guard = False

        self.current_turn = "Player"

    def use_item(self):

        consumables = [
            item for item in self.player.inventory.items
            if item.itemType == "Consumable"
        ]

        if not consumables:

            logger.typewriter("No usable items.")
            return

        print("\n=== Consumables ===")

        for i, item in enumerate(consumables, 1):
            print(f"{i}. {item.name}")

        print(f"{len(consumables) + 1}. Cancel")

        try:

            choice = int(input("Choose item number: "))

            if choice == len(consumables) + 1:
                logger.typewriter("Cancelled.")
                return

            item = consumables[choice - 1]

            item.use(self.player)
            self.player.inventory.remove_item(item)

            logger.typewriter(f"{self.player.name} used {item.name}.")

        except (ValueError, IndexError):

            logger.typewriter("Invalid item choice.")

    def check_combat_end(self):

        return (
            not self.player.is_alive()
            or not self.enemy.is_alive()
        )

    def level_up_check(self):

        required_exp = self.player.level * 100

        while self.player.exp >= required_exp:

            self.player.exp -= required_exp
            self.player.level += 1

            self.player.max_hp += 20
            self.player.hp = self.player.max_hp

            self.player.attack += 3
            self.player.defense += 2

            logger.typewriter("\nLEVEL UP!")
            logger.typewriter(
                f"{self.player.name} is now level {self.player.level}!"
            )

            required_exp = self.player.level * 100

    def end_combat(self):

        self.player_guard = False
        self.enemy_guard = False

        if self.player.is_alive():

            logger.typewriter(
                f"\n{self.player.name} defeated "
                f"{self.enemy.name}!"
            )

            self.player.exp += self.enemy.exp_reward

            logger.typewriter(
                f"Gained {self.enemy.exp_reward} EXP."
            )

            self.player.gold += self.enemy.gold_reward

            logger.typewriter(
                f"Gained {self.enemy.gold_reward} gold."
            )

            dropped_item = self.enemy.drop_item()

            if dropped_item:

                logger.typewriter(
                    f"{self.enemy.name} dropped "
                    f"{dropped_item.name}!"
                )

                self.player.inventory.add_item(dropped_item)

            self.level_up_check()

            return "win"

        logger.typewriter("\nYou were defeated. Game Over.")
        return "dead"