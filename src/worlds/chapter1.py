"""Chapter 1 — The Block: items, enemies, locations, ambient flavour."""

META = {
    "number": 1,
    "title": "The Block",
    "age": 14,
    "era": "Middle school",
    "rank": "Push-over Kid",
    "respect_range": (0, 10),
    "boss": "Marcus 'Kicks' Delano",
    "boss_id": "marcus",
    "weapon_progression": ["fists", "loose brick"],
    "unlock_actions": ["run away", "basic punch"],
    "player_max_hp": 30,
    "setting": (
        "A worn-down neighbourhood block. You're fourteen, small for your "
        "age, and at the bottom of every food chain that matters."
    ),
}

ITEMS = {
    "soda_can": {
        "name": "Soda Can",
        "desc": "A lukewarm can of cola. Restores a little health.",
        "heal": 5,
    },
    "candy_bar": {
        "name": "Candy Bar",
        "desc": "Slightly sticky. Tastes like victory.",
        "heal": 8,
    },
    "moms_money": {
        "name": "Mom's $20",
        "desc": "A crumpled twenty from Mom's purse. You feel guilty.",
        "type": "quest",
    },
    "loose_brick": {
        "name": "Loose Brick",
        "desc": "A chunk of brick from a crumbling wall. Better than bare knuckles.",
        "type": "weapon",
        "damage_bonus": 2,
    },
}

ENEMIES = {
    "skinny_derek": {
        "name": "Skinny Derek",
        "max_hp": 15, "hp": 15,
        "damage_min": 2, "damage_max": 4,
        "respect_reward": 5,
        "desc": "A wiry kid with a mean look and bony fists.",
        "attacks": [
            "takes a wild swing",
            "scratches at you",
            "throws a sloppy jab",
            "kicks at your shin",
        ],
        "defeat_text": "Derek scrambles away, holding his face.",
        "taunt": "You're dead meat, kid!",
    },
    "big_tommy": {
        "name": "Big Tommy",
        "max_hp": 22, "hp": 22,
        "damage_min": 3, "damage_max": 6,
        "respect_reward": 7,
        "desc": "A hefty kid built like a refrigerator. Slow but strong.",
        "attacks": [
            "throws a heavy haymaker",
            "shoves you hard",
            "lands a meaty punch",
            "body-checks you",
        ],
        "defeat_text": "Tommy sits down hard, wheezing. He's done.",
        "taunt": "I'm gonna flatten you!",
    },
    "jake_the_snake": {
        "name": "Jake the Snake",
        "max_hp": 12, "hp": 12,
        "damage_min": 1, "damage_max": 3,
        "respect_reward": 4,
        "desc": "A quick, sneaky kid. Strikes fast and runs faster.",
        "attacks": [
            "darts in with a quick jab",
            "sucker-punches you",
            "snaps a kick at your knee",
            "goes for a cheap shot",
        ],
        "defeat_text": "Jake bolts into the distance. Smart move.",
        "taunt": "You won't even see it coming!",
    },
    "marcus": {
        "name": "Marcus 'Kicks' Delano",
        "max_hp": 40, "hp": 40,
        "damage_min": 5, "damage_max": 8,
        "respect_reward": 15,
        "desc": (
            "The block's biggest bully. Sixteen, built like he's been "
            "held back three times — because he has. Crew-cut, oversized "
            "letterman jacket he definitely didn't earn, and a pair of "
            "pristine white Jordans he treats like they're made of glass. "
            "Every kid on the block pays tribute or pays the price."
        ),
        "attacks": [
            "throws a crushing right hook",
            "slams his fist into your gut",
            "headbutts you",
            "grabs you and throws you down",
            "stomps toward you with those clean Jordans",
        ],
        "defeat_text": (
            "Marcus stumbles back, disbelief on his face. "
            "His precious Jordans are scuffed and dirty. "
            "For the first time the block's king looks shook."
        ),
        "taunt": "You know who runs this block.",
    },
}

