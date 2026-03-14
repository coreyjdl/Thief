"""Chapter 7 — The Heights: items, enemies, locations, ambient flavour.

DESIGN NOTES
─────────────
Setting:  High-end heist locations — mansions, high-tech warehouses,
          black-market labs. The player has climbed from the gutter to the
          glass towers.
Age:      30–35 (thirties, at the peak of criminal career).
Boss:     Rival syndicate leader — in a robotic exo-suit.
Weapons:  Explosives, rifles (military-grade hardware).
Actions:  High-end heists, assemble/deliver items, coordinated strikes.

NARRATIVE
─────────
You discover that the items you stole from the lab back in Chapter 4
were for something sinister your current boss is working on. The
stakes are no longer about turf — this is about what's being built
with the things you helped steal.

The rival syndicate leader has access to military-grade tech. To beat
him you need a special assembled weapon — something absurd, like he's
in a robotic exo-suit and you need a laser launcher crafted from
components scavenged across Syndicate missions.

QUEST FLOW
──────────
1. Arrive at the Heights. Van loot from Ch6 funds explosives + rifles.
2. High-end heist missions: mansions, vaults, black-market labs.
3. Discovery: lab items from Ch4 are being used for something sinister.
4. Grind respect through heists and coordinated strikes.
5. Challenge rival syndicate leader → scripted loss (exo-suit).
6. Assemble special weapon: requires multiple components from
   different missions and NPC deliveries.
   • Component A: scavenged from a heist target.
   • Component B: traded from a black-market NPC.
   • Component C: recovered from a prior-chapter thread.
7. Craft the laser launcher (or similar absurd weapon).
8. Fight the exo-suit boss with the assembled weapon.
9. Victory: unlocks Boss Level and the final confrontation.

FORWARD-USE THREAD
──────────────────
Multi-component assembly pattern peaks here. Everything from prior
chapters converges. Special weapon carries into Boss Level.

LOCATIONS (planned)
───────────────────
- The Heights (hub)
- Private club
- Penthouse tower
- Black-market lab
- Mansion target
- Rooftop arena (boss fight)
"""

META = {
    "number": 7,
    "title": "The Heights",
    "age": 32,
    "era": "Thirties",
    "rank": "Syndicate",
    "respect_range": (400, 800),
    "boss": "TBD — Rival syndicate leader (exo-suit)",
    "boss_id": "syndicate_leader",
    "weapon_progression": ["explosives", "rifles", "laser launcher"],
    "unlock_actions": ["high-end heists", "assemble weapons"],
    "player_max_hp": 160,
    "setting": (
        "The Heights — glass towers and private clubs where the real "
        "money moves. You started on the block. Now you're looking down "
        "from forty floors up. The view comes with a price."
    ),
}

ITEMS = {
    "explosives": {
        "name": "Explosives",
        "desc": "C-4 blocks with detonators. Opens any door — permanently.",
        "type": "weapon",
        "damage_bonus": 18,
    },
    "rifle": {
        "name": "Assault Rifle",
        "desc": "Military-grade AR-15. Accurate, reliable, deadly.",
        "type": "weapon",
        "damage_bonus": 16,
    },
    "laser_launcher": {
        "name": "Laser Launcher",
        "desc": (
            "A jury-rigged energy weapon assembled from three stolen "
            "components. It hums with barely-contained power. The only "
            "thing that can crack an exo-suit."
        ),
        "type": "weapon",
        "damage_bonus": 25,
    },
    "laser_component_a": {
        "name": "Power Cell",
        "desc": "A high-density power cell scavenged from a heist target.",
        "type": "quest",
    },
    "laser_component_b": {
        "name": "Focusing Array",
        "desc": "A precision lens assembly from the black-market lab.",
        "type": "quest",
    },
    "laser_component_c": {
        "name": "Control Module",
        "desc": (
            "A circuit board from the Ch4 lab — the sinister thing they "
            "were building. Repurposed as a weapon controller."
        ),
        "type": "quest",
    },
    "trauma_kit": {
        "name": "Trauma Kit",
        "desc": "Professional trauma supplies. Stabilises serious injuries.",
        "heal": 45,
        "price": 25,
    },
    "energy_bar_pro": {
        "name": "MRE",
        "desc": "Military ration. Tastes like cardboard but keeps you going.",
        "heal": 15,
        "price": 8,
    },
}

