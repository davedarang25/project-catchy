# logger.py
import sys
import time


class Logger:
    def __init__(self, delay=10):
        self.delay = delay
        self.buffer = []

    def log(self, message):
        self.buffer.append(message)

    def display_buffer(self):
        for message in self.buffer:
            self.typewriter(message)
        self.clear_buffer()

    def typewriter(self, message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(self.delay)
        print()

    def loading(self, message="Loading", dots=3):
        sys.stdout.write(message)
        sys.stdout.flush()

        for _ in range(dots):
            time.sleep(0.4)
            sys.stdout.write(".")
            sys.stdout.flush()

        print()

    def clear_buffer(self):
        self.buffer.clear()