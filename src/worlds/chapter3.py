"""Chapter 3 — The Yard: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  Industrial rail yard / warehouse district on the edge of town.
          Abandoned boxcars, chain-link fences, loading docks.
Age:      16–17 (high school junior/senior).
Boss:     Skinhead gang leader — controls the yard and its turf.
Weapons:  Chain, pipe (melee range upgrade).
Actions:  Petty theft (steal from boxcars, warehouses).
Music:    Industrial / heavy — metal clanking, trains in the distance.

BOSS FIGHT
──────────
- Skinhead has lieutenants — possibly a 2-on-1 or pre-fight gauntlet.
- Weakness: needs a specific weapon (chain or pipe) to stand a chance.
- Reward: control of the yard, opens up warehouse district.

LOCATIONS (planned)
───────────────────
- Rail yard (hub)
- Boxcar row
- Loading dock
- Warehouse
- Chain-link fence perimeter
- Skinhead hangout (boss arena)
"""

META = {
    "number": 3,
    "title": "The Yard",
    "age": 16,
    "era": "High school upperclassman",
    "rank": "Punk",
    "respect_range": (25, 50),
    "boss": "TBD — Skinhead leader",
    "boss_id": "skinhead_boss",
    "weapon_progression": ["chain", "pipe"],
    "unlock_actions": ["petty theft"],
    "player_max_hp": 55,
    "setting": (
        "An industrial rail yard on the wrong side of the tracks. "
        "Rusted boxcars, chain-link fences, and the kind of silence "
        "that means someone's watching."
    ),
}

ITEMS = {}
ENEMIES = {}
LOCATIONS = {}
AMBIENT = []
