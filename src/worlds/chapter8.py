"""Chapter 8 — The Crown: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  The city itself — syndicate HQ, high-tech complex, and a return
          to where it all started. The final chapter.
Age:      35+ (the endgame).
Boss:     The City Kingpin — the ultimate boss. Has been pulling strings
          since Chapter 1.
Weapons:  All previously acquired weapons + special items.
Actions:  Final challenge — multi-step, uses all prior tools and actions.

NARRATIVE
─────────
Ultimate confrontation with the City Kingpin. You started as a
fourteen-year-old kid getting shoved around on the block. Now you
control the block, the strip, the yard, the avenue, the row, the
docks, the heights — or you will, after tonight.

The Kingpin fight uses all previously acquired weapons, cash, and
special items from earlier missions. Multi-step strategies: hack
doors, deliver items mid-battle, use explosives to break defences.

Success requires the player to have kept, used, and assembled all
forward-thread items, completing the story arc.

QUEST FLOW
──────────
1. All prior territories are accessible. The kingpin controls the city.
2. Gather final intel — revisit locations from earlier chapters.
3. Assemble final loadout from all accumulated weapons and items.
4. Multi-phase final boss with callbacks to every chapter:
   • Phase 1: breach the complex (explosives, hacking device).
   • Phase 2: fight through guards (rifles, shotgun, SMG).
   • Phase 3: face the kingpin (special weapons, laser launcher).
5. Victory: you run the city — or burn it down trying.

FORWARD-USE THREAD
──────────────────
Everything converges. Every forward-thread item from Ch1–Ch7 has a
role in the final battle.

LOCATIONS (planned)
───────────────────
- Syndicate HQ / high-tech complex (hub)
- The old block (return to where it started)
- Kingpin's stronghold (final boss arena)
- Rooftop / helipad (climax scene)
- Underground bunker
"""

META = {
    "number": 8,
    "title": "The Crown",
    "age": 36,
    "era": "Late thirties — the endgame",
    "rank": "Boss Level",
    "respect_range": (800, None),
    "boss": "The City Kingpin",
    "boss_id": "kingpin",
    "weapon_progression": ["all prior weapons", "special weapons"],
    "unlock_actions": ["final challenge"],
    "player_max_hp": 200,
    "setting": (
        "The whole city. You started as a fourteen-year-old kid getting "
        "shoved around on the block. Now the block, the strip, the yard, "
        "the avenue, the row, the docks, the heights — they're all yours. "
        "Or they will be, after tonight."
    ),
}

ITEMS = {
    "master_key": {
        "name": "Master Key",
        "desc": (
            "A key that opens every door in the complex. Taken from "
            "a guard who won't need it anymore."
        ),
        "type": "quest",
    },
    "final_explosive": {
        "name": "Breaching Charge",
        "desc": "A shaped charge built for armoured doors. One use.",
        "type": "quest",
    },
    "combat_stim": {
        "name": "Combat Stimulant",
        "desc": "Military adrenaline shot. Hurts going in, heals coming out.",
        "heal": 50,
        "price": 30,
    },
    "armour_vest": {
        "name": "Armour Vest",
        "desc": "Kevlar vest. Won't stop everything but it helps.",
        "type": "armour",
        "damage_reduction": 3,
    },
    "kingpin_intel": {
        "name": "Kingpin Dossier",
        "desc": (
            "A folder containing photos, schedules, weaknesses. "
            "Everything you need to plan the final assault."
        ),
        "type": "quest",
    },
}

