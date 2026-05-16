# movement.py
import random


class MovementCycle:

    def __init__(self):

        self.current_floor = 1
        self.current_path = 1
        self.current_location = "Dungeon Entrance"

        self.floor_names = {
            1: "Upper Ruins",
            2: "Rotten Depths",
            3: "Blood Halls",
            4: "Abyssal Keep",
            5: "Emperor's Descent"
        }

        self.floor_entrances = {
            1: "Dungeon Entrance",
            2: "Rotten Depths Entrance",
            3: "Blood Hall Gate",
            4: "Abyssal Keep Entrance",
            5: "Emperor's Descent Gate"
        }

        self.rooms = {
            1: {
                "Left": [
                    "Broken Cell Block",
                    "Collapsed Guard Hall",
                    "Dusty Storage Room",
                    "Old Prison Corridor"
                ],

                "Center": [
                    "Main Entrance Hall",
                    "Cracked Stone Chamber",
                    "Abandoned Shrine",
                    "Silent Crossing"
                ],

                "Right": [
                    "Rusty Armory",
                    "Old Supply Room",
                    "Burned Library",
                    "Forgotten Barracks"
                ]
            },

            2: {
                "Left": [
                    "Rotten Tunnel",
                    "Molded Cellar",
                    "Bone-Filled Passage",
                    "Flooded Prison Hall"
                ],

                "Center": [
                    "Dark Ritual Room",
                    "Underground Chapel",
                    "Old Sacrifice Chamber",
                    "Hollow Stone Hall"
                ],

                "Right": [
                    "Monster Nest",
                    "Spider Den",
                    "Abandoned Kitchen",
                    "Cursed Workshop"
                ]
            },

            3: {
                "Left": [
                    "Blood-Stained Corridor",
                    "Execution Chamber",
                    "Broken Torture Room",
                    "Silent Grave Path"
                ],

                "Center": [
                    "Crimson Hall",
                    "Cursed Throne Room",
                    "Ancient War Room",
                    "Darkened Crossing"
                ],

                "Right": [
                    "Treasure Vault",
                    "Guard Captain Room",
                    "Weapon Storage",
                    "Hidden Supply Chamber"
                ]
            },

            4: {
                "Left": [
                    "Shadow Prison",
                    "Void-Touched Hall",
                    "Fallen Knight Room",
                    "Black Iron Corridor"
                ],

                "Center": [
                    "Abyss Shrine",
                    "Grand Dungeon Passage",
                    "Dark King Hall",
                    "Ancient Seal Room"
                ],

                "Right": [
                    "Cursed Armory",
                    "Wraith Library",
                    "Forgotten Treasury",
                    "War Beast Den"
                ]
            },

            5: {
                "Left": [
                    "Final Prison Wing",
                    "Hall of Broken Crowns",
                    "Black Flame Corridor",
                    "Dead King's Passage"
                ],

                "Center": [
                    "Imperial Throne Path",
                    "Emperor's Gate",
                    "Abyssal Throne Hall",
                    "Final Ritual Chamber"
                ],

                "Right": [
                    "Royal Armory",
                    "Ancient Treasure Vault",
                    "Dragon-Bone Chamber",
                    "Last Guard Barracks"
                ]
            }
        }

    def get_floor_from_total_path(self, total_path):

        floor = ((total_path - 1) // 10) + 1

        if floor > 5:
            floor = 5

        return floor

    def get_path_from_total_path(self, total_path):

        return ((total_path - 1) % 10) + 1

    def sync_with_player_path(self, total_path, player=None):

        old_floor = self.current_floor

        self.current_floor = self.get_floor_from_total_path(total_path)
        self.current_path = self.get_path_from_total_path(total_path)

        floor_changed = self.current_floor != old_floor

        if floor_changed:
            self.current_location = self.floor_entrances[self.current_floor]

        if player:
            player.current_floor = self.current_floor
            player.current_path = self.current_path
            player.current_location = self.current_location

        return floor_changed

    def move_path(self, path_name, total_path, player=None):

        self.sync_with_player_path(
            total_path,
            player
        )

        room_list = self.rooms[self.current_floor][path_name]

        self.current_location = random.choice(room_list)

        if player:
            player.current_floor = self.current_floor
            player.current_path = self.current_path
            player.current_location = self.current_location

    def get_floor_name(self):

        return self.floor_names[self.current_floor]

    def get_room_flavor(self):

        messages = {
            "Dungeon Entrance": "The dungeon mouth waits behind you.",

            "Broken Cell Block": "Old chains hang from the broken walls.",
            "Collapsed Guard Hall": "The ceiling has fallen in several places.",
            "Dusty Storage Room": "Old crates rot in the corners.",
            "Old Prison Corridor": "The walls still carry claw marks.",

            "Main Entrance Hall": "The main hall stretches into darkness.",
            "Cracked Stone Chamber": "The floor is split with deep cracks.",
            "Abandoned Shrine": "A broken shrine watches silently.",
            "Silent Crossing": "Three dark passages meet here.",

            "Rusty Armory": "Rusty weapons line the wall.",
            "Old Supply Room": "Forgotten supplies are scattered around.",
            "Burned Library": "Ash and torn pages cover the floor.",
            "Forgotten Barracks": "Rotten beds and broken armor remain.",

            "Rotten Tunnel": "The smell of decay fills the air.",
            "Molded Cellar": "The walls are wet and covered in mold.",
            "Bone-Filled Passage": "Bones crack beneath your steps.",
            "Flooded Prison Hall": "Cold water reaches your ankles.",

            "Dark Ritual Room": "Old symbols glow faintly on the ground.",
            "Underground Chapel": "A ruined altar stands in silence.",
            "Old Sacrifice Chamber": "The stone floor is stained dark.",
            "Hollow Stone Hall": "Every step echoes loudly.",

            "Monster Nest": "You hear something moving nearby.",
            "Spider Den": "Sticky webs cover the walls.",
            "Abandoned Kitchen": "Broken tools and old bones remain.",
            "Cursed Workshop": "Strange tools lie on blood-marked tables.",

            "Blood-Stained Corridor": "The stones are dark with old blood.",
            "Execution Chamber": "A rusted blade hangs above a broken platform.",
            "Broken Torture Room": "The air feels heavy and cruel.",
            "Silent Grave Path": "Old graves line the path.",

            "Crimson Hall": "Red banners hang from the cracked ceiling.",
            "Cursed Throne Room": "A shattered throne sits in the dark.",
            "Ancient War Room": "Old maps are carved into the stone table.",
            "Darkened Crossing": "The darkness feels alive here.",

            "Treasure Vault": "Broken chests and coins scatter the floor.",
            "Guard Captain Room": "A broken captain's banner lies in the dust.",
            "Weapon Storage": "Old weapons are stacked against the wall.",
            "Hidden Supply Chamber": "Someone once hid supplies here.",

            "Shadow Prison": "The shadows seem to move by themselves.",
            "Void-Touched Hall": "The air feels thin and cold.",
            "Fallen Knight Room": "A dead knight's armor rests against the wall.",
            "Black Iron Corridor": "Black iron bars line the narrow path.",

            "Abyss Shrine": "The shrine hums with dark energy.",
            "Grand Dungeon Passage": "The passage is wide and unnaturally quiet.",
            "Dark King Hall": "A ruined royal crest is carved into the wall.",
            "Ancient Seal Room": "A large seal is cracked in the floor.",

            "Cursed Armory": "The weapons here feel cursed.",
            "Wraith Library": "Ghostly whispers drift between shelves.",
            "Forgotten Treasury": "Gold dust glimmers under broken stone.",
            "War Beast Den": "Deep claw marks cover the floor.",

            "Final Prison Wing": "The cells are sealed with old iron.",
            "Hall of Broken Crowns": "Broken crowns lie scattered like trash.",
            "Black Flame Corridor": "Black flames burn without heat.",
            "Dead King's Passage": "The walls are carved with dead kings.",

            "Imperial Throne Path": "A red carpet leads into the darkness.",
            "Emperor's Gate": "A massive gate blocks the path ahead.",
            "Abyssal Throne Hall": "A throne waits at the end of the hall.",
            "Final Ritual Chamber": "The final ritual circle glows faintly.",

            "Royal Armory": "Royal weapons rest behind cracked glass.",
            "Ancient Treasure Vault": "Ancient treasure is buried in dust.",
            "Dragon-Bone Chamber": "Huge bones form arches across the room.",
            "Last Guard Barracks": "The last guards died here long ago."
        }

        return messages.get(
            self.current_location,
            "The room is eerily quiet..."
        )