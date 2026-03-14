"""Chapter 5 — The Row: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  Urban neighbourhood — corner stores, pawn shops, gang hangouts.
          The legitimate-looking side of crime.
Age:      20–22 (early twenties, experienced street operator).
Boss:     Corrupt store owner with bodyguards.
Weapons:  Knife (carried from Ch4), cheap pistol (acquired via cash/pawn).
Actions:  Rob corner stores, resource management.

NARRATIVE
─────────
You're high in the gang now but still a miscreant and a loner. Corner
store robberies aren't sanctioned — the gang doesn't approve — but
you gotta do it to afford ammo, small weapons, and survival. This is
the chapter where you realise you're in the gang and it matters.

The corrupt store owner tolerates your petty theft in exchange for
protection payments. He's got bodyguards and connections.

QUEST FLOW
──────────
1. Arrive on The Row. Cash and items from the Ch4 lab job are your
   starting resources.
2. Grind: rob corner stores for cash. Unsanctioned, risky — teaches
   resource management, stealth, and planning.
3. Buy cheap pistol from pawn/contact when you can afford it.
4. Earn respect through robberies and shakedowns.
5. Challenge the corrupt store owner → scripted loss (bodyguards).
6. Figure out his operation — case the joint, learn routines.
7. Take him down. Sell/modify stolen goods for next missions.
8. Completion triggers dialogue: "You gotta go professional. No more
   dirty petty crime." → unlocks Crew Member missions.

FORWARD-USE THREAD
──────────────────
Cash + stolen goods → fund pistol + ammo → "go professional" dialogue
→ transitions to Crew Member van heists.

LOCATIONS (planned)
───────────────────
- The Row (hub)
- Corner store (robbable)
- Laundromat front
- Back office
- Pawn shop / arms contact
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
    "weapon_progression": ["cheap pistol"],
    "unlock_actions": ["rob corner stores"],
    "player_max_hp": 90,
    "setting": (
        "The Row — corner stores, pawn shops, gang hangouts. You're "
        "high in the gang but still a loner. Petty crime isn't sanctioned "
        "but you gotta eat."
    ),
}

ITEMS = {
    "cheap_pistol": {
        "name": "Cheap Pistol",
        "desc": "A beat-up .22 that jams every third shot. Better than nothing.",
        "type": "weapon",
        "damage_bonus": 10,
    },
    "ammo_box": {
        "name": "Ammo Box",
        "desc": "A small box of .22 rounds. Won't last forever.",
        "type": "quest",
    },
    "pain_pills": {
        "name": "Pain Pills",
        "desc": "Over-the-counter painkillers. Dull the ache.",
        "heal": 15,
        "price": 6,
    },
    "protein_bar": {
        "name": "Protein Bar",
        "desc": "Tastes like cardboard mixed with ambition.",
        "heal": 8,
        "price": 3,
    },
    "register_cash": {
        "name": "Register Cash",
        "desc": "A wad of bills from a store register. Smells like guilt.",
        "type": "quest",
    },
}

ENEMIES = {
    "corner_store_clerk": {
        "name": "Corner Store Clerk",
        "max_hp": 20, "hp": 20,
        "damage_min": 3, "damage_max": 6,
        "respect_reward": 5,
        "money_drop": (5, 15),
        "desc": (
            "A tired-looking clerk who's been robbed before and isn't "
            "going to take it lying down this time. Reaches under the counter."
        ),
        "attacks": [
            "swings a can of soup at your head",
            "throws a glass jar that shatters on you",
            "hits you with a broom handle",
            "sprays you with pepper spray",
        ],
        "defeat_text": "The clerk puts his hands up and backs against the wall. Register's open.",
        "taunt": "Not again! I'll fight you for it!",
    },
    "armed_shopkeeper": {
        "name": "Armed Shopkeeper",
        "max_hp": 30, "hp": 30,
        "damage_min": 8, "damage_max": 15,
        "respect_reward": 8,
        "money_drop": (10, 25),
        "desc": (
            "This store owner has a gun under the counter and he's not "
            "afraid to use it. Eyes like a hawk. Trigger finger twitching."
        ),
        "attacks": [
            "fires a shot that grazes your arm",
            "pistol-whips you across the face",
            "fires and the bullet tears through your sleeve",
            "swings the gun butt into your ribs",
        ],
        "defeat_text": "The shopkeeper drops the gun and slides against the wall. Register's yours.",
        "taunt": "You picked the WRONG store!",
        "death_chance": 0.08,
        "death_text": (
            "The shopkeeper fires. The bullet catches you center mass. "
            "Your legs buckle. The last thing you see is the fluorescent light."
        ),
    },
    "street_hustler": {
        "name": "Street Hustler",
        "max_hp": 22, "hp": 22,
        "damage_min": 4, "damage_max": 7,
        "respect_reward": 6,
        "money_drop": (3, 10),
        "desc": "A fast-talking con man who doesn't con easy. Quick with a razor.",
        "attacks": [
            "slashes at you with a box cutter",
            "throws a quick combination",
            "kicks you in the knee",
            "throws sand in your eyes and sucker-punches you",
        ],
        "defeat_text": "The hustler picks up his hat and vanishes into the crowd.",
        "taunt": "You got no idea who you're dealing with.",
    },
    "bodyguard": {
        "name": "Bodyguard",
        "max_hp": 40, "hp": 40,
        "damage_min": 6, "damage_max": 10,
        "respect_reward": 10,
        "money_drop": (5, 12),
        "desc": (
            "A mountainous guy in a black t-shirt two sizes too small. "
            "He works for the store owner and takes the job seriously."
        ),
        "attacks": [
            "throws a devastating haymaker",
            "grabs you and throws you through a shelf",
            "headbutts you with raw force",
            "picks you up by the throat",
        ],
        "defeat_text": "The bodyguard crumples like a folding chair. He's out.",
        "taunt": "Boss said nobody gets through. That means you.",
    },
    "store_owner": {
        "name": "Mr. Fontaine",
        "max_hp": 95, "hp": 95,
        "damage_min": 8, "damage_max": 14,
        "respect_reward": 30,
        "desc": (
            "The corrupt store owner who runs The Row. Mid-forties, heavy-set, "
            "with slicked-back hair and a gold pinky ring. He's got two "
            "bodyguards, connections to real criminals, and a snub-nose .38 "
            "in his desk drawer. He plays nice until you threaten his money."
        ),
        "attacks": [
            "fires the .38 — the bullet tears past you",
            "throws a right hook with the gold ring leading",
            "grabs a desk lamp and smashes it across your face",
            "kicks you backward into the shelves",
            "pistol-whips you hard across the jaw",
        ],
        "defeat_text": (
            "Fontaine slumps back in his chair, blood on his expensive "
            "shirt. \"Alright, kid. You win this one.\" He slides a roll "
            "of bills across the desk. \"But you gotta go professional. "
            "No more dirty petty crime.\""
        ),
        "taunt": "You think you can rob ME? I OWN this street.",
    },
}

LOCATIONS = {
    "the_row": {
        "name": "The Row",
        "desc": (
            "A busy street lined with corner stores, a laundromat, and "
            "a pawn shop. People come and go but nobody's looking too "
            "closely. The Row is where small-time crime happens in plain "
            "sight."
        ),
        "connections": ["the_avenue", "row_corner_store", "laundromat", "row_pawn_shop", "back_office"],
        "scene": "the_row",
        "interior": False,
        "loot_table": ["soda_can", "protein_bar"],
        "encounter_chance": 0.18,
        "enemies": ["street_hustler"],
        "chapter": 5,
        "hazards": [
            {"text": "A car backfires and you flinch into a fire hydrant.", "damage": 1, "chance": 0.08},
            {"text": "Someone's pit bull lunges at you on a thin leash. The teeth graze your leg.", "damage": 2, "chance": 0.06},
        ],
    },
    "row_corner_store": {
        "name": "Corner Store",
        "desc": (
            "A small store with barred windows and a buzzer door. "
            "The clerk watches you the second you walk in. A camera "
            "blinks red in the corner. The register is right there."
        ),
        "connections": ["the_row"],
        "scene": "row_corner_store",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0.35,
        "enemies": ["corner_store_clerk", "armed_shopkeeper"],
        "chapter": 5,
        "shop": {
            "protein_bar": 3,
            "pain_pills": 6,
        },
    },
    "laundromat": {
        "name": "The Laundromat",
        "desc": (
            "A humid box of spinning machines and the smell of cheap "
            "detergent. The owner uses it as a front. Money goes in "
            "dirty and comes out clean — one quarter at a time."
        ),
        "connections": ["the_row"],
        "scene": "laundromat",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0.10,
        "enemies": ["street_hustler"],
        "chapter": 5,
        "hazards": [
            {"text": "You slip on a puddle of detergent and crack your elbow on a machine.", "damage": 2, "chance": 0.10},
        ],
    },
    "row_pawn_shop": {
        "name": "Pawn Shop / Arms Contact",
        "desc": (
            "A hole-in-the-wall pawn shop. Guitars, TVs, and a locked "
            "case of 'sporting goods' that are definitely not for sport. "
            "The owner, Mack, knows what you're here for."
        ),
        "connections": ["the_row"],
        "scene": "row_pawn_shop",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 5,
        "shop": {
            "cheap_pistol": 50,
            "ammo_box": 15,
            "pain_pills": 6,
        },
    },
    "back_office": {
        "name": "The Back Office",
        "desc": (
            "A windowless room behind Fontaine's store. Metal desk, "
            "filing cabinets, and a safe the size of a dishwasher. "
            "This is where the money goes."
        ),
        "connections": ["the_row", "fontaine_store"],
        "scene": "back_office",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0.20,
        "enemies": ["bodyguard"],
        "chapter": 5,
    },
    "fontaine_store": {
        "name": "Fontaine's Fortified Shop",
        "desc": (
            "Mr. Fontaine's store — the biggest on The Row. Reinforced "
            "door, camera system, and two bodyguards flanking the entrance. "
            "The boss arena."
        ),
        "connections": ["back_office"],
        "scene": "fontaine_store",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 5,
    },
}

AMBIENT = [
    "A neon 'OPEN' sign flickers in a store window.",
    "Someone counts cash in a paper bag on a bench.",
    "You smell fresh-baked rolls from a bakery that's seen better days.",
    "A kid on a scooter zips past, almost clipping your knee.",
    "Two guys lean against a wall, watching everyone who passes.",
    "A storefront shutter goes up — somebody's opening for the day.",
    "You hear a cash register ding from inside a corner store.",
    "Someone's dog is tied up outside a store, barking at nothing.",
    "A delivery truck double-parks and the driver argues with a cop.",
    "You see a store owner sweeping broken glass off the sidewalk.",
    "Sirens in the distance. Getting closer. Then they fade.",
    "A homeless guy mutters directions to nobody in particular.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "mack": {
        "name": "Mack",
        "role": "shopkeeper / arms dealer",
        "desc": (
            "The pawn shop owner and underground arms contact. Weathered "
            "face, reading glasses on a chain. Sells you the cheap pistol "
            "when you've got the cash."
        ),
        "location": "row_pawn_shop",
        "dialogue": [
            "Fifty bucks for the .22. It jams sometimes but it works.",
            "Ammo's fifteen a box. Don't waste it.",
            "You didn't buy this here. We never met.",
        ],
        "quest_role": "Sells cheap pistol and ammo (Ch5 weapons).",
        "fights_back": True,
        "fight_back_chance": 0.30,
        "fight_back_damage": (6, 12),
        "fight_back_text": "Mack pulls a revolver from under the counter and fires!",
        "fight_back_death_chance": 0.08,
        "fight_back_death_text": (
            "Mack's aim is better than you expected. The revolver barks "
            "once and you're done."
        ),
    },
    "rita": {
        "name": "Rita",
        "role": "info",
        "desc": (
            "Works at the laundromat. Knows everyone's business because "
            "everyone's clothes tell stories. Bloodstains, cash in pockets, "
            "receipts left behind."
        ),
        "location": "laundromat",
        "dialogue": [
            "Fontaine? He keeps the money in the back office safe.",
            "His bodyguards change shift at nine. The tall one's lazy.",
            "Don't rob the corner store on Fifth. The owner's got a gun.",
            "The police cruise past here every twenty minutes. Time it.",
        ],
        "quest_role": "Gives intel on Fontaine's schedule and store owner dangers.",
    },
    "old_sarge": {
        "name": "Old Sarge",
        "role": "info / warning",
        "desc": (
            "A retired army sergeant who hangs out on The Row. He sees "
            "everything and occasionally warns you about what's coming."
        ),
        "location": "the_row",
        "dialogue": [
            "That store on the corner? The new guy's got a piece. Watch yourself.",
            "Fontaine's got connections you don't want to know about.",
            "I seen three guys try what you're trying. Two of 'em are in the ground.",
            "Go professional, kid. This petty stuff'll get you killed.",
        ],
        "quest_role": "Foreshadows dangers and the 'go professional' transition.",
    },
}

# ── Police system ──────────────────────────────────────────────────
POLICE = {
    "presence": 0.18,
    "arrest_chance": 0.40,
    "money_loss_pct": 0.60,
    "respect_loss": 10,
    "arrest_text": (
        "Blue lights everywhere. They've been watching the corner stores. "
        "You're face-down on the pavement before you can drop the cash."
    ),
    "release_text": (
        "They book you, take everything you've got, and cut you loose "
        "twelve hours later. Your money's gone and your name's on a list."
    ),
}
