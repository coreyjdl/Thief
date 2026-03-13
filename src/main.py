"""THIEF — A text-based crime RPG.  Run this file to play."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui import enable_ansi
from game import Game


def main():
    enable_ansi()
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\n\n  Later.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()

