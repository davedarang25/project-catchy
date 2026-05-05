# movement py
class MovementCycle:
    def __init__(self, startLocation="Entrance", mapData=None):
        self.currentLocation = startLocation
        self.mapData = mapData if mapData else {
            "Entrance": {"north": "Hallway", "east": None, "south": None, "west":None},
            "Hallway": {"north": "Treasure Room", "east": "Armory", "south": "Entrance", "east": None},
            "Treasure Room": {"south": "Hallway"},
            "Armory": {"west": "Hallway"}
        }

    def showLocation(self):
        print(f"You are now at: {self.currentLocation}")

    def move(self, direction: str):
        if self.checkPath(direction):
            self.currentLocation = self.mapData(self.currentLocation)[direction]
            print(f"You move {direction} to {self.currentLocation}.")
            self.checkEvent()
        else:
            print(f"The path {direction} is blocked.")

    def checkEvent(self):
        # Placeholder: events tied to locations
        if self.currentLocation == "Treasure Room":
            print("You a chest of gold!")
        elif self.currentLocation == "Armory":
            print("You discover old weapons and armoor.")
        else:
            print("The room is eerily quiet...")

    def checkEncounter(self):
        # Placeholder random encounter logic
        import random
        encounter = random.choice([True, False])
        if encounter:
            print("An enemy appears!")
        return encounter
    
    def checkPath(self, direction: str):
        """Return True if path is possible, False if blocked."""
        if direction in self.mapData[self.currentLocation]:
            return self.mapData[self.currentLocation][direction] is not None
        return False