ENEMIES = {
    "elite_guard": {
        "name": "Elite Guard",
        "max_hp": 55, "hp": 55,
        "damage_min": 10, "damage_max": 16,
        "respect_reward": 14,
        "money_drop": (15, 30),
        "desc": (
            "Ex-special forces in full tactical gear. Night vision, "
            "body armour, and a rifle that's seen real combat. These "
            "are the Kingpin's personal security."
        ),
        "attacks": [
            "fires a controlled burst — rounds crack past your ear",
            "throws a stun grenade and rushes you",
            "drives a knee into your chest with trained precision",
            "grabs you in a choke hold from behind",
        ],
        "defeat_text": "The guard drops. His radio squawks. More on the way.",
        "taunt": "You're already dead. You just don't know it yet.",
    },
    "armoured_merc": {
        "name": "Armoured Mercenary",
        "max_hp": 70, "hp": 70,
        "damage_min": 12, "damage_max": 18,
        "respect_reward": 16,
        "money_drop": (20, 40),
        "desc": (
            "A foreign mercenary in full plate carrier and helmet. "
            "He carries a light machine gun and doesn't flinch."
        ),
        "attacks": [
            "opens fire with the machine gun — the wall behind you explodes",
            "throws you into a wall with cybernetic-enhanced strength",
            "fires a grenade launcher round that detonates near you",
            "charges and tackles you through a door",
        ],
        "defeat_text": "The merc crashes through a table. His armour saved him but he's done fighting.",
        "taunt": "I've killed men in six countries. You're just number seven.",
    },
    "kingpin_lieutenant": {
        "name": "The Ghost Hand",
        "max_hp": 60, "hp": 60,
        "damage_min": 10, "damage_max": 15,
        "respect_reward": 15,
        "money_drop": (15, 30),
        "desc": (
            "The Kingpin's right hand. A woman in a black suit with "
            "white gloves. She fights with martial arts precision and "
            "a silenced pistol."
        ),
        "attacks": [
            "fires two precise shots from a silenced pistol",
            "delivers a spinning kick to your jaw",
            "throws a knife that slices your arm",
            "sweeps your legs and stomps on your hand",
        ],
        "defeat_text": "She hits the floor, white gloves stained red. 'He'll kill you,' she whispers.",
        "taunt": "The Kingpin sees everything. You're already in the grave.",
    },
    "kingpin": {
        "name": "The Kingpin — Alexander Cross",
        "max_hp": 250, "hp": 250,
        "damage_min": 16, "damage_max": 25,
        "respect_reward": 100,
        "desc": (
            "Alexander Cross. The man behind every string in this city. "
            "Late fifties, iron-grey hair, and the calm of someone who's "
            "never had to fight his own battles — until now. He stands "
            "behind a desk made of bulletproof glass, wearing a custom "
            "suit that probably costs more than the block you grew up on. "
            "He's got a golden Desert Eagle in one hand and a detonator "
            "in the other."
        ),
        "attacks": [
            "fires the Desert Eagle — the .50 cal round tears through the air",
            "presses the detonator — an explosion rocks the floor beneath you",
            "signals and ceiling-mounted turrets open fire",
            "throws a smoke grenade and fires through the cloud",
            "slams a titanium briefcase into your face",
            "activates a floor panel — electric current surges through your boots",
        ],
        "defeat_text": (
            "Cross falls behind his desk. The golden gun clatters across "
            "bullet-proof glass. He looks up at you — not with fear, but "
            "with something like recognition. 'You're just like me,' he says. "
            "'Twenty years ago I was standing right where you are.' "
            "The detonator rolls from his hand. The city is yours."
        ),
        "taunt": "I built this city's shadow. You think you can take it?",
    },
}

LOCATIONS = {
    "syndicate_hq": {
        "name": "Syndicate HQ",
        "desc": (
            "A fortified high-tech complex on the edge of the city. "
            "Concrete walls, razor wire, and armed guards at every "
            "checkpoint. This is the nerve center. Everything leads here."
        ),
        "connections": ["the_heights", "old_block", "underground_bunker", "kingpin_stronghold"],
        "scene": "syndicate_hq",
        "interior": False,
        "loot_table": ["combat_stim"],
        "encounter_chance": 0.30,
        "enemies": ["elite_guard", "armoured_merc"],
        "chapter": 8,
        "hazards": [
            {"text": "A motion sensor triggers and a security door slams into your side.", "damage": 4, "chance": 0.08},
            {"text": "You step on a pressure plate. A gas canister pops and your eyes burn.", "damage": 3, "chance": 0.06},
            {"text": "Razor wire hidden in the grass catches your ankle.", "damage": 3, "chance": 0.08},
        ],
    },
    "old_block": {
        "name": "The Old Block",
        "desc": (
            "The block where it all started. Same cracked sidewalks, "
            "same tired brick houses. But now you see it different. "
            "The Kingpin's influence starts here — always has. Even "
            "Marcus worked for someone."
        ),
        "connections": ["syndicate_hq"],
        "scene": "old_block",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0.10,
        "enemies": ["elite_guard"],
        "chapter": 8,
    },
    "underground_bunker": {
        "name": "The Underground Bunker",
        "desc": (
            "Beneath the complex. Reinforced concrete, blast doors, and "
            "a server room humming with data. This is where the Kingpin "
            "stores his secrets — and his escape route."
        ),
        "connections": ["syndicate_hq", "kingpin_stronghold"],
        "scene": "underground_bunker",
        "interior": True,
        "loot_table": ["combat_stim", "armour_vest"],
        "encounter_chance": 0.35,
        "enemies": ["elite_guard", "kingpin_lieutenant"],
        "chapter": 8,
        "hazards": [
            {"text": "An automated turret activates and sprays bullets. One grazes your arm.", "damage": 5, "chance": 0.08},
            {"text": "A blast door slams shut and the pressure wave knocks you off your feet.", "damage": 3, "chance": 0.06},
            {"text": "A pipe bursts overhead, scalding steam hits your shoulder.", "damage": 3, "chance": 0.08},
        ],
    },
    "kingpin_stronghold": {
        "name": "Kingpin's Stronghold",
        "desc": (
            "The top floor. Floor-to-ceiling windows overlooking the "
            "entire city. A bulletproof glass desk, a minibar, and "
            "Alexander Cross sitting in a leather chair, waiting. "
            "He knew you were coming. He's always known."
        ),
        "connections": ["underground_bunker"],
        "scene": "kingpin_stronghold",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 8,
    },
    "rooftop_helipad": {
        "name": "The Helipad",
        "desc": (
            "The rooftop. A helicopter sits idle, rotors still. The city "
            "sprawls below in a carpet of lights. This is the escape route — "
            "or the place where it all ends."
        ),
        "connections": ["kingpin_stronghold"],
        "scene": "rooftop_helipad",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 8,
        "hazards": [
            {"text": "The helicopter's rotor wash nearly throws you off the edge.", "damage": 3, "chance": 0.08},
        ],
    },
}

