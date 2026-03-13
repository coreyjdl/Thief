"""Shared world helpers — enemy spawning, loot rolls, lookups, flavour text."""
import copy
import random

# These get populated by __init__.py after chapter modules load
ITEMS = {}
ENEMIES = {}
LOCATIONS = {}


def fresh_enemy(eid):
    """Return a deep-copy of an enemy template ready for combat."""
    return copy.deepcopy(ENEMIES[eid])


def loc_key_by_name(name):
    """Find location key from its display name."""
    for k, v in LOCATIONS.items():
        if v["name"] == name:
            return k
    return None


def roll_loot(location_id):
    """Roll for ground loot when entering a location. Returns list of items."""
    table = LOCATIONS[location_id].get("loot_table", [])
    found = []
    for item_id in table:
        if random.random() < 0.20:
            found.append(copy.deepcopy(ITEMS[item_id]))
    return found


ENCOUNTER_INTROS = [
    "A figure steps out from the shadows...",
    "Someone's blocking the path ahead...",
    "You hear heavy footsteps behind you...",
    "A kid steps up, cracking his knuckles...",
    "Trouble walks right up to you...",
]
