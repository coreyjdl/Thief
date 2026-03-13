"""Terminal UI utilities — text formatting, input, ANSI helpers."""
import os
import sys
import time


def enable_ansi():
    """Enable ANSI escape codes on Windows 10+."""
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        except Exception:
            pass


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def typewriter(text, speed=0.025):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def slow_print(text, speed=0.012):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def narrate(text, speed=0.018):
    """Print narrative text with punctuation pauses."""
    if not text:
        print()
        return
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in '.!?':
            time.sleep(0.25)
        elif char == ',':
            time.sleep(0.12)
        else:
            time.sleep(speed)
    print()


def prompt():
    return input("\n>>> ").strip().lower()


def divider(width=56):
    print("─" * width)


def header(text, width=56):
    print("═" * width)
    padding = (width - len(text)) // 2
    print(" " * padding + text)
    print("═" * width)


def pause(msg="\n  Press Enter to continue..."):
    input(msg)


def choice_menu(options):
    """Display numbered choices, return selected index."""
    print()
    for i, opt in enumerate(options, 1):
        print(f"  [{i}] {opt}")
    print()
    while True:
        try:
            c = input("  >>> ").strip()
            idx = int(c) - 1
            if 0 <= idx < len(options):
                return idx
        except (ValueError, EOFError):
            pass
        print("  Pick a number from the list.")


def status_bar(player):
    bar_len = player.max_hp // 3
    filled = max(0, player.hp // 3)
    empty = bar_len - filled
    hp_bar = "█" * filled + "░" * empty
    rank = player.get_rank()
    print(f"  HP [{hp_bar}] {player.hp}/{player.max_hp}  |  "
          f"Respect: {player.respect}  |  ${player.money}  |  {rank}")


def dialogue(speaker, text, color=None):
    if color:
        print(f"  \033[{color}m{speaker}:\033[0m \"{text}\"")
    else:
        print(f"  {speaker}: \"{text}\"")
