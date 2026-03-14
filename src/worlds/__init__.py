"""World package — aggregates all chapter data into unified dicts.

Importing from this package gives the same names the rest of the
codebase expects: ITEMS, ENEMIES, LOCATIONS, fresh_enemy, roll_loot,
loc_key_by_name, ENCOUNTER_INTROS, AMBIENT, AMBIENT_CH2, CHAPTERS.

To add a new chapter, create worlds/chapter<N>.py with META, ITEMS,
ENEMIES, LOCATIONS, and AMBIENT — it will be auto-registered.
"""

from worlds import common
from worlds import chapter1
from worlds import chapter2
from worlds import chapter3
from worlds import chapter4
from worlds import chapter5
from worlds import chapter6
from worlds import chapter7
from worlds import chapter8

# Ordered list of all chapter modules
_ALL_CHAPTERS = [
    chapter1, chapter2, chapter3, chapter4,
    chapter5, chapter6, chapter7, chapter8,
]

# ── Merge chapter dicts into the shared common dicts ────────────────────
for _ch in _ALL_CHAPTERS:
    common.ITEMS.update(getattr(_ch, "ITEMS", {}))
    common.ENEMIES.update(getattr(_ch, "ENEMIES", {}))
    common.LOCATIONS.update(getattr(_ch, "LOCATIONS", {}))

# ── Chapter metadata registry ──────────────────────────────────────────
CHAPTERS = {ch.META["number"]: ch.META for ch in _ALL_CHAPTERS}
CHAPTER_AMBIENT = {ch.META["number"]: ch.AMBIENT for ch in _ALL_CHAPTERS}

# ── Re-export the public API ────────────────────────────────────────────
ITEMS = common.ITEMS
ENEMIES = common.ENEMIES
LOCATIONS = common.LOCATIONS
ENCOUNTER_INTROS = common.ENCOUNTER_INTROS

fresh_enemy = common.fresh_enemy
roll_loot = common.roll_loot
loc_key_by_name = common.loc_key_by_name

# Backward-compatible ambient exports
AMBIENT = chapter1.AMBIENT
AMBIENT_CH2 = chapter2.AMBIENT
