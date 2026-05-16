from .logger import Logger
import sys
import time


logger = Logger(delay=0.005)


def enter_pressed():

    if sys.platform.startswith("win"):

        import msvcrt

        if msvcrt.kbhit():

            key = msvcrt.getwch()

            if key == "\r":
                return True

        return False

    else:

        import select

        readable, _, _ = select.select(
            [sys.stdin],
            [],
            [],
            0
        )

        if readable:
            sys.stdin.readline()
            return True

        return False


def log_block(text):

    lines = text.splitlines()
    skip = False

    for line_index, line in enumerate(lines):

        if skip:
            print(line)
            continue

        for char_index, char in enumerate(line):

            if enter_pressed():

                print(line[char_index:], end="")
                skip = True
                break

            print(char, end="", flush=True)
            time.sleep(logger.delay)

        print()


def show_menu():

    log_block(r"""
=============================================================
                    EXILED BELOW
              A Text-Based Roguelike RPG
=============================================================

         _____________________________________________
        |.'',                                     ,''.|
        |.'.'',                                 ,''.'.|
        |.'.'.'',                             ,''.'.'.|
        |.'.'.'.'',                         ,''.'.'.'.|
        |.'.'.'.'.|                         |.'.'.'.'.|
        |.'.'.'.'.|===;                 ;===|.'.'.'.'.|
        |.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
        |.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
        |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
        |,',',',',|---|',|'|???????|'|,'|---|,',',',',|
        |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
        |.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
        |.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
        |.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
        |.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
        |.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
        |.'.','         /%%%%%%%%%%%%%\         ','.'.|
        |.','          /%%%%%%%%%%%%%%%\          ','.|
        |;____________/%%%%%%%%%%%%%%%%%\____________;|

            "Your only goal is to keep moving."

=============================================================
                         MAIN MENU
=============================================================

    [1] Start Game
    [2] Leaderboard
    [3] Exit

=============================================================
""")

    choice = input("Choose an option: ").strip()

    return choice