AMBIENT = [
    "Searchlights sweep the complex perimeter.",
    "You hear radio chatter — your name crackles through static.",
    "A helicopter circles overhead, spotlight probing.",
    "The hum of generators vibrates through the floor.",
    "Somewhere below, a door slams. Then silence.",
    "You can see the whole city from here. Every block you fought through.",
    "An alarm blares, then cuts off. Someone silenced it.",
    "Bullet holes in the wall tell stories of others who tried.",
    "The air smells like gunpowder and expensive aftershave.",
    "Camera feeds flicker on monitors — you see yourself on one of them.",
    "You hear Cross's voice on the intercom: 'I've been expecting you.'",
    "The city lights shimmer below. It all comes down to tonight.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "prophet": {
        "name": "The Prophet",
        "role": "info / quest",
        "desc": (
            "A former Kingpin insider who defected. He lives in hiding "
            "on the old block. He gives you the Kingpin dossier — schedules, "
            "weaknesses, and the layout of the stronghold."
        ),
        "location": "old_block",
        "dialogue": [
            "Cross has two weaknesses. His ego and his escape route.",
            "The bunker connects to the stronghold. That's your way in.",
            "I worked for him for fifteen years. I know every camera blind spot.",
            "Take this dossier. It's everything I've got. Make it count.",
        ],
        "quest_role": "Gives Kingpin dossier and stronghold intel.",
    },
    "nails_again": {
        "name": "Nails",
        "role": "crew / support",
        "desc": (
            "Your old crew partner from the docks. She's here for the "
            "final job. She'll cut the power when you give the signal."
        ),
        "location": "syndicate_hq",
        "dialogue": [
            "I'll cut the power on your signal. You've got sixty seconds of darkness.",
            "We started stealing vans. Now we're taking down the Kingpin. Life's funny.",
            "Don't die in there. I need someone to buy me a drink after.",
        ],
        "quest_role": "Crew support for final assault (cuts power on signal).",
    },
    "sparks_again": {
        "name": "Sparks",
        "role": "tech support",
        "desc": (
            "The tinkerer from Ch4 — older now, better equipped. He "
            "hacks the stronghold's security system remotely while you "
            "fight through."
        ),
        "location": "underground_bunker",
        "dialogue": [
            "I'm in their system. Disabling cameras... now.",
            "The blast doors run on a separate circuit. Give me two minutes.",
            "Cross has a kill switch in his desk. Don't let him press it.",
        ],
        "quest_role": "Remote tech support — disables cameras and doors.",
    },
    "ghost_again": {
        "name": "Ghost",
        "role": "info",
        "desc": (
            "The legendary thief from The Heights. He's watching from "
            "a distance. One final piece of advice."
        ),
        "location": "syndicate_hq",
        "dialogue": [
            "Everything you've done led to this. Every brick, every knife, every laser.",
            "Cross isn't the city. The city is bigger than any one man.",
            "Win or lose — the game doesn't stop. Remember that.",
        ],
        "quest_role": "Final narrative closure / philosophical sendoff.",
    },
    "officer_shaw": {
        "name": "Detective Shaw",
        "role": "threat / wild card",
        "desc": (
            "An honest cop who's been building a case against Cross for "
            "years. He might arrest you, or he might look the other way — "
            "depending on how you play it."
        ),
        "location": "syndicate_hq",
        "dialogue": [
            "I know what you're doing. I should stop you.",
            "Cross has people in the department. I can't trust anyone.",
            "Get him. Then we'll talk about your rap sheet.",
        ],
        "quest_role": "Potential ally or threat — police wild card.",
    },
}

# ── Police system ──────────────────────────────────────────────────
POLICE = {
    "presence": 0.25,
    "arrest_chance": 0.45,
    "money_loss_pct": 0.70,
    "respect_loss": 20,
    "arrest_text": (
        "SWAT team. They breach from three directions with flashbangs and "
        "automatic weapons. You don't even get to draw."
    ),
    "release_text": (
        "Forty-eight hours in federal holding. They take everything — "
        "money, weapons, intel. When they release you, your operation "
        "is in shambles."
    ),
}
