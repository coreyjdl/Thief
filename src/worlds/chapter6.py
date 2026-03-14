"""Chapter 6 — The Docks: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  City outskirts, industrial areas — warehouses, delivery depots,
          waterfront docks. Organised crime territory.
Age:      25–28 (late twenties, seasoned criminal).
Boss:     Local mob capo — supervises missions, demands high success rate.
Weapons:  Shotgun, SMG (serious firepower).
Actions:  Gang missions, steal vans, drive-offs, loot pickups.

NARRATIVE
─────────
You've gone professional. No more petty corner-store jobs. Now you're
operating on official gang business — hijacking vans full of unknown
cargo, coordinating timing, tools, and gear.

The "go professional" dialogue from Ch5 transitions directly into
these crew-level operations.

QUEST FLOW
──────────
1. Arrive at the docks. You're running with a crew now.
2. Missions: hijack delivery vans — plan routes, time windows, tools.
3. Van contents include cash, weapon parts, and special components
   that feed into Syndicate missions.
4. Multi-step missions introduced: pick up from one NPC, deliver to
   another, assemble components.
5. Earn respect through successful heists.
6. Challenge the mob capo → scripted loss.
7. Dismantle his supply chain — multiple NPC tasks, deliveries.
8. Confront and beat the capo.
9. Loot from hijacked vans funds explosives and rifles for Ch7.

FORWARD-USE THREAD
──────────────────
Van loot (cash + weapon parts) → fund explosives + rifles for
Syndicate missions. Multi-step NPC delivery pattern established.

LOCATIONS (planned)
───────────────────
- The Docks (hub)
- Container yard
- Delivery depot
- Fish market (front)
- Capo's warehouse (boss arena)
- Pier / boat slip
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
        "The docks — warehouses, delivery depots, and a waterfront "
        "that smells like fish and dirty money. You're running with "
        "a crew now. This is professional."
    ),
}

ITEMS = {
    "shotgun": {
        "name": "Shotgun",
        "desc": "A sawed-off pump-action. Loud, messy, very persuasive.",
        "type": "weapon",
        "damage_bonus": 14,
    },
    "smg": {
        "name": "SMG",
        "desc": (
            "A compact submachine gun that rattles like a sewing machine "
            "from hell. Spray and pray."
        ),
        "type": "weapon",
        "damage_bonus": 12,
    },
    "van_cargo": {
        "name": "Van Cargo",
        "desc": (
            "A sealed package from a hijacked delivery van. Heavy. "
            "Whatever's inside, somebody wants it bad."
        ),
        "type": "quest",
    },
    "weapon_parts": {
        "name": "Weapon Parts",
        "desc": (
            "Disassembled components — trigger assemblies, barrels, springs. "
            "The right person can build something serious with these."
        ),
        "type": "quest",
    },
    "field_medkit": {
        "name": "Field Medkit",
        "desc": "Military surplus. Gauze, morphine syrettes, suture kit.",
        "heal": 30,
        "price": 15,
    },
    "canned_food": {
        "name": "Canned Food",
        "desc": "Canned beans. Cold. Edible. That's all you need.",
        "heal": 10,
        "price": 4,
    },
}

ENEMIES = {
    "dock_worker": {
        "name": "Dock Worker",
        "max_hp": 30, "hp": 30,
        "damage_min": 5, "damage_max": 9,
        "respect_reward": 8,
        "money_drop": (5, 12),
        "desc": (
            "A big guy in coveralls and steel-toed boots. Works the docks "
            "and moonlights as muscle. Arms like ham hocks."
        ),
        "attacks": [
            "swings a cargo hook at your face",
            "throws a crate lid at you like a frisbee",
            "body-checks you into a shipping container",
            "clotheslines you with a thick forearm",
        ],
        "defeat_text": "The dock worker backs off, rubbing his jaw. Break time.",
        "taunt": "Union rules say I can break your face.",
    },
    "smuggler": {
        "name": "Smuggler",
        "max_hp": 28, "hp": 28,
        "damage_min": 6, "damage_max": 10,
        "respect_reward": 9,
        "money_drop": (8, 20),
        "desc": (
            "A weathered man in a peacoat with a pistol tucked in his "
            "waistband. He moves cargo and doesn't like witnesses."
        ),
        "attacks": [
            "fires a shot that grazes your side",
            "pistol-whips you across the temple",
            "throws a heavy net over you and kicks",
            "shoves a crate into you",
        ],
        "defeat_text": "The smuggler vanishes between the containers. Cargo's unguarded.",
        "taunt": "You didn't see nothing. And you won't.",
    },
    "van_driver": {
        "name": "Van Driver",
        "max_hp": 25, "hp": 25,
        "damage_min": 4, "damage_max": 8,
        "respect_reward": 7,
        "money_drop": (5, 15),
        "desc": (
            "The delivery van driver. Not a fighter by trade, but "
            "cornered people do desperate things. He's got a tire iron."
        ),
        "attacks": [
            "swings the tire iron at your head",
            "kicks you in the stomach",
            "throws his phone at your face",
            "slams the van door into you",
        ],
        "defeat_text": "The driver drops the tire iron and runs. The van's yours.",
        "taunt": "This cargo isn't yours! Back off!",
    },
    "capo_enforcer": {
        "name": "Capo's Enforcer",
        "max_hp": 45, "hp": 45,
        "damage_min": 7, "damage_max": 12,
        "respect_reward": 12,
        "money_drop": (10, 25),
        "desc": (
            "A professional. Tailored suit, gold watch, and a silenced "
            "pistol. He handles problems for the capo."
        ),
        "attacks": [
            "fires two quick shots — one grazes your arm",
            "grabs you by the collar with iron hands",
            "drives a knee into your ribs",
            "throws a precise jab that rattles your jaw",
        ],
        "defeat_text": "The enforcer adjusts his cuffs and walks away. He'll be back.",
        "taunt": "The capo sends his regards.",
    },
    "mob_capo": {
        "name": "Salvatore 'The Fish' Moretti",
        "max_hp": 120, "hp": 120,
        "damage_min": 10, "damage_max": 16,
        "respect_reward": 40,
        "desc": (
            "The local mob capo. Fifties, silver hair, always smells like "
            "cigars and cologne. Runs the docks like a business — because "
            "that's exactly what it is. Two enforcers flank him at all "
            "times. He's survived three assassination attempts and doesn't "
            "intend to change that record."
        ),
        "attacks": [
            "pulls out a gold-plated pistol and fires",
            "snaps his fingers and an enforcer hits you from behind",
            "throws a cigar at your face and follows with a fist",
            "grabs a bottle of expensive whiskey and smashes it over your head",
            "cold-cocks you with a punch that belies his age",
        ],
        "defeat_text": (
            "Moretti slumps into his leather chair, blood dripping onto "
            "his silk tie. 'You got talent, kid. Real talent.' He pushes "
            "a set of keys across the desk. 'The vans are yours now.'"
        ),
        "taunt": "Nobody takes from me. Not twice.",
    },
}

LOCATIONS = {
    "the_docks": {
        "name": "The Docks",
        "desc": (
            "A sprawling waterfront of warehouses, cranes, and shipping "
            "containers stacked five high. The air is salt, fish, and "
            "diesel. Crews work day and night moving things that never "
            "show up on any manifest."
        ),
        "connections": ["the_row", "container_yard", "delivery_depot", "fish_market", "pier"],
        "scene": "the_docks",
        "interior": False,
        "loot_table": ["canned_food"],
        "encounter_chance": 0.20,
        "enemies": ["dock_worker", "smuggler"],
        "chapter": 6,
        "hazards": [
            {"text": "A crane swings a load overhead. A cable snaps and whips past your face.", "damage": 3, "chance": 0.06},
            {"text": "You slip on the wet dock and crack your hip on a bollard.", "damage": 2, "chance": 0.10},
            {"text": "A wave crashes over the seawall and knocks you into a pallet.", "damage": 2, "chance": 0.08},
        ],
    },
    "container_yard": {
        "name": "Container Yard",
        "desc": (
            "A maze of shipping containers — red, blue, green, rusted. "
            "Narrow corridors between them. Easy to get lost. Easier to "
            "get ambushed."
        ),
        "connections": ["the_docks", "capo_warehouse"],
        "scene": "container_yard",
        "interior": False,
        "loot_table": ["canned_food", "weapon_parts"],
        "encounter_chance": 0.30,
        "enemies": ["smuggler", "dock_worker", "capo_enforcer"],
        "chapter": 6,
        "hazards": [
            {"text": "A container door bursts open and a crate tumbles out, clipping your leg.", "damage": 3, "chance": 0.08},
            {"text": "You round a corner and walk into a forklift. The forks rake your side.", "damage": 3, "chance": 0.06},
        ],
    },
    "delivery_depot": {
        "name": "Delivery Depot",
        "desc": (
            "A fenced lot full of delivery vans — FedEx, UPS, and "
            "unmarked white ones. This is where the hijack missions start. "
            "A chain-link gate is the only way in."
        ),
        "connections": ["the_docks"],
        "scene": "delivery_depot",
        "interior": False,
        "loot_table": ["van_cargo"],
        "encounter_chance": 0.25,
        "enemies": ["van_driver", "dock_worker"],
        "chapter": 6,
        "hazards": [
            {"text": "A van reverses without looking and you dive out of the way, skinning your hands.", "damage": 2, "chance": 0.10},
        ],
    },
    "fish_market": {
        "name": "The Fish Market",
        "desc": (
            "A covered market that reeks of salt and scales. Fish on ice, "
            "cash under the table. The vendors are connected. This is "
            "where info trades as fast as the catch."
        ),
        "connections": ["the_docks"],
        "scene": "fish_market",
        "interior": True,
        "loot_table": ["canned_food"],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 6,
        "shop": {
            "canned_food": 4,
            "field_medkit": 15,
        },
    },
    "pier": {
        "name": "The Pier",
        "desc": (
            "A rotting wooden pier extending into the harbour. A few "
            "boats bob in the dark water. This is where late-night "
            "deals happen and bodies don't always come back."
        ),
        "connections": ["the_docks"],
        "scene": "pier",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0.15,
        "enemies": ["smuggler"],
        "chapter": 6,
        "hazards": [
            {"text": "A rotted plank gives way. Your leg plunges through to the knee.", "damage": 3, "chance": 0.12},
            {"text": "A wave surges up and drags you against the railing. Splinters dig into your side.", "damage": 2, "chance": 0.08},
        ],
    },
    "capo_warehouse": {
        "name": "Capo's Warehouse",
        "desc": (
            "A heavily guarded warehouse at the end of the container yard. "
            "Reinforced doors, security cameras, and armed men. Moretti "
            "runs his operation from a leather chair inside. Boss arena."
        ),
        "connections": ["container_yard"],
        "scene": "capo_warehouse",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 6,
    },
}

AMBIENT = [
    "A foghorn blasts from somewhere in the harbour.",
    "Seagulls scream and fight over something on the dock.",
    "The smell of fish is so thick you can taste it.",
    "A container crane swings its load in slow, heavy arcs.",
    "You hear the chug of a boat engine idling at the pier.",
    "Dock workers shout orders in three different languages.",
    "A rat the size of a housecat skitters across the wet concrete.",
    "Someone's welding something inside a container — sparks fly out the door.",
    "Water laps against the pilings with a sound like slow applause.",
    "A black sedan with tinted windows rolls slowly through the container yard.",
    "Police boat spotlight sweeps across the harbour.",
    "You hear a van door slam and tires squeal somewhere in the depot.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "fish_monger_sal": {
        "name": "Fish Monger Sal",
        "role": "info / shopkeeper",
        "desc": (
            "An old fisherman turned market vendor. He knows every boat, "
            "every schedule, and every shady deal that goes down at the "
            "docks. Information costs the price of a coffee."
        ),
        "location": "fish_market",
        "dialogue": [
            "The unmarked vans come in at three AM. That's your window.",
            "Moretti's warehouse has two entrances. Back door's weaker.",
            "The enforcers change shift at midnight. Half-hour gap.",
            "Don't go near the pier at night unless you want a swim you won't come back from.",
        ],
        "quest_role": "Gives intel on van schedules, warehouse layout, and guard rotations.",
    },
    "nails": {
        "name": "Nails",
        "role": "crew / quest",
        "desc": (
            "Your crew partner for van hijack missions. A wiry woman "
            "with a shaved head and a toolbox full of lockpicks. She "
            "drives while you grab the cargo."
        ),
        "location": "the_docks",
        "dialogue": [
            "I'll drive, you grab the cargo. We got ninety seconds.",
            "Don't screw this up. Moretti's watching us.",
            "Three vans tonight. We hit the middle one — that's the cash van.",
        ],
        "quest_role": "Crew partner for van hijack missions (multi-step jobs).",
    },
    "eddie_books": {
        "name": "Eddie Books",
        "role": "quest / delivery",
        "desc": (
            "Moretti's accountant. A nervous man in a rumpled suit who "
            "handles the money side. He tells you where to deliver the "
            "van cargo and who gets paid."
        ),
        "location": "capo_warehouse",
        "dialogue": [
            "Take this package to the fish market. Ask for Sal.",
            "Moretti wants the delivery by midnight or it's your neck.",
            "Don't open the cargo. Don't ask what's inside. Just deliver.",
        ],
        "quest_role": "Gives multi-step deliver missions (pick up → deliver to NPC).",
    },
    "harbor_cop": {
        "name": "Officer Ketch",
        "role": "threat",
        "desc": (
            "A harbour patrol officer who's either honest or waiting for "
            "a bigger bribe. He patrols the docks at irregular intervals."
        ),
        "location": "the_docks",
        "dialogue": [
            "Move along. Nothing to see here.",
            "I've got my eye on you.",
            "One more complaint from the dock workers and I'm hauling you in.",
        ],
        "quest_role": "Represents police threat at the docks.",
    },
}

# ── Police system ──────────────────────────────────────────────────
POLICE = {
    "presence": 0.15,
    "arrest_chance": 0.35,
    "money_loss_pct": 0.50,
    "respect_loss": 12,
    "arrest_text": (
        "Harbour patrol. The boat's spotlight pins you against a container "
        "wall. Officers close in from both sides."
    ),
    "release_text": (
        "They confiscate the cargo, empty your pockets, and let you go "
        "with a warning that's not really a warning. Moretti won't be happy."
    ),
}
