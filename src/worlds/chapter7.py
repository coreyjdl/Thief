"""Chapter 7 — The Heights: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  Uptown / financial district — penthouses, private clubs, high-rises.
          The player has climbed from the gutter to the glass towers.
Age:      30–35 (thirties, at the peak of criminal career).
Boss:     City crime boss or rival syndicate leader — controls the Heights.
Weapons:  Explosives, rifles (military-grade hardware).
Actions:  High-end heists (bank vaults, art galleries, armoured cars).
Music:    Electronic / synth-noir — neon, glass, money.

BOSS FIGHT
──────────
- Crime boss operates from a penthouse / private club.
- Must execute a heist to draw them out or infiltrate their operation.
- Multiple approaches: stealth, force, or leverage.
- Reward: control of the criminal underworld, sets up the final chapter.

LOCATIONS (planned)
───────────────────
- The Heights (hub)
- Private club
- Penthouse tower
- Bank / vault
- Art gallery
- Rooftop (boss arena)
"""

META = {
    "number": 7,
    "title": "The Heights",
    "age": 32,
    "era": "Thirties",
    "rank": "Syndicate",
    "respect_range": (400, 800),
    "boss": "TBD — City crime boss / rival syndicate leader",
    "boss_id": "crime_boss",
    "weapon_progression": ["explosives", "rifles"],
    "unlock_actions": ["high-end heists"],
    "player_max_hp": 160,
    "setting": (
        "Glass towers and private clubs where the real money moves. "
        "You started on the block — now you're looking down at it from "
        "forty floors up. The view comes with a price."
    ),
}

ITEMS = {}
ENEMIES = {}
LOCATIONS = {}
AMBIENT = []