ENEMIES = {
    "private_security": {
        "name": "Private Security",
        "max_hp": 40, "hp": 40,
        "damage_min": 7, "damage_max": 12,
        "respect_reward": 10,
        "money_drop": (10, 20),
        "desc": (
            "A professional in a tailored black suit with an earpiece and "
            "a concealed weapon. Guards the Heights with precision."
        ),
        "attacks": [
            "fires two quick shots from a silenced pistol",
            "throws a precise palm strike to your sternum",
            "sweeps your legs and follows with an elbow drop",
            "grabs your arm and twists it into a joint lock",
        ],
        "defeat_text": "The guard crumples, earpiece squawking. More will come.",
        "taunt": "You're not on the guest list.",
    },
    "syndicate_soldier": {
        "name": "Syndicate Soldier",
        "max_hp": 50, "hp": 50,
        "damage_min": 8, "damage_max": 14,
        "respect_reward": 12,
        "money_drop": (15, 30),
        "desc": (
            "A hardened operative in tactical gear. Body armour, assault "
            "rifle, and the dead eyes of someone who's done this a hundred "
            "times."
        ),
        "attacks": [
            "fires a burst that rips through the air around you",
            "throws a flashbang and follows with a tackle",
            "jabs the rifle stock into your face",
            "fires and a round grazes your ribs",
        ],
        "defeat_text": "The soldier goes down hard. His radio crackles with panic.",
        "taunt": "Target acquired. Engaging.",
    },
    "mansion_guard": {
        "name": "Mansion Guard",
        "max_hp": 35, "hp": 35,
        "damage_min": 6, "damage_max": 11,
        "respect_reward": 9,
        "money_drop": (8, 18),
        "desc": (
            "A guard in a grey uniform patrolling a mansion estate. "
            "He's got a Taser and a radio. Not elite, but not a pushover."
        ),
        "attacks": [
            "fires the Taser — the prongs dig into your chest",
            "swings a heavy flashlight at your head",
            "tackles you onto the marble floor",
            "shoves you into a glass display case",
        ],
        "defeat_text": "The guard slumps against the wall, reaching for his radio. Too slow.",
        "taunt": "Intruder! Stop right there!",
    },
    "lab_scientist": {
        "name": "Lab Scientist",
        "max_hp": 15, "hp": 15,
        "damage_min": 2, "damage_max": 5,
        "respect_reward": 4,
        "money_drop": (5, 10),
        "desc": (
            "A panicked scientist in a lab coat. Not a fighter, but "
            "cornered people do stupid things. He's swinging a fire "
            "extinguisher."
        ),
        "attacks": [
            "swings the fire extinguisher at you",
            "sprays chemical foam in your face",
            "throws a beaker that shatters on you",
            "pushes a rack of equipment at you",
        ],
        "defeat_text": "The scientist drops to his knees. 'I'm just a researcher! Please!'",
        "taunt": "Stay back! I'll — I'll call security!",
    },
    "syndicate_leader": {
        "name": "Viktor Kessler",
        "max_hp": 180, "hp": 180,
        "damage_min": 14, "damage_max": 22,
        "respect_reward": 50,
        "desc": (
            "The rival syndicate leader. Ex-military, mid-forties, with "
            "a cold German accent and colder eyes. He's wearing a robotic "
            "exo-suit — hydraulic limbs, titanium plating, and a heads-up "
            "display behind his visor. Without the laser launcher, you "
            "can't even scratch him."
        ),
        "attacks": [
            "swings an exo-suit fist that cracks the concrete where you stood",
            "fires a mounted turret — bullets chew through the wall behind you",
            "charges forward with hydraulic-powered speed and slams you",
            "grabs you with a mechanical hand and throws you across the room",
            "activates the suit's shock system — electricity arcs through the floor",
        ],
        "defeat_text": (
            "The exo-suit sparks and seizes. Kessler stumbles, smoke pouring "
            "from the joints. The visor cracks and he pulls it off, blood "
            "running from his nose. 'Impossible,' he whispers. Then the "
            "suit collapses and takes him with it."
        ),
        "taunt": "This suit cost more than your entire life. Come test it.",
    },
}

