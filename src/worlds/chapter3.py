"""Chapter 3 — The Yard: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  Industrial rail yard / warehouse district on the edge of town.
          Abandoned boxcars, chain-link fences, loading docks.
Age:      16–17 (high school junior/senior).
Boss:     Skinhead gang leader — controls the yard and its turf.
Weapons:  Crowbar (from pawn shop trade).
Actions:  Petty theft (boxcars, warehouses), loot retrieval.

QUEST FLOW
──────────
1. Player arrives at The Yard with the car stereo from Ch2.
2. Pawn Shop: try to sell the stereo — owner says it's busted,
   offers a crowbar in trade. Crowbar becomes primary weapon.
3. Explore the yard — fight skinhead grunts for respect.
4. Skinhead boss caught you lifting small gear earlier. He won't
   fight until you bring him something of value.
5. Warehouse Crate Quest: skinhead demands a specific boxcar crate.
   Player must break into the warehouse/boxcar row to retrieve it.
   Crate contains electronics modules and small arms parts.
6. Return crate → boss fight unlocks.
7. Boss fight: use crowbar and environment (boxes, cover, crate
   doors) to survive minions and the skinhead leader.
8. Victory: access to crate loot — electronics/parts can be sold,
   traded, or modified for Street Thug weapons (bat, ammo, etc.)
   in Chapter 4.

LOCATIONS (planned)
───────────────────
- The Yard (hub)
- Pawn shop
- Boxcar row
- Loading dock
- Warehouse
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
    "weapon_progression": ["crowbar"],
    "unlock_actions": ["petty theft", "loot retrieval"],
    "player_max_hp": 55,
    "setting": (
        "An industrial rail yard on the wrong side of the tracks. "
        "Rusted boxcars, chain-link fences, and the kind of silence "
        "that means someone's watching."
    ),
}

ITEMS = {
    "crowbar": {
        "name": "Crowbar",
        "desc": "Cold steel with a comfortable curve. Pries open doors and skulls.",
        "type": "weapon",
        "damage_bonus": 5,
    },
    "beef_jerky": {
        "name": "Beef Jerky",
        "desc": "A gas-station stick of jerky. Tough but filling.",
        "heal": 7,
        "price": 3,
    },
    "cheap_bandage": {
        "name": "Cheap Bandage",
        "desc": "Some gauze and tape. Better than nothing.",
        "heal": 12,
        "price": 5,
    },
    "crate_loot": {
        "name": "Electronics Crate",
        "desc": (
            "A heavy crate packed with circuit boards, wiring harnesses, "
            "and small components. Valuable to the right people."
        ),
        "type": "quest",
    },
}

ENEMIES = {
    "rail_rat": {
        "name": "Rail Rat",
        "max_hp": 18, "hp": 18,
        "damage_min": 3, "damage_max": 5,
        "respect_reward": 6,
        "money_drop": (1, 4),
        "desc": "A scrappy kid who lives in the boxcars. Quick and vicious.",
        "attacks": [
            "swings a rusty chain at you",
            "jabs you with a sharpened screwdriver",
            "throws a handful of gravel at your face",
            "kicks a loose board into your shins",
        ],
        "defeat_text": "Rail Rat scrambles into a boxcar and slams the door shut.",
        "taunt": "This yard ain't yours!",
    },
    "bolt_cutter_ben": {
        "name": "Bolt-Cutter Ben",
        "max_hp": 24, "hp": 24,
        "damage_min": 4, "damage_max": 7,
        "respect_reward": 8,
        "money_drop": (2, 5),
        "desc": (
            "A stocky teenager with a pair of bolt cutters he uses as "
            "both a tool and a weapon. Missing a front tooth."
        ),
        "attacks": [
            "swings the bolt cutters at your head",
            "jabs the handle into your gut",
            "smashes the heavy jaws into your shoulder",
            "hooks your ankle with the cutters and yanks",
        ],
        "defeat_text": "Ben drops the bolt cutters and limps off between the boxcars.",
        "taunt": "I'll clip you like a chain-link!",
    },
    "grease_monkey": {
        "name": "Grease Monkey",
        "max_hp": 20, "hp": 20,
        "damage_min": 3, "damage_max": 6,
        "respect_reward": 7,
        "money_drop": (1, 6),
        "desc": (
            "A wiry kid covered in engine grease. Works on stolen car "
            "parts in the yard and doesn't like company."
        ),
        "attacks": [
            "chucks a wrench at your head",
            "slams a car battery into your ribs",
            "throws motor oil in your eyes",
            "cracks you with a lug wrench",
        ],
        "defeat_text": "Grease Monkey wipes his hands on his jeans and walks away, done.",
        "taunt": "You picked the wrong junkyard, bro.",
    },
    "skinhead_grunt": {
        "name": "Skinhead Grunt",
        "max_hp": 28, "hp": 28,
        "damage_min": 5, "damage_max": 8,
        "respect_reward": 9,
        "money_drop": (2, 7),
        "desc": (
            "Shaved head, combat boots, knuckle tattoos. One of the "
            "skinhead crew that controls the warehouse district."
        ),
        "attacks": [
            "throws a brutal right cross",
            "headbutts you square in the nose",
            "stomps on your foot with his steel-toed boot",
            "grabs you by the collar and slams you into a boxcar",
        ],
        "defeat_text": "The grunt spits blood and backs off, radioing his crew.",
        "taunt": "You don't belong here. Nobody invited you.",
    },
    "skinhead_boss": {
        "name": "Razor",
        "max_hp": 65, "hp": 65,
        "damage_min": 6, "damage_max": 10,
        "respect_reward": 20,
        "desc": (
            "The skinhead crew's leader. Tall, lean, with a shaved head "
            "and a straight razor he keeps in his boot. He runs the yard "
            "like a kingdom and doesn't share. Cold eyes, colder hands."
        ),
        "attacks": [
            "slashes at you with the straight razor",
            "throws a devastating elbow to your jaw",
            "kicks you in the chest with steel-toed boots",
            "grabs your arm and twists it behind your back",
            "slams you face-first into a boxcar door",
        ],
        "defeat_text": (
            "Razor stumbles back, blood on his lip. He stares at you "
            "with something between fury and grudging respect. "
            "\"This ain't over.\" But it is."
        ),
        "taunt": "Nobody takes what's mine and walks away.",
    },
}

LOCATIONS = {
    "the_yard": {
        "name": "The Yard",
        "desc": (
            "A sprawling rail yard of rusted tracks, gravel beds, and "
            "chain-link fencing topped with barbed wire. The air smells "
            "like diesel and rust. Abandoned boxcars line up like "
            "sleeping giants."
        ),
        "connections": ["the_strip", "pawn_shop", "boxcar_row", "loading_dock"],
        "scene": "the_yard",
        "interior": False,
        "loot_table": ["soda_can", "beef_jerky"],
        "encounter_chance": 0.20,
        "enemies": ["rail_rat", "grease_monkey"],
        "chapter": 3,
        "hazards": [
            {"text": "You trip over a rail spike and cut your palm.", "damage": 2, "chance": 0.12},
            {"text": "A rusted rail car door swings open and catches your shoulder.", "damage": 3, "chance": 0.08},
        ],
    },
    "pawn_shop": {
        "name": "The Pawn Shop",
        "desc": (
            "A grimy storefront crammed with other people's stuff. "
            "Guitars, power tools, jewelry — and under the counter, "
            "things that don't have serial numbers anymore. The owner, "
            "Shifty, peers at you through smudged glasses."
        ),
        "connections": ["the_yard"],
        "scene": "pawn_shop",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 3,
        "shop": {
            "crowbar": 0,  # traded for car stereo, not cash
            "beef_jerky": 3,
            "cheap_bandage": 5,
        },
    },
    "boxcar_row": {
        "name": "Boxcar Row",
        "desc": (
            "A line of old freight cars on a dead-end siding. Some are "
            "rusted shut, some have been pried open. You can hear rats "
            "scurrying inside. The skinhead crew uses a couple of these "
            "as stash points."
        ),
        "connections": ["the_yard", "warehouse"],
        "scene": "boxcar_row",
        "interior": False,
        "loot_table": ["beef_jerky"],
        "encounter_chance": 0.25,
        "enemies": ["rail_rat", "bolt_cutter_ben", "skinhead_grunt"],
        "chapter": 3,
        "hazards": [
            {"text": "A loose boxcar door swings shut on your hand.", "damage": 3, "chance": 0.10},
            {"text": "You step on a rusted nail. It goes right through your shoe.", "damage": 2, "chance": 0.12},
            {"text": "An old coupling mechanism snaps and the metal whips past your face.", "damage": 2, "chance": 0.06},
        ],
    },
    "loading_dock": {
        "name": "The Loading Dock",
        "desc": (
            "A concrete platform backed by roller doors — most of them "
            "jammed. Pallets stacked high with who-knows-what. A forklift "
            "with flat tires sits abandoned. This is neutral ground where "
            "deals happen."
        ),
        "connections": ["the_yard", "skinhead_hangout"],
        "scene": "loading_dock",
        "interior": False,
        "loot_table": ["soda_can"],
        "encounter_chance": 0.15,
        "enemies": ["grease_monkey", "bolt_cutter_ben"],
        "chapter": 3,
        "hazards": [
            {"text": "A pallet tips over. You dodge but a box clips your head.", "damage": 2, "chance": 0.10},
            {"text": "You lean on a roller door and it collapses inward. You fall with it.", "damage": 3, "chance": 0.06},
        ],
    },
    "warehouse": {
        "name": "The Warehouse",
        "desc": (
            "A cavernous metal building full of crates, machinery, and "
            "shadows. High windows let in dusty beams of light. This is "
            "where the electronics crate is kept — the one the skinhead "
            "boss wants."
        ),
        "connections": ["boxcar_row"],
        "scene": "warehouse",
        "interior": True,
        "loot_table": ["cheap_bandage"],
        "encounter_chance": 0.30,
        "enemies": ["skinhead_grunt", "bolt_cutter_ben"],
        "chapter": 3,
        "hazards": [
            {"text": "A heavy chain drops from a pulley above and hits your shoulder.", "damage": 3, "chance": 0.08},
            {"text": "You knock over a barrel of chemical solvent. The fumes burn your throat.", "damage": 2, "chance": 0.10},
        ],
    },
    "skinhead_hangout": {
        "name": "The Hangout",
        "desc": (
            "A gutted office trailer behind the loading dock. Graffiti "
            "covers every wall. A steel drum fire crackles out front. "
            "This is Razor's base of operations."
        ),
        "connections": ["loading_dock"],
        "scene": "skinhead_hangout",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 3,
    },
}

AMBIENT = [
    "A freight train rumbles past on the main line, shaking the ground.",
    "Pigeons explode from a boxcar as something startles them inside.",
    "You hear metal scraping on metal somewhere deep in the yard.",
    "A dog barks from behind a chain-link fence, hackles up.",
    "The wind carries the smell of diesel fuel and old rust.",
    "Someone's spray-painted 'RAZOR' across a boxcar in red.",
    "A rat the size of a cat watches you from under a pallet.",
    "You hear the distant clang of someone working on something metal.",
    "An old security camera hangs from a pole, its cable cut years ago.",
    "Gravel crunches somewhere behind you. When you look, nobody's there.",
    "A police car parks near the yard entrance. The officer watches but doesn't come in.",
    "You hear a shopkeeper at the pawn shop arguing with someone over a price.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "shifty": {
        "name": "Shifty",
        "role": "shopkeeper / quest",
        "desc": (
            "The pawn shop owner. Greasy comb-over, smudged glasses, "
            "and a permanent squint. Trades in anything no-questions-asked."
        ),
        "location": "pawn_shop",
        "dialogue": [
            "That stereo's busted. Tell you what — I'll trade you this crowbar for it.",
            "Everything's got a price. Even you.",
            "You want bandages? Five bucks. Don't bleed on the counter.",
        ],
        "quest_role": "Trades busted car stereo for crowbar (Ch3 weapon).",
        "fights_back": True,
        "fight_back_chance": 0.25,
        "fight_back_damage": (3, 5),
        "fight_back_text": "Shifty pulls a pipe from behind the counter and swings!",
    },
    "diesel_dave": {
        "name": "Diesel Dave",
        "role": "info",
        "desc": (
            "A retired rail worker who still hangs around the yard. "
            "Knows the layout — which boxcars are stash points, which "
            "doors are welded shut, where the crew hides their goods."
        ),
        "location": "the_yard",
        "dialogue": [
            "The electronics crate? Third boxcar from the end, blue door.",
            "Watch out for Razor's boys near the warehouse. They patrol in pairs.",
            "Used to be an honest yard. Now it's all skinheads and stolen goods.",
            "The loading dock's neutral ground. Even Razor respects that — mostly.",
        ],
        "quest_role": "Gives info on crate location and skinhead patrol routes.",
    },
    "mute_jenny": {
        "name": "Mute Jenny",
        "role": "info / quest",
        "desc": (
            "A girl who lives in one of the boxcars. Doesn't talk much — "
            "or at all — but she draws maps. Detailed ones. She slips "
            "you a hand-drawn map of the warehouse interior if you bring "
            "her food."
        ),
        "location": "boxcar_row",
        "dialogue": [
            "(She holds up a finger — wait. She sketches something on cardboard.)",
            "(She slides you a hand-drawn map of the warehouse. Every door marked.)",
            "(She points at a spot on the map and draws a skull. Danger.)",
        ],
        "quest_role": "Trades food for warehouse map (helps navigate warehouse quest).",
    },
}

# ── Police system ──────────────────────────────────────────────────
POLICE = {
    "presence": 0.08,
    "arrest_chance": 0.25,
    "money_loss_pct": 0.50,
    "respect_loss": 5,
    "arrest_text": (
        "A railway security guard spots you and radios the cops. "
        "A patrol car pulls up before you can run."
    ),
    "release_text": (
        "They search you, confiscate your cash, and kick you out of the yard. "
        "Word gets around. Your rep takes a hit."
    ),
}
