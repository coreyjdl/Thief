"""Chapter 4 — The Avenue: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  Downtown avenue — pool halls, dive bars, back-alley gambling.
          Grittier, more dangerous. The player is out of school now.
Age:      18–19 (just out of high school, no safety net).
Boss:     Rival gang lieutenant — runs a crew on the avenue.
Weapons:  Bat, crowbar (heavy melee).
Actions:  Shake down NPCs (extort shop owners, collect debts).
Music:    Hip-hop / funk — street-level hustle.

BOSS FIGHT
──────────
- Lieutenant has a small crew — may need to thin ranks first.
- Shakedown mechanic: collect "protection" money as mission requirement.
- Reward: avenue turf, reputation opens up grifter-level jobs.

LOCATIONS (planned)
───────────────────
- The Avenue (hub)
- Pool hall
- Dive bar
- Back-alley dice game
- Pawn shop (trade stolen goods from earlier chapters)
- Lieutenant's corner (boss arena)
"""

META = {
    "number": 4,
    "title": "The Avenue",
    "age": 18,
    "era": "Just out of high school",
    "rank": "Street Thug",
    "respect_range": (50, 100),
    "boss": "TBD — Rival gang lieutenant",
    "boss_id": "gang_lieutenant",
    "weapon_progression": ["bat", "crowbar"],
    "unlock_actions": ["shake down NPCs"],
    "player_max_hp": 70,
    "setting": (
        "Downtown's rougher stretch. Pool halls, dive bars, and the "
        "kind of people who don't ask questions. You're not a kid anymore."
    ),
}

ITEMS = {}
ENEMIES = {}
LOCATIONS = {}
AMBIENT = []
