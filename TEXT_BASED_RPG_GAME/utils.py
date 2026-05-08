# utils.py
import os
import time


def clear_screen():
    """
    Clears the terminal screen.
    Works on Windows and Linux/macOS.
    """

    os.system("cls" if os.name == "nt" else "clear")


def pause(seconds=1):
    """
    Pauses the program for a short time.
    """

    time.sleep(seconds)