LOCATIONS = {
    "home": {
        "name": "Home",
        "desc": (
            "Your house. Small, cramped, but safe. The TV hums in the "
            "corner. Mom's purse sits on the kitchen table."
        ),
        "connections": ["your_block"],
        "scene": "home",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
    },
    "your_block": {
        "name": "Your Block",
        "desc": (
            "A row of tired brick houses lines the cracked sidewalk. "
            "An old Buick on cinder blocks thumps bass across the street. "
            "The neighborhood's seen better decades."
        ),
        "connections": ["home", "park", "corner_store", "alley", "construction_site"],
        "scene": "your_block",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0.15,
        "enemies": ["skinny_derek", "jake_the_snake"],
    },
    "park": {
        "name": "The Park",
        "desc": (
            "A patch of brown grass the city calls a park. A busted swing "
            "set creaks in the wind. A wooden bench offers a seat — if you "
            "don't mind splinters. The kind of place trouble finds you."
        ),
        "connections": ["your_block", "schoolyard", "woods"],
        "scene": "park",
        "interior": False,
        "loot_table": ["soda_can"],
        "encounter_chance": 0.25,
        "enemies": ["skinny_derek", "big_tommy", "jake_the_snake"],
    },
    "schoolyard": {
        "name": "The Schoolyard",
        "desc": (
            "Chain-link fence surrounds cracked concrete and a lopsided "
            "basketball hoop. School's out but the real lessons happen "
            "here. This is Marcus's turf."
        ),
        "connections": ["park"],
        "scene": "schoolyard",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
    },
    "corner_store": {
        "name": "The Corner Store",
        "desc": (
            "Kim's Corner Market. The awning's faded and the neon flickers. "
            "You can see snacks through the barred windows but you can't go "
            "inside — Kim banned half the neighbourhood kids last month. "
            "Sometimes you find a dropped candy bar out front."
        ),
        "connections": ["your_block"],
        "scene": "corner_store",
        "interior": False,
        "loot_table": ["candy_bar", "soda_can"],
        "encounter_chance": 0.10,
        "enemies": ["jake_the_snake"],
    },
    "alley": {
        "name": "The Alley",
        "desc": (
            "A narrow passage between two brick buildings. A rusted "
            "dumpster squats against one wall. Puddles reflect what little "
            "light makes it in. Not a place to hang around."
        ),
        "connections": ["your_block"],
        "scene": "alley",
        "interior": False,
        "loot_table": ["soda_can", "loose_brick"],
        "encounter_chance": 0.30,
        "enemies": ["big_tommy", "skinny_derek"],
        "hazards": [
            {"text": "A rat darts out and bites your ankle.", "damage": 1, "chance": 0.15},
            {"text": "You scrape your arm on a rusty nail sticking out of the wall.", "damage": 2, "chance": 0.10},
        ],
    },
    "woods": {
        "name": "The Woods",
        "desc": (
            "A scraggly patch of trees behind the houses. Broken bottles "
            "and old mattresses litter the ground. Kids come here to hide "
            "or to fight where nobody's watching."
        ),
        "connections": ["park", "abandoned_lot"],
        "scene": "woods",
        "interior": False,
        "loot_table": ["soda_can"],
        "encounter_chance": 0.20,
        "enemies": ["big_tommy", "jake_the_snake"],
        "hazards": [
            {"text": "You trip over a root and bang your knee hard.", "damage": 2, "chance": 0.15},
            {"text": "A branch snaps back and whips you across the face.", "damage": 1, "chance": 0.20},
            {"text": "Something stings your arm — a wasp nest in the tree.", "damage": 2, "chance": 0.10},
        ],
    },
    "abandoned_lot": {
        "name": "The Abandoned Lot",
        "desc": (
            "A weed-choked lot where a house used to be. Nothing left but "
            "a crumbling foundation, broken glass, and a rusted chain-link "
            "fence with a gap big enough to squeeze through."
        ),
        "connections": ["woods", "construction_site"],
        "scene": "abandoned_lot",
        "interior": False,
        "loot_table": ["soda_can", "candy_bar"],
        "encounter_chance": 0.20,
        "enemies": ["skinny_derek", "big_tommy", "jake_the_snake"],
        "hazards": [
            {"text": "You step on broken glass. It cuts right through your shoe.", "damage": 2, "chance": 0.15},
            {"text": "A piece of rebar snags your leg as you climb through the fence.", "damage": 1, "chance": 0.12},
            {"text": "A stray dog lunges and nips your hand before running off.", "damage": 2, "chance": 0.10},
        ],
    },
    "construction_site": {
        "name": "The Construction Site",
        "desc": (
            "A half-built something surrounded by orange fencing that's "
            "mostly fallen over. Concrete pillars, exposed rebar, and a "
            "rusty crane that hasn't moved in months. Dangerous, but the "
            "older kids hang out on the second floor."
        ),
        "connections": ["abandoned_lot", "your_block"],
        "scene": "construction_site",
        "interior": False,
        "loot_table": ["loose_brick"],
        "encounter_chance": 0.25,
        "enemies": ["big_tommy", "skinny_derek", "jake_the_snake"],
        "hazards": [
            {"text": "A loose board gives way under your foot. You drop a few feet.", "damage": 3, "chance": 0.12},
            {"text": "Dust and debris rain down from above — you catch some in your eyes.", "damage": 1, "chance": 0.15},
            {"text": "You grab a rebar to steady yourself and slice your palm open.", "damage": 2, "chance": 0.10},
        ],
    },
}

