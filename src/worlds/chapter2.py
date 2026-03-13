"""Chapter 2 — The Strip: items, enemies, locations, ambient flavour."""

META = {
    "number": 2,
    "title": "The Strip",
    "age": 15,
    "era": "High school freshman",
    "rank": "Fighter",
    "respect_range": (10, 25),
    "boss": "Vinnie 'Chrome' Lucca",
    "boss_id": "vinnie",
    "weapon_progression": ["brass knuckles"],
    "unlock_actions": ["take down bullies"],
    "player_max_hp": 40,
    "setting": (
        "A run-down strip of shops and parking lots past the block. "
        "Tougher greasers and older kids run things here."
    ),
}

ITEMS = {
    "brass_knuckles": {
        "name": "Brass Knuckles",
        "desc": "Heavy and cold. Makes your punches hit harder.",
        "type": "weapon",
        "damage_bonus": 3,
    },
    "energy_drink": {
        "name": "Energy Drink",
        "desc": "Tastes like battery acid and regret. Restores health.",
        "heal": 10,
        "price": 3,
    },
    "chips": {
        "name": "Bag of Chips",
        "desc": "Half air, half chip, all delicious.",
        "heal": 4,
        "price": 2,
    },
    "car_stereo": {
        "name": "Car Stereo",
        "desc": "A JVC head unit ripped from a dashboard. Wires dangle from the back.",
        "type": "quest",
    },
}

ENEMIES = {
    "rico_blades": {
        "name": "Rico Blades",
        "max_hp": 20, "hp": 20,
        "damage_min": 3, "damage_max": 5,
        "respect_reward": 6,
        "money_drop": (1, 5),
        "desc": "A wiry kid with a switchblade comb and a chip on his shoulder.",
        "attacks": [
            "takes a quick jab",
            "kicks at your knee",
            "throws a looping hook",
            "shoves you backward",
        ],
        "defeat_text": "Rico backs off, hands up. He's had enough.",
        "taunt": "You don't belong around here, kid.",
    },
    "darnell": {
        "name": "Darnell",
        "max_hp": 28, "hp": 28,
        "damage_min": 4, "damage_max": 7,
        "respect_reward": 8,
        "money_drop": (2, 6),
        "desc": "A stocky kid with a flat-top and fists like cinder blocks.",
        "attacks": [
            "throws a heavy overhand right",
            "catches you with an uppercut",
            "body-slams you into a wall",
            "headbutts you square in the nose",
        ],
        "defeat_text": "Darnell spits blood and limps off around the corner.",
        "taunt": "Let me show you what pain feels like.",
    },
    "cutter_pete": {
        "name": "Cutter Pete",
        "max_hp": 18, "hp": 18,
        "damage_min": 2, "damage_max": 6,
        "respect_reward": 7,
        "money_drop": (0, 3),
        "desc": "Greasy hair, darting eyes, a kid who fights dirty.",
        "attacks": [
            "goes for your eyes",
            "kicks dirt in your face",
            "rakes his nails across your arm",
            "sucker-punches you in the gut",
        ],
        "defeat_text": "Pete scrambles away on all fours. Pathetic.",
        "taunt": "I'll cut you up real nice!",
    },
    "tony_v": {
        "name": "Tony V",
        "max_hp": 35, "hp": 35,
        "damage_min": 5, "damage_max": 9,
        "respect_reward": 10,
        "money_drop": (3, 8),
        "desc": (
            "Bigger, older, meaner. Tony's got arms like truck axles "
            "and a look that says he's done this before. A lot."
        ),
        "attacks": [
            "throws a devastating cross",
            "grabs you by the collar and punches you",
            "slams you against the wall",
            "cracks you with a brutal headbutt",
        ],
        "defeat_text": (
            "Tony hits a knee, breathing hard. "
            "He nods slowly — you earned that one."
        ),
        "taunt": "You got guts coming at me. Stupid guts.",
    },
    "vinnie": {
        "name": "Vinnie 'Chrome' Lucca",
        "max_hp": 55, "hp": 55,
        "damage_min": 6, "damage_max": 10,
        "respect_reward": 20,
        "desc": (
            "He's nineteen, maybe twenty — way too old to be hanging "
            "around high schoolers, but nobody tells him that. Slicked-back "
            "hair, leather jacket with the collar popped, and a cigarette "
            "behind one ear. He leans against a cherry-red '72 Chevelle "
            "that he polishes every single day like it's his firstborn. "
            "The Strip's unofficial king."
        ),
        "attacks": [
            "throws a brutal right cross",
            "slams a fist into your ribs",
            "grabs you and throws you into a parked car",
            "catches you with an elbow to the jaw",
            "kicks you in the chest with a steel-toed boot",
        ],
        "defeat_text": (
            "Vinnie stumbles back, wiping blood from his lip. "
            "He stares at you like he can't quite believe what just happened. "
            "His precious Chevelle has a fresh scratch down the side."
        ),
        "taunt": "Touch my car and I'll end you.",
    },
}

