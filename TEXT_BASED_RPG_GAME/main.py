# main py
# start coding by Clark David Darang 1 May 2026, 8:30pm
import sys
from menu  import show_menu
from gameplay import start_game
from leaderboard import show_leaderboard

def main():
    print("=== Welcome to Exiled Below ===")
    print("A Text-Based RPG Game developed by Dos Productions")
    while True:
        choice = show_menu()

        if choice == '1':
            start_game()

        elif choice == '2':
            show_leaderboard()

        elif choice == '3':
            print()