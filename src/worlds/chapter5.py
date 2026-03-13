"""Chapter 5 — The Row: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  Commercial row — corner stores, bodegas, laundromats used as
          fronts. The legitimate-looking side of crime.
Age:      20–22 (early twenties, experienced street operator).
Boss:     Corrupt store owner with bodyguards — runs a laundering network.
Weapons:  Knife, cheap pistol (first ranged weapon).
Actions:  Rob corner stores (armed robbery missions).
Music:    Tension / suspense — ticking clocks, police scanners.

BOSS FIGHT
──────────
- Store owner doesn't fight alone — has 2 bodyguards (multi-phase fight?).
- Need intel before attempting (case the joint, learn routines).
- Reward: cash flow from the row, connections to bigger operations.

LOCATIONS (planned)
───────────────────
- The Row (hub)
- Corner store (robbable)
- Laundromat front
- Back office
- Warehouse storage
- Owner's fortified shop (boss arena)
"""

META = {
    "number": 5,
    "title": "The Row",
    "age": 21,
    "era": "Early twenties",
    "rank": "Grifter",
    "respect_range": (100, 200),
    "boss": "TBD — Corrupt store owner",
    "boss_id": "store_owner",
    "weapon_progression": ["knife", "cheap pistol"],
    "unlock_actions": ["rob corner stores"],
    "player_max_hp": 90,
    "setting": (
        "A row of storefronts hiding dirty money. Laundromats, bodegas, "
        "corner stores — all of them washing more than clothes. This is "
        "where crime starts wearing a collar."
    ),
}

ITEMS = {}
ENEMIES = {}
LOCATIONS = {}
AMBIENT = []
