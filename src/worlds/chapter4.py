"""Chapter 4 — The Avenue: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  The Avenue — commercial district with alleyways, pawn shops,
          and abandoned lots. At the far end sits a mysterious lab/warehouse
          with strange equipment visible through dusty windows.
Age:      18–19 (just out of high school, no safety net).
Boss:     Rival gang lieutenant — oversees the mission indirectly.
Weapons:  Knife (primary weapon for this chapter).
Actions:  Shake down NPCs, minor theft, tribute runs, hacking/break-in.

QUEST FLOW
──────────
1. Rival gang lieutenant approaches you with a job he can't do himself:
   infiltrate a neutral warehouse/lab to retrieve or deliver an item.
2. The lab has electronic security (locks, coded doors) — can't just
   walk in.
3. Crate loot from Chapter 3 (electronics modules, small arms parts)
   is the key. Explore the avenue to find the tinkerer NPC.
4. Tinkerer's Workshop: trade the crate components → he builds a
   hacking/break-in device.
5. Use the device at the lab: bypass security, open doors, retrieve
   the required item.
6. Guards or trespassers may intervene — knife is your combat option.
7. Deliver or secure the lab item → earn respect, cash, and unlock
   access to Grifter rank missions.

FORWARD-USE THREAD
──────────────────
Ch3 crate → tinkerer → hacking device → neutral lab → knife + cash
→ prepares for Grifter missions in Chapter 5.

The lab is a neutral, narrative-focused location — gives plot and
mission significance to the crate loot without being a combat upgrade.

LOCATIONS (planned)
───────────────────
- The Avenue (hub)
- Tinkerer's workshop
- Dive bar
- Back-alley dice game
- The Lab / neutral warehouse (mission target)
- Lieutenant's corner (quest giver)
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
    "weapon_progression": ["knife"],
    "unlock_actions": ["shake down NPCs", "hacking/break-in"],
    "player_max_hp": 70,
    "setting": (
        "The Avenue — a commercial stretch with alleyways and pawn shops. "
        "At the far end a mysterious lab hums behind dusty windows. "
        "You're not a kid anymore."
    ),
}

ITEMS = {
    "knife": {
        "name": "Knife",
        "desc": "A folding knife with a black handle. Quick and quiet.",
        "type": "weapon",
        "damage_bonus": 7,
    },
    "hacking_device": {
        "name": "Hacking Device",
        "desc": (
            "A jury-rigged gadget built from circuit boards and wiring — "
            "the tinkerer's masterwork. Bypasses electronic locks."
        ),
        "type": "quest",
    },
    "lab_data": {
        "name": "Lab Data Drive",
        "desc": (
            "A small hard drive pulled from the lab's server. Whatever's "
            "on here, somebody wants it bad."
        ),
        "type": "quest",
    },
    "malt_liquor": {
        "name": "Malt Liquor",
        "desc": "A forty in a brown bag. Restores health and dignity — questionable on both.",
        "heal": 10,
        "price": 4,
    },
    "first_aid_kit": {
        "name": "First Aid Kit",
        "desc": "Antiseptic, gauze, and tape. Proper wound care for once.",
        "heal": 20,
        "price": 10,
    },
}

ENEMIES = {
    "corner_thug": {
        "name": "Corner Thug",
        "max_hp": 25, "hp": 25,
        "damage_min": 4, "damage_max": 7,
        "respect_reward": 8,
        "money_drop": (2, 8),
        "desc": "A young man in a hoodie who guards this stretch of sidewalk.",
        "attacks": [
            "swings a heavy fist at your jaw",
            "shoves you into a wall",
            "kicks you in the ribs",
            "throws a wild haymaker",
        ],
        "defeat_text": "The thug backs off, hands up. He knows he's beat.",
        "taunt": "Wrong block, wrong day.",
    },
    "dice_game_enforcer": {
        "name": "Dice Game Enforcer",
        "max_hp": 30, "hp": 30,
        "damage_min": 5, "damage_max": 9,
        "respect_reward": 10,
        "money_drop": (5, 12),
        "desc": (
            "A muscular guy who makes sure nobody cheats at the back-alley "
            "dice game. And by 'cheats' he means 'wins.'"
        ),
        "attacks": [
            "throws a crushing right hook",
            "picks you up and throws you into the garbage",
            "grabs your shirt and headbutts you",
            "stomps on your hand",
        ],
        "defeat_text": "The enforcer sits down heavy, winded. The dice game scatters.",
        "taunt": "House always wins. And I'm the house.",
    },
    "tweaker": {
        "name": "Tweaker",
        "max_hp": 15, "hp": 15,
        "damage_min": 3, "damage_max": 8,
        "respect_reward": 5,
        "money_drop": (0, 3),
        "desc": (
            "Twitchy, skinny, and unpredictable. Could be on anything. "
            "Low HP but hits wild and hard."
        ),
        "attacks": [
            "lunges at you with feral energy",
            "scratches and claws at your face",
            "bites your arm",
            "throws a frantic flurry of punches",
        ],
        "defeat_text": "The tweaker crumples and curls up. He's not getting back up.",
        "taunt": "GAAAAH! I'LL GET YOU!",
    },
    "lab_guard": {
        "name": "Lab Security Guard",
        "max_hp": 35, "hp": 35,
        "damage_min": 5, "damage_max": 8,
        "respect_reward": 10,
        "money_drop": (3, 8),
        "desc": (
            "A private security guard in a black uniform. Baton, radio, "
            "and a bad attitude. He's protecting whatever's in the lab."
        ),
        "attacks": [
            "cracks you across the arm with his baton",
            "jabs the baton into your stomach",
            "shoves you and follows with a knee",
            "swings the baton at your head",
        ],
        "defeat_text": "The guard crumples against the wall, radio squawking.",
        "taunt": "Unauthorized access. You're done.",
    },
    "gang_lieutenant": {
        "name": "D-Block",
        "max_hp": 80, "hp": 80,
        "damage_min": 7, "damage_max": 12,
        "respect_reward": 25,
        "desc": (
            "The rival gang lieutenant. Mid-twenties, cold-eyed, with a "
            "scar running from his left ear to his chin. He set you up "
            "for the lab job and now he wants the data for himself."
        ),
        "attacks": [
            "throws a devastating combination",
            "pulls a chain and whips it across your back",
            "slams you into a car hood",
            "catches you with a brutal uppercut",
            "grabs you by the throat",
        ],
        "defeat_text": (
            "D-Block hits the pavement. He looks up at you with cold fury "
            "but the fight's gone out of him. 'You're dead to this gang,' "
            "he mutters. But you're already walking away."
        ),
        "taunt": "You think you can play my game? I invented it.",
    },
}

LOCATIONS = {
    "the_avenue": {
        "name": "The Avenue",
        "desc": (
            "A busy commercial strip — bodegas, nail salons, check-cashing "
            "places with bars on the windows. The sidewalk's crowded but "
            "nobody makes eye contact. You can feel the gang presence."
        ),
        "connections": ["the_yard", "tinkerer_workshop", "dive_bar", "dice_alley", "the_lab"],
        "scene": "the_avenue",
        "interior": False,
        "loot_table": ["soda_can", "malt_liquor"],
        "encounter_chance": 0.20,
        "enemies": ["corner_thug", "tweaker"],
        "chapter": 4,
        "hazards": [
            {"text": "A car jumps the curb and you have to dive out of the way. You skin your elbows.", "damage": 2, "chance": 0.08},
            {"text": "Someone throws a bottle from a fire escape. Glass rains down on you.", "damage": 2, "chance": 0.06},
        ],
    },
    "tinkerer_workshop": {
        "name": "Tinkerer's Workshop",
        "desc": (
            "A basement shop crammed with circuit boards, soldering irons, "
            "and wires spilling out of every drawer. The tinkerer, Sparks, "
            "hunches over a workbench under a single bulb."
        ),
        "connections": ["the_avenue"],
        "scene": "tinkerer_workshop",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 4,
    },
    "dive_bar": {
        "name": "The Dive Bar",
        "desc": (
            "A dark hole-in-the-wall with sticky floors, a jukebox that "
            "only plays sad country, and regulars who've been sitting on "
            "the same stools since the '90s. Information flows here."
        ),
        "connections": ["the_avenue"],
        "scene": "dive_bar",
        "interior": True,
        "loot_table": ["malt_liquor"],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 4,
        "shop": {
            "malt_liquor": 4,
            "first_aid_kit": 10,
        },
    },
    "dice_alley": {
        "name": "The Dice Alley",
        "desc": (
            "A narrow alley where men crouch around a pair of dice on a "
            "flattened cardboard sheet. Cash changes hands fast. An enforcer "
            "leans against the wall, watching."
        ),
        "connections": ["the_avenue"],
        "scene": "dice_alley",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0.30,
        "enemies": ["dice_game_enforcer", "corner_thug"],
        "chapter": 4,
        "hazards": [
            {"text": "You step on a discarded syringe. The needle pricks through your shoe.", "damage": 2, "chance": 0.10},
        ],
    },
    "lieutenant_corner": {
        "name": "D-Block's Corner",
        "desc": (
            "A corner where D-Block holds court. A black Escalade idles "
            "at the curb. Two runners lean on the wall. This is where "
            "jobs get handed out."
        ),
        "connections": ["the_avenue"],
        "scene": "lieutenant_corner",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 4,
    },
    "the_lab": {
        "name": "The Lab",
        "desc": (
            "A nondescript building at the far end of the avenue. "
            "Dusty windows, a reinforced door with an electronic lock, "
            "and a low hum coming from inside. Whatever they're doing "
            "in there, they don't want visitors."
        ),
        "connections": ["the_avenue"],
        "scene": "the_lab",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0.35,
        "enemies": ["lab_guard"],
        "chapter": 4,
        "hazards": [
            {"text": "A motion sensor triggers and a burst of UV light burns your eyes.", "damage": 2, "chance": 0.10},
            {"text": "You brush against exposed wiring. The shock jolts through your arm.", "damage": 3, "chance": 0.08},
        ],
    },
}

AMBIENT = [
    "A bus rolls past, belching exhaust.",
    "Someone's arguing on a pay-as-you-go phone.",
    "A kid on a bike does a wheelie down the middle of the street.",
    "You smell chicken grease from the carryout on the corner.",
    "A group of guys in matching jackets eye you from a stoop.",
    "A fire hydrant sprays onto the sidewalk. Nobody fixed it.",
    "You hear dice rattling and someone yelling 'Seven! Seven!'",
    "A stray pit bull with a heavy chain trots down the avenue.",
    "The check-cashing place has a line out the door.",
    "Someone spray-painted 'D-BLOCK' on the side of a dumpster.",
    "A police helicopter circles overhead, searchlight sweeping.",
    "A store alarm goes off. Nobody even looks up.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "sparks": {
        "name": "Sparks",
        "role": "quest / craft",
        "desc": (
            "The tinkerer. A nervous genius who can build anything from "
            "junk. He needs the electronics crate components from Ch3 "
            "to build the hacking device."
        ),
        "location": "tinkerer_workshop",
        "dialogue": [
            "You got circuit boards? Good ones? I can build something.",
            "Give me the electronics and I'll make you a skeleton key for any lock.",
            "Don't rush me. Soldering takes patience. Unlike you.",
        ],
        "quest_role": "Trades crate loot for hacking device (Ch4 key item).",
    },
    "barkeep_ray": {
        "name": "Barkeep Ray",
        "role": "info / shopkeeper",
        "desc": (
            "The bartender at the dive bar. Vietnam vet, missing two "
            "fingers on his left hand. Hears everything, says little — "
            "unless you buy a drink."
        ),
        "location": "dive_bar",
        "dialogue": [
            "D-Block's been moving product through the lab. That's his play.",
            "The lab has electronic locks. You ain't kicking that door down.",
            "You want info? Buy a drink first.",
            "The guards change shift at midnight. Just saying.",
        ],
        "quest_role": "Gives intel on lab security and D-Block's operation.",
        "fights_back": False,
    },
    "d_block_runner": {
        "name": "Little Chris",
        "role": "quest",
        "desc": (
            "One of D-Block's runners. A skinny sixteen-year-old who "
            "delivers messages and picks up packages. He tells you where "
            "D-Block wants to meet."
        ),
        "location": "the_avenue",
        "dialogue": [
            "D-Block wants to see you. His corner. Don't keep him waiting.",
            "I'm just the messenger, man. Don't shoot me.",
            "You did the lab job? Respect. D-Block's got something for you.",
        ],
        "quest_role": "Delivers quest triggers from D-Block to player.",
    },
    "pawn_jenny": {
        "name": "Pawn Shop Jenny",
        "role": "shopkeeper",
        "desc": (
            "Runs a small pawn shop on the avenue. Tattoos up both arms, "
            "a nose ring, and a shotgun behind the door frame. She sells "
            "knives and first aid supplies."
        ),
        "location": "the_avenue",
        "dialogue": [
            "Need a knife? Thirty bucks. It's sharp.",
            "Don't try anything stupid. I've got a twelve-gauge back here.",
        ],
        "fights_back": True,
        "fight_back_chance": 0.45,
        "fight_back_damage": (8, 15),
        "fight_back_text": "Jenny grabs the shotgun from behind the door and fires a warning shot. It grazes you!",
        "fight_back_death_chance": 0.10,
        "fight_back_death_text": (
            "Jenny doesn't miss twice. The shotgun blast catches you "
            "square in the chest. You're dead before you hit the floor."
        ),
    },
}

# ── Police system ──────────────────────────────────────────────────
POLICE = {
    "presence": 0.15,
    "arrest_chance": 0.35,
    "money_loss_pct": 0.50,
    "respect_loss": 8,
    "arrest_text": (
        "Sirens. Two squad cars block the avenue. Officers slam you "
        "against the hood."
    ),
    "release_text": (
        "They take your cash, rough you up, and leave you on the curb. "
        "Word spreads — your rep takes a hit."
    ),
}