AMBIENT = [
    "A stray cat watches you from a windowsill.",
    "Someone's music thumps from a parked car nearby.",
    "An old man sits on his porch, shaking his head at the world.",
    "A group of kids run past, laughing at something.",
    "You hear a siren in the distance. Nothing new.",
    "A plastic bag tumbles down the sidewalk in the wind.",
    "You spot some faded graffiti: 'KICKS RUNS THIS BLOCK.'",
    "A pigeon pecks at a crushed french-fry container.",
    "Someone yells from a window upstairs. A door slams.",
    "Two stray dogs trot down the street like they own it.",
    "A police cruiser rolls past slow, officer eyeing the block.",
    "You hear a shopkeeper yelling at someone to get out.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "mom": {
        "name": "Mom",
        "role": "family",
        "desc": "Your mother. Tired, overworked, but she loves you.",
        "location": "home",
        "dialogue": [
            "Be careful out there. And stay away from that Marcus boy.",
            "There's leftover rice in the fridge.",
            "You better be doing your homework.",
        ],
    },
    "old_earl": {
        "name": "Old Earl",
        "role": "info",
        "desc": (
            "An old man who sits on his porch all day. Sees everything "
            "that happens on the block. Knows who runs what."
        ),
        "location": "your_block",
        "dialogue": [
            "You want to know who runs things? Watch the schoolyard after three.",
            "That Marcus kid's been shaking down everyone. Somebody ought to stand up.",
            "Used to be a good block. Before the gangs.",
        ],
    },
    "kim": {
        "name": "Kim",
        "role": "shopkeeper",
        "desc": (
            "Owner of Kim's Corner Market. Tough, no-nonsense. "
            "Keeps a bat under the counter and she's not afraid to use it."
        ),
        "location": "corner_store",
        "dialogue": [
            "You buying something or just looking?",
            "Don't even think about it. I see everything.",
            "Last kid who tried something got a bat to the shins.",
        ],
        "fights_back": True,
        "fight_back_chance": 0.35,
        "fight_back_damage": (3, 6),
        "fight_back_text": "Kim swings the bat from under the counter!",
    },
}
