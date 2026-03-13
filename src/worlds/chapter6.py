"""Chapter 6 — The Docks: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  Waterfront district — shipping containers, fishing boats,
          crab shacks hiding serious operations. Organised crime territory.
Age:      25–28 (mid-to-late twenties, seasoned criminal).
Boss:     Local mob capo — controls the docks and import/export rackets.
Weapons:  Shotgun, SMG (serious firepower).
Actions:  Gang missions, steal vans (cargo heists, smuggling runs).
Music:    Dark jazz / noir — fog horns, creaking docks.

BOSS FIGHT
──────────
- Capo is insulated — must dismantle operations before reaching him.
- Multi-stage: take out supply chains, then confront at his yacht/warehouse.
- Reward: docks territory, access to import pipeline for high-end gear.

LOCATIONS (planned)
───────────────────
- The Docks (hub)
- Container yard
- Fish market (front)
- Capo's warehouse
- Pier / boat slip
- Smuggler's cove
"""

META = {
    "number": 6,
    "title": "The Docks",
    "age": 26,
    "era": "Late twenties",
    "rank": "Crew Member",
    "respect_range": (200, 400),
    "boss": "TBD — Local mob capo",
    "boss_id": "mob_capo",
    "weapon_progression": ["shotgun", "SMG"],
    "unlock_actions": ["gang missions", "steal vans"],
    "player_max_hp": 120,
    "setting": (
        "The waterfront. Shipping containers stacked like walls, fog "
        "rolling off the water, and the smell of fish hiding something "
        "much worse. This is organised crime's front door."
    ),
}

ITEMS = {}
ENEMIES = {}
LOCATIONS = {}
AMBIENT = []
