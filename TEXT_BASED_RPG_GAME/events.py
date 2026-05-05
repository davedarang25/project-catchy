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
            }
        ]

    def get_event(self):
        return random.choice(self.event_pool)

    def trigger_event(self, player):
        event = self.get_event()

        print(f"\nRandom Event: {event['name']}")
        print(event["description"])

        if event["effect"] == "heal":
            player.hp = min(player.max_hp, player.hp + event["value"])
            print(f"You restored {event['value']} HP.")

        elif event["effect"] == "damage":
            player.take_damage(event["value"])
            print(f"You took {event['value']} damage.")

        elif event["effect"] == "gold":
            player.gold += event["value"]
            print(f"You gained {event['value']} gold.")

        else:
            print("Nothing happened.")