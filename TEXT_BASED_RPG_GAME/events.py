import random


class RandomEvents:

    def __init__(self):

        self.event_pool = [
            {
                "name": "Healing Fountain",
                "description": "You found a small healing fountain.",
                "effect": "heal",
                "value": 20
            },
            {
                "name": "Hidden Trap",
                "description": "You stepped on a hidden trap!",
                "effect": "damage",
                "value": 15
            },
            {
                "name": "Abandoned Chest",
                "description": "You found gold inside an abandoned chest.",
                "effect": "gold",
                "value": 25
            },
            {
                "name": "Quiet Room",
                "description": "The room is empty. Nothing happens.",
                "effect": "none",
                "value": 0
            },
            {
                "name": "Ancient Shrine",
                "description": "You found an ancient shrine glowing faintly.",
                "effect": "heal",
                "value": 35
            },
            {
                "name": "Lost Coin Pouch",
                "description": "You found a pouch filled with old dungeon coins.",
                "effect": "gold",
                "value": 40
            },
            {
                "name": "Poison Gas",
                "description": "A cloud of poison gas bursts from the walls!",
                "effect": "damage",
                "value": 20
            },
            {
                "name": "Blessed Statue",
                "description": "A cracked statue releases a warm light.",
                "effect": "heal",
                "value": 45
            },
            {
                "name": "Cursed Floor",
                "description": "Dark symbols glow beneath your feet and burn you.",
                "effect": "damage",
                "value": 30
            },
            {
                "name": "Forgotten Treasure Box",
                "description": "You find a small treasure box hidden behind loose stones.",
                "effect": "gold",
                "value": 60
            },
            {
                "name": "Cursed Altar",
                "description": "You find a cursed altar with a black flame burning on top.",
                "effect": "choice",
                "value": 0
            }
        ]

    def get_event(self):

        return random.choice(self.event_pool)

    def trigger_event(self, player):

        event = self.get_event()

        print(f"\nRandom Event: {event['name']}")
        print(event["description"])

        if event["effect"] == "heal":

            old_hp = player.hp

            player.hp = min(
                player.max_hp,
                player.hp + event["value"]
            )

            healed = player.hp - old_hp

            print(f"You restored {healed} HP.")

        elif event["effect"] == "damage":

            player.take_damage(event["value"])

            print(f"You took {event['value']} damage.")

        elif event["effect"] == "gold":

            player.gold += event["value"]

            print(f"You gained {event['value']} gold.")

        elif event["effect"] == "choice":

            self.cursed_altar_choice(player)

        else:

            print("Nothing happened.")

        event_exp = 10

        player.exp += event_exp

        print(f"You gained {event_exp} EXP from the event.")

        if hasattr(player, "check_level_up"):
            player.check_level_up()

    def cursed_altar_choice(self, player):

        print("\nThe altar whispers to you...")
        print("A voice offers you power, but demands a price.")

        print("\nChoose your action:")
        print("1. Touch the black flame")
        print("2. Walk away from the altar")

        choice = input("Choose: ").strip()

        if choice == "1":

            damage = 25
            gold_reward = 75
            exp_reward = 25

            print("\nYou touch the black flame.")
            print("Power rushes through your body, but it burns your soul.")

            player.take_damage(damage)
            player.gold += gold_reward
            player.exp += exp_reward

            print(f"You took {damage} damage.")
            print(f"You gained {gold_reward} gold.")
            print(f"You gained {exp_reward} bonus EXP.")

        elif choice == "2":

            heal_amount = 15

            old_hp = player.hp

            player.hp = min(
                player.max_hp,
                player.hp + heal_amount
            )

            healed = player.hp - old_hp

            print("\nYou step away from the altar.")
            print("The black flame fades, leaving behind a small warmth.")

            print(f"You restored {healed} HP.")

        else:

            damage = 10

            print("\nYou hesitated too long.")
            print("The altar punishes your indecision.")

            player.take_damage(damage)

            print(f"You took {damage} damage.")