LOCATIONS = {
    "the_strip": {
        "name": "The Strip",
        "desc": (
            "A stretch of cracked pavement lined with shops that have "
            "seen better days. Neon buzzes, bass thumps from somewhere. "
            "This is where the older kids run things."
        ),
        "connections": ["your_block", "head_shop", "bodega", "parking_lot", "boom_car"],
        "scene": "the_strip",
        "interior": False,
        "loot_table": ["soda_can"],
        "encounter_chance": 0.25,
        "enemies": ["rico_blades", "cutter_pete"],
        "chapter": 2,
        "hazards": [
            {"text": "A neon sign sparks and a hot piece of glass lands on your arm.", "damage": 1, "chance": 0.08},
            {"text": "A skateboarder flies past and clips your ankle.", "damage": 1, "chance": 0.10},
        ],
    },
    "head_shop": {
        "name": "The Head Shop",
        "desc": (
            "Dragon Claw Emporium. The window's full of fake swords, "
            "throwing stars, and incense. A bored guy with a ponytail "
            "sits behind the counter. He sells real stuff under it."
        ),
        "connections": ["the_strip"],
        "scene": "head_shop",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 2,
        "shop": {
            "brass_knuckles": 20,
        },
    },
    "bodega": {
        "name": "The Bodega",
        "desc": (
            "A narrow convenience store wedged between a laundromat and "
            "a boarded-up barber shop. The buzzing cooler has drinks. "
            "The counter has snacks. The owner has a bat under the register."
        ),
        "connections": ["the_strip"],
        "scene": "bodega",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 2,
        "hazards": [
            {"text": "The owner catches you trying to steal a soda and swings his bat at you!", "damage": 5, "chance": 0.40},
            {"text": "Bodega cat scratches you from under the counter.", "damage": 1, "chance": 0.15},
        ],
        "shop": {
            "soda_can": 2,
            "candy_bar": 3,
            "energy_drink": 5,
            "chips": 2,
        },
    },
    "parking_lot": {
        "name": "The Parking Lot",
        "desc": (
            "A crumbling lot behind the strip. Shopping carts, broken "
            "glass, and a few cars that look like they might run. "
            "This is where Vinnie 'Chrome' Lucca holds court next to "
            "his cherry-red Chevelle."
        ),
        "connections": ["the_strip"],
        "scene": "parking_lot",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0.30,
        "enemies": ["darnell", "tony_v"],
        "chapter": 2,
        "hazards": [
            {"text": "You slip on an oil slick and slam into a bumper.", "damage": 2, "chance": 0.10},
            {"text": "A car alarm goes off. Somebody chucks a bottle from a window and it clips your shoulder.", "damage": 2, "chance": 0.08},
        ],
    },
    "boom_car": {
        "name": "The Boom Car",
        "desc": (
            "An old Buick on cinder blocks with the biggest speakers "
            "you've ever seen crammed in the back seat. The bass rattles "
            "windows three houses down. Nobody's watching it right now."
        ),
        "connections": ["the_strip"],
        "scene": "boom_car",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 2,
    },
}

AMBIENT = [
    "A car rolls by slow, bass shaking the windows.",
    "Someone's smoking on a stoop, watching you pass.",
    "A neon sign flickers and buzzes overhead.",
    "You catch the smell of frying food from somewhere.",
    "A group of older kids eye you from across the street.",
    "Broken glass crunches under your shoes.",
    "A payphone rings. Nobody answers.",
    "You hear an argument echoing from an open window.",
    "A lowrider idles at the curb, chrome catching the light.",
    "Someone's tagged 'CHROME' across a dumpster in silver paint.",
    "A police cruiser creeps down the strip. Everyone scatters.",
    "You hear a store owner shouting 'Get out!' at someone inside.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "ponytail_guy": {
        "name": "Ponytail Guy",
        "role": "shopkeeper",
        "desc": (
            "The bored guy behind the counter at Dragon Claw Emporium. "
            "Sells fake swords up top, real stuff underneath."
        ),
        "location": "head_shop",
        "dialogue": [
            "You looking or buying? I don't do window shoppers.",
            "Brass knuckles. Twenty bucks. Best deal on the strip.",
            "Don't tell nobody I sold you that.",
        ],
    },
    "bodega_owner": {
        "name": "Mr. Salazar",
        "role": "shopkeeper",
        "desc": (
            "Stocky guy with a thick mustache and a Louisville Slugger "
            "under the register. Runs the bodega. Doesn't take any crap."
        ),
        "location": "bodega",
        "dialogue": [
            "Buy something or get out.",
            "You think I don't see you looking at the register? I see everything.",
            "This bat ain't for baseball, kid.",
        ],
        "fights_back": True,
        "fight_back_chance": 0.40,
        "fight_back_damage": (4, 8),
        "fight_back_text": "Mr. Salazar grabs the bat from under the counter and swings!",
        "fight_back_death_chance": 0.05,
        "fight_back_death_text": (
            "Mr. Salazar catches you clean across the temple with the bat. "
            "Everything goes white, then nothing."
        ),
    },
    "loose_lip_larry": {
        "name": "Loose-Lip Larry",
        "role": "info",
        "desc": (
            "A skinny guy who hangs out on the strip and talks too much. "
            "He knows who's who and who owes who."
        ),
        "location": "the_strip",
        "dialogue": [
            "You wanna know about Vinnie? He loves that Chevelle more than life.",
            "There's a boom car nobody's watching. Just saying.",
            "Don't mess with Tony V unless you got knuckles at least.",
        ],
    },
}

# ── Police system ──────────────────────────────────────────────────
POLICE = {
    "presence": 0.12,              # base chance of police showing up per move
    "arrest_chance": 0.30,         # chance of arrest if caught doing crime
    "money_loss_pct": 0.50,        # lose 50% of money on arrest
    "respect_loss": 5,             # lose respect on arrest
    "arrest_text": (
        "A police cruiser screeches up. Two officers jump out. "
        "You don't even get a chance to run."
    ),
    "release_text": (
        "They rough you up, take your cash, and dump you back on the street. "
        "Your rep takes a hit."
    ),
}