LOCATIONS = {
    "the_heights": {
        "name": "The Heights",
        "desc": (
            "A gleaming high-rise district of glass towers, luxury stores, "
            "and rooftop bars. The streets are clean, the cars are expensive, "
            "and the crime is invisible. Up here, money protects money."
        ),
        "connections": ["the_docks", "private_club", "penthouse_tower", "black_market_lab", "mansion_target"],
        "scene": "the_heights",
        "interior": False,
        "loot_table": ["energy_bar_pro"],
        "encounter_chance": 0.18,
        "enemies": ["private_security"],
        "chapter": 7,
        "hazards": [
            {"text": "A window washer's bucket falls from above. It catches your shoulder.", "damage": 2, "chance": 0.06},
            {"text": "You step onto a glass panel and it cracks under your weight.", "damage": 2, "chance": 0.05},
        ],
    },
    "private_club": {
        "name": "The Private Club",
        "desc": (
            "Velvet ropes, a bouncer built like a fridge, and music "
            "throbbing through the walls. Inside: expensive drinks, "
            "expensive people, and deals worth millions whispered over "
            "champagne."
        ),
        "connections": ["the_heights"],
        "scene": "private_club",
        "interior": True,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 7,
    },
    "penthouse_tower": {
        "name": "Penthouse Tower",
        "desc": (
            "A fifty-story residential tower. The top floors are owned "
            "by people who fly private. Security cameras in every hallway, "
            "keycard-locked elevators, and guards on every floor."
        ),
        "connections": ["the_heights", "rooftop_arena"],
        "scene": "penthouse_tower",
        "interior": True,
        "loot_table": ["trauma_kit"],
        "encounter_chance": 0.30,
        "enemies": ["private_security", "syndicate_soldier"],
        "chapter": 7,
        "hazards": [
            {"text": "An elevator cable snaps and the car drops two floors before the brake catches.", "damage": 4, "chance": 0.05},
            {"text": "You trip a laser alarm and a steel security door slams into your side.", "damage": 3, "chance": 0.08},
        ],
    },
    "black_market_lab": {
        "name": "Black-Market Lab",
        "desc": (
            "A hidden lab behind a legitimate tech company. Clean rooms, "
            "centrifuges, and equipment that shouldn't exist outside a "
            "government facility. This is where the sinister project "
            "lives."
        ),
        "connections": ["the_heights"],
        "scene": "black_market_lab",
        "interior": True,
        "loot_table": ["laser_component_b"],
        "encounter_chance": 0.35,
        "enemies": ["lab_scientist", "syndicate_soldier"],
        "chapter": 7,
        "hazards": [
            {"text": "You knock over a rack of chemicals. The fumes burn your lungs.", "damage": 3, "chance": 0.10},
            {"text": "A containment field sparks and arcs of electricity jump to your metal weapon.", "damage": 4, "chance": 0.06},
        ],
    },
    "mansion_target": {
        "name": "The Mansion",
        "desc": (
            "A sprawling estate behind iron gates. Marble floors, art "
            "worth more than buildings, and a security system that would "
            "make a bank jealous. Your heist target."
        ),
        "connections": ["the_heights"],
        "scene": "mansion_target",
        "interior": False,
        "loot_table": ["laser_component_a"],
        "encounter_chance": 0.25,
        "enemies": ["mansion_guard", "private_security"],
        "chapter": 7,
        "hazards": [
            {"text": "Guard dogs. A Doberman catches your calf before you clear the fence.", "damage": 3, "chance": 0.10},
            {"text": "Motion sensors trigger a spotlight and you run into a stone pillar.", "damage": 2, "chance": 0.08},
        ],
    },
    "rooftop_arena": {
        "name": "The Rooftop",
        "desc": (
            "The top of the penthouse tower. Open sky, city lights "
            "spreading to the horizon, and a cold wind that cuts through "
            "everything. This is where you fight Viktor Kessler."
        ),
        "connections": ["penthouse_tower"],
        "scene": "rooftop_arena",
        "interior": False,
        "loot_table": [],
        "encounter_chance": 0,
        "enemies": [],
        "chapter": 7,
        "hazards": [
            {"text": "The wind catches you off-balance near the edge. Your heart stops before your feet do.", "damage": 2, "chance": 0.08},
        ],
    },
}

AMBIENT = [
    "A helicopter drifts between the towers, searchlight sweeping.",
    "You catch a whiff of expensive perfume and cigar smoke.",
    "A sports car rumbles past, engine worth more than a house.",
    "Someone's champagne glass shatters on the sidewalk forty floors below.",
    "A security drone buzzes overhead, camera lens rotating.",
    "You hear classical music drifting from an open penthouse window.",
    "Two men in suits shake hands outside a private club. A briefcase changes hands.",
    "A limousine idles at the curb, engine purring like a cat.",
    "Window-washing platforms sway in the wind, chains creaking.",
    "The city sprawls below you — everything you came from, everything you left.",
    "A private security patrol walks past, radios crackling.",
    "You see your reflection in a glass tower. You barely recognise yourself.",
]

# ── NPCs (non-combat, narrative / info / quest) ────────────────────
NPCS = {
    "ghost": {
        "name": "Ghost",
        "role": "info / quest",
        "desc": (
            "A legendary thief who retired at the top. Nobody knows his "
            "real name. He operates from the private club, trading intel "
            "for favours. He knows about the sinister project."
        ),
        "location": "private_club",
        "dialogue": [
            "The things you stole from that lab? They're building a weapon. A big one.",
            "Kessler has an exo-suit. Military prototype. Nothing conventional can touch it.",
            "You need three things to build something that can. I know where they are.",
            "The power cell is in the mansion vault. The array is in the lab. The module — you already have it.",
        ],
        "quest_role": "Reveals sinister plot, tells player how to assemble laser launcher.",
    },
    "dr_chen": {
        "name": "Dr. Chen",
        "role": "quest / craft",
        "desc": (
            "A disgraced weapons researcher who was fired from Kessler's "
            "operation. She can assemble the laser launcher from the three "
            "components if you bring them to her."
        ),
        "location": "black_market_lab",
        "dialogue": [
            "I designed the focusing array. I can reverse-engineer the weapon.",
            "Bring me the power cell, the array, and the control module. I'll build it.",
            "Kessler stole my research. This is personal.",
        ],
        "quest_role": "Assembles laser launcher from 3 components (Ch7 key weapon).",
    },
    "concierge_marco": {
        "name": "Concierge Marco",
        "role": "info",
        "desc": (
            "The concierge at the penthouse tower. He's been bribed by "
            "everyone. For the right price, he'll tell you the guard "
            "rotations, elevator codes, and Kessler's schedule."
        ),
        "location": "penthouse_tower",
        "dialogue": [
            "Kessler's on the rooftop every night at midnight. He likes the view.",
            "The service elevator doesn't have cameras. Code is 7734.",
            "Two guards on forty, one on forty-five. Nobody on forty-seven after ten.",
        ],
        "quest_role": "Gives intel on guard rotations and Kessler's location.",
    },
    "art_dealer_sylvia": {
        "name": "Sylvia",
        "role": "info / fence",
        "desc": (
            "An art dealer who fences stolen goods from the mansions. "
            "She buys what you steal and tells you which houses are worth "
            "hitting."
        ),
        "location": "the_heights",
        "dialogue": [
            "The Carrington mansion has a Monet in the east wing. Worth hitting.",
            "Don't touch the Hendricks place. Private army. Literally.",
            "I'll buy anything you grab. Sixty cents on the dollar.",
        ],
        "quest_role": "Info on heist targets, buys stolen goods.",
    },
}

# ── Police system ──────────────────────────────────────────────────
POLICE = {
    "presence": 0.20,
    "arrest_chance": 0.40,
    "money_loss_pct": 0.60,
    "respect_loss": 15,
    "arrest_text": (
        "Tactical unit. They came in silent — black van, body armour, "
        "automatic weapons. Your face is on the pavement before you "
        "hear the siren."
    ),
    "release_text": (
        "They take everything. Cash, weapons, intel. Forty-eight hours "
        "in a holding cell. When they let you go, your reputation's in ashes."
    ),
}
