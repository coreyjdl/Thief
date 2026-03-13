"""World package — aggregates all chapter data into unified dicts.

Importing from this package gives the same names the rest of the
codebase expects: ITEMS, ENEMIES, LOCATIONS, fresh_enemy, roll_loot,
loc_key_by_name, ENCOUNTER_INTROS, AMBIENT, AMBIENT_CH2.

To add a new chapter, create worlds/chapter<N>.py with ITEMS, ENEMIES,
LOCATIONS, and AMBIENT dicts, then register it below.
"""

from worlds import common
from worlds import chapter1
from worlds import chapter2

# ── Merge chapter dicts into the shared common dicts ────────────────────
common.ITEMS.update(chapter1.ITEMS)
common.ITEMS.update(chapter2.ITEMS)

common.ENEMIES.update(chapter1.ENEMIES)
common.ENEMIES.update(chapter2.ENEMIES)

common.LOCATIONS.update(chapter1.LOCATIONS)
common.LOCATIONS.update(chapter2.LOCATIONS)

# ── Re-export the public API ────────────────────────────────────────────
ITEMS = common.ITEMS
ENEMIES = common.ENEMIES
LOCATIONS = common.LOCATIONS
ENCOUNTER_INTROS = common.ENCOUNTER_INTROS

fresh_enemy = common.fresh_enemy
roll_loot = common.roll_loot
loc_key_by_name = common.loc_key_by_name

# Per-chapter ambient lists
AMBIENT = chapter1.AMBIENT
AMBIENT_CH2 = chapter2.AMBIENT
