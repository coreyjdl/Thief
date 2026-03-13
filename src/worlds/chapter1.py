"""Chapter 1 — The Block: items, enemies, locations, ambient flavour."""

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
        "connections": ["home", "park", "corner_store", "alley"],
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
        "connections": ["your_block", "schoolyard"],
        "scene": "park",
        "interior": False,
        "loot_table": ["soda_can"],
        "encounter_chance": 0.35,
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
        "encounter_chance": 0.40,
        "enemies": ["big_tommy", "skinny_derek"],
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
]
