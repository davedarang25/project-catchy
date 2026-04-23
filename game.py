# Do not touch, sample only

import time
import random

class Outpost09:
    def __init__(self):
        # Game State
        self.power = 85
        self.railgun_primed = False
        self.scouts_deployed = 0
        self.engineers_busy = False
        self.diplomacy_score = 0
        self.game_active = True

    def display_status(self):
        print("\n" + "="*30)
        print(f"OUTPOST 09 - COMMAND CONSOLE")
        print(f"Power: {self.power}% | Railgun: {'READY' if self.railgun_primed else 'OFFLINE'}")
        print(f"Scouts Active: {self.scouts_deployed}/3")
        print("="*30)

    def start_game(self):
        print("Tactical Display: 4 mechanized blips crossing the Neutral Zone.")
        print("'Commander, they reach the Red Line in 10 minutes. Orders?'")
        
        while self.game_active:
            self.display_status()
            print("\nChoose your action:")
            print("A. Passive Recon (Shadow with 2 Kestrels)")
            print("B. Fortify & Calibrate (Engineers to Railgun)")
            print("C. The Open Channel (Broadcast Warning)")
            print("D. Combat Readiness (Flank the Red Line)")
            
            choice = input("\nSelection: ").upper()
            self.process_choice(choice)

    def process_choice(self, choice):
        if choice == 'A':
            print("\n[RECON] Kestrels 1 and 2 are moving out. Sensors are painting the targets...")
            time.sleep(1)
            print("Report: Targets identified as 'Iron Guard' Autonomous Walkers. They are heavily armed.")
            self.scouts_deployed = 2
            self.game_active = False # End of prototype turn
            
        elif choice == 'B':
            print("\n[TECH] Engineers are scrambling to the platform. 'Capacitors are screaming, sir!'")
            # Risk/Reward Mechanic
            success = random.random() > 0.3
            if success:
                print("Success: Railgun is online and calibrated.")
                self.railgun_primed = True
            else:
                print("Failure: Power surge! The railgun is locked in a reboot cycle.")
                self.power -= 20
            self.game_active = False

        elif choice == 'C':
            print("\n[DIPLOMACY] Broadcasting on all frequencies...")
            print("'This is Outpost 09. You are approaching sovereign territory. Turn back.'")
            print("The blips pause... but do not retreat. They are testing your resolve.")
            self.diplomacy_score += 1
            self.game_active = False

        elif choice == 'D':
            print("\n[TACTICAL] All Kestrels moving to intercept coordinates.")
            print("Your units are in cover. You have the element of surprise, but you are outgunned.")
            self.scouts_deployed = 3
            self.game_active = False
            
        else:
            print("Invalid command. The enemy is closing in!")

# Run the game
if __name__ == "__main__":
    game = Outpost09()
    game.start_game()