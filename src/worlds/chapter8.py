"""Chapter 8 — The Crown: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  The city itself — the final chapter spans all previous territories.
          The mysterious kingpin who's been pulling strings is revealed.
Age:      35+ (late thirties, the endgame).
Boss:     The Ultimate Boss — the kingpin who controls the city, or a
          corrupt official with a private army. The final confrontation.
Weapons:  Special / unique weapons (one-of-a-kind, earned through the story).
Actions:  Final challenge — everything you've built leads to this.
Music:    Epic / orchestral — the stakes are everything.

BOSS FIGHT
──────────
- Multi-phase final boss with callbacks to every chapter.
- The kingpin may have been mentioned or hinted at since Chapter 1.
- Victory means you run the city — or burn it down trying.
- Could branch: take the throne, walk away, or destroy the system.

LOCATIONS (planned)
───────────────────
- City Hall / mansion (hub)
- Underground bunker
- The old block (return to where it started)
- Kingpin's stronghold (final boss arena)
- Rooftop / helipad (climax scene)
"""

META = {
    "number": 8,
    "title": "The Crown",
    "age": 36,
    "era": "Late thirties — the endgame",
    "rank": "Boss Level",
    "respect_range": (800, None),
    "boss": "TBD — The Kingpin / corrupt official",
    "boss_id": "kingpin",
    "weapon_progression": ["special weapons"],
    "unlock_actions": ["final challenge"],
    "player_max_hp": 200,
    "setting": (
        "The whole city. You started as a fourteen-year-old kid getting "
        "shoved around on the block. Now the block, the strip, the yard, "
        "the avenue, the row, the docks, the heights — they're all yours. "
        "Or they will be, after tonight."
    ),
}

ITEMS = {}
ENEMIES = {}
LOCATIONS = {}
AMBIENT = []
