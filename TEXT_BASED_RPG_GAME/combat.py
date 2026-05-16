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

        # Special attack cooldown
        # 0 means ready
        self.special_cooldown = 0

    # =========================
    # UI HELPERS
    # =========================

    def hp_bar(self, current, maximum, length=20):

        if maximum <= 0:
            maximum = 1

        filled = int((current / maximum) * length)

        if filled < 0:
            filled = 0

        if filled > length:
            filled = length

        empty = length - filled

        return "[" + ("█" * filled) + (" " * empty) + "]"

    def special_ready(self):

        return self.special_cooldown == 0

    def turns_until_special(self):

        return self.special_cooldown

    def advance_player_turn(self, used_special=False):

        if used_special:

            self.special_cooldown = 3

        else:

            if self.special_cooldown > 0:
                self.special_cooldown -= 1

    def show_combat_ui(self):

        print("\n" + "=" * 55)
        print("                     COMBAT")
        print("=" * 55)

        print(
            f"\n{self.player.name} "
            f"(Lv {self.player.level})"
        )

        print(
            f"HP  : {self.player.hp}/{self.player.max_hp} "
            f"{self.hp_bar(self.player.hp, self.player.max_hp)}"
        )

        print(
            f"ATK : {self.player.attack} | "
            f"DEF : {self.player.defense}"
        )

        print(f"EXP : {self.player.get_exp_info()}")

        if self.player_guard:
            print("STATUS: Guarding")

        if getattr(self.player, "attack_boost_turns", 0) > 0:
            print(
                f"ATK BOOST: +{self.player.temp_attack_bonus} "
                f"({self.player.attack_boost_turns} turns)"
            )

        if getattr(self.player, "defense_boost_turns", 0) > 0:
            print(
                f"DEF BOOST: +{self.player.temp_defense_bonus} "
                f"({self.player.defense_boost_turns} turns)"
            )

        print("\n" + "-" * 55)

        print(
            f"\n{self.enemy.name} "
            f"(Lv {self.enemy.level})"
        )

        print(
            f"HP  : {self.enemy.hp}/{self.enemy.max_hp} "
            f"{self.hp_bar(self.enemy.hp, self.enemy.max_hp)}"
        )

        print(
            f"ATK : {self.enemy.attack} | "
            f"DEF : {self.enemy.defense}"
        )

        if self.enemy_guard:
            print("STATUS: Guarding")

        print("=" * 55)

    def show_action_menu(self):

        print("\nChoose Action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Defend")

        if self.special_ready():
            print("4. Special Attack [READY]")
        else:
            print(
                f"4. Special Attack "
                f"[Cooldown: {self.turns_until_special()} turn(s)]"
            )

    # =========================
    # COMBAT MAIN LOOP
    # =========================

    def start_combat(self):

        clear_screen()

        print("\n" + "=" * 55)
        print(f"A {self.enemy.name} appears!")
        print("=" * 55)

        while not self.check_combat_end():

            if self.current_turn == "Player":
                self.player_turn()

            else:
                self.enemy_turn()

        return self.end_combat()

    # =========================
    # HIT CHECK
    # =========================

    def check_hit(self, attacker, defender):

        base_hit_chance = 0.75

        attacker_accuracy = getattr(attacker, "accuracy", 0)
        defender_dodge = getattr(defender, "dodge", 0)

        hit_chance = base_hit_chance + attacker_accuracy - defender_dodge
        hit_chance = max(0.05, min(hit_chance, 0.95))

        return random.random() <= hit_chance

    # =========================
    # PLAYER TURN
    # =========================

    def player_turn(self):

        while True:

            print("\n--- Player Turn ---")

            self.show_combat_ui()
            self.show_action_menu()

            choice = input("\nEnter choice: ").strip()
            clear_screen()

            if choice == "1":

                self.player_attack()

                self.current_turn = "Enemy"
                self.advance_player_turn()

                break

            elif choice == "2":

                used_item = self.use_item()

                if used_item:

                    self.current_turn = "Enemy"
                    self.advance_player_turn()

                    break

            elif choice == "3":

                self.player_guard = True

                print(
                    f"{self.player.name} defends "
                    f"and reduces incoming damage."
                )

                self.current_turn = "Enemy"
                self.advance_player_turn()

                break

            elif choice == "4":

                if not self.special_ready():

                    print(
                        f"Special Attack is still on cooldown. "
                        f"{self.turns_until_special()} turn(s) remaining."
                    )

                    continue

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
                self.advance_player_turn(used_special=True)

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

    # =========================
    # ENEMY TURN
    # =========================

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

    # =========================
    # ITEMS
    # =========================

    def use_item(self):

        consumables = [
            item for item in self.player.inventory.items
            if item.itemType == "Consumable"
        ]

        if not consumables:

            print("No usable items.")
            return False

        print("\n" + "=" * 45)
        print("                 ITEMS")
        print("=" * 45)

        for i, item in enumerate(consumables, 1):
            print(f"{i}. {item.name}")

        print(f"{len(consumables) + 1}. Cancel")
        print("=" * 45)

        try:

            choice = int(
                input("Choose item number: ")
            )

            clear_screen()

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

    # =========================
    # TEMPORARY BUFFS
    # =========================

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

    # =========================
    # COMBAT END
    # =========================

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

            print("\n" + "=" * 45)
            print("                 VICTORY")
            print("=" * 45)

            print(
                f"{self.player.name} defeated "
                f"{self.enemy.name}!"
            )

            print("\nRewards")
            print("-" * 45)

            self.player.exp += self.enemy.exp_reward

            print(f"EXP Gained  : {self.enemy.exp_reward}")

            self.player.gold += self.enemy.gold_reward

            print(f"Gold Gained : {self.enemy.gold_reward}")

            dropped_item = self.enemy.drop_item()

            if dropped_item:

                print(f"Item Drop   : {dropped_item.name}")

                item_added = self.player.inventory.add_item(
                    dropped_item,
                    self.player
                )

                if not item_added:

                    print(
                        f"{dropped_item.name} was left behind."
                    )

            else:

                print("Item Drop   : None")

            print("-" * 45)

            self.level_up_check()

            print("\nCurrent Status")
            print("-" * 45)
            print(f"HP   : {self.player.hp}/{self.player.max_hp}")
            print(f"ATK  : {self.player.attack}")
            print(f"DEF  : {self.player.defense}")
            print(f"Gold : {self.player.gold}")
            print(f"EXP  : {self.player.get_exp_info()}")
            print("=" * 45)

            input("\nPress Enter to continue...")
            clear_screen()

            return "win"

        print("\n" + "=" * 45)
        print("                 DEFEAT")
        print("=" * 45)

        print("\nYou were defeated. Game Over.")

        input("\nPress Enter to continue...")
        clear_screen()

        return "dead"