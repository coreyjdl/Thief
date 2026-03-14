# THIEF

*A text-based crime RPG about climbing from nothing.*

You're fourteen, small for your age, and at the bottom of every food chain that matters.
The block's got a pecking order — and right now you're somewhere below the pigeons.
But today's gonna be different.

## How to play

```bash
cd src
python main.py
```

Requires **Python 3.8+** — no external dependencies.

## Rank progression

| Respect | Rank          | Age    | Era                    | Weapons              | Boss / Quest Thread                                                                                 |
| ------- | ------------- | ------ | ---------------------- | -------------------- | --------------------------------------------------------------------------------------------------- |
| 0–10    | Push-over Kid | 14     | Middle school          | fists → loose brick  | Bully: Marcus. Scuff triggers fight. $20 from Mom → brass knuckles at Head Shop (Ch2)               |
| 10–25   | Fighter       | 15     | High school freshman   | brass knuckles       | Vinnie "Chrome" Lucca. Chevelle scratch → car stereo quest → pawned for crowbar                     |
| 25–50   | Punk          | 16–17  | High school upperclass | crowbar (pawn shop)  | Skinhead leader. Trade busted stereo → crowbar → warehouse crate (electronics/parts) → Ch4 tinkerer |
| 50–100  | Street Thug   | 18–19  | Just out of school     | knife                | Gang lieutenant. Crate loot → tinkerer → hacking device → infiltrate neutral lab                    |
| 100–200 | Grifter       | 20–22  | Early twenties         | cheap pistol         | Corrupt store owner + bodyguards. Petty crime → "go professional" dialogue → Crew missions          |
| 200–400 | Crew Member   | 25–28  | Late twenties          | shotgun, SMG         | Mob capo. Hijack vans → loot cash & weapon parts → fund Syndicate gear                              |
| 400–800 | Syndicate     | 30–35  | Thirties               | explosives, rifles   | Rival syndicate leader (exo-suit). Assemble laser launcher from multi-mission components             |
| 800+    | Boss Level    | 35+    | The endgame            | special weapons      | City Kingpin. Final multi-phase fight using all prior weapons, items, and tools                      |

## Chapter 1 — The Block

Earn respect fighting street bullies until Marcus "Kicks" Delano notices you.
Step to him, survive his beatdown, then find a weapon (loose brick in the alley)
and steal $20 from Mom's purse to satisfy his demands. Take him down with the
brick to keep the money and rank up into Chapter 2.

**Locations:** Home, Your Block, The Park, The Schoolyard, The Corner Store,
The Alley, The Woods, The Abandoned Lot, The Construction Site.

**Enemies:** Skinny Derek, Big Tommy, Jake the Snake, Marcus "Kicks" Delano (boss).

**NPCs:**
- **Mom** (Home) — family, quest dialogue (the $20).
- **Old Earl** (Your Block) — info NPC, tells you who runs the schoolyard.
- **Kim** (Corner Store) — shopkeeper who fights back (bat, 35% chance, 3-6 dmg).

**Hazards:** Rat bites and rusty nails (alley), tree roots and wasp nests (woods),
broken glass and stray dogs (abandoned lot), loose boards and exposed rebar
(construction site).

## Chapter 2 — The Strip

Beat Marcus and the block opens up to The Strip — a run-down stretch of shops
and parking lots. Tougher greasers roam the area and drop small cash when you
beat them.

**Boss:** Vinnie "Chrome" Lucca, a leather-jacket greaser who guards the
parking lot. You need at least 25 respect to even get his attention. He'll wipe
the floor with you the first time — then scratch his beloved Chevelle on your
face and demand you replace his car stereo.

**Mission flow:**
1. Earn ≥ 25 respect fighting Strip NPCs (Rico Blades, Darnell, Cutter Pete, Tony V).
2. Challenge Vinnie at the parking lot — survive the scripted loss.
3. Buy brass knuckles ($20) at the Head Shop (appears after Vinnie's mission triggers).
4. Pocket the screwdriver off the counter while the shopkeeper's back is turned.
5. Use the screwdriver to steal the car stereo from the boom car.
6. Bring the stereo back to Vinnie, then take him down with brass knuckles.

**Locations:** The Strip, Head Shop, Bodega, Parking Lot, Boom Car.

**Enemies:** Rico Blades, Darnell, Cutter Pete, Tony V, Vinnie (boss).

**NPCs:**
- **Ponytail Guy** (Head Shop) — shopkeeper, sells brass knuckles.
- **Mr. Salazar** (Bodega) — shopkeeper who fights back (bat, 40% chance, 4-8 dmg,
  5% death chance).
- **Loose-Lip Larry** (The Strip) — info NPC, tips about Vinnie and the boom car.

**Hazards:** Sparking neon signs and skateboarders (the strip), oil slicks and
airborne bottles (parking lot).

**Police:** 12% presence per move, 30% arrest chance. Lose 50% cash + 5 respect.

**Shops:**
- **Head Shop** — brass knuckles ($20).
- **Bodega** — energy drink ($5), bag of chips ($2).

## Chapter 3 — The Yard

**Age 16–17.** An industrial rail yard on the wrong side of the tracks. Rusted
boxcars, chain-link fences, and warehouse shadows.

**Boss:** Razor — skinhead gang leader. Straight razor, steel-toed boots, cold eyes.

**Mission flow:**
1. Beat Vinnie — transition cutscene introduces The Yard.
2. Visit the pawn shop: Shifty says the stereo's busted, trades it for a crowbar (+5 dmg).
3. Earn respect fighting yard enemies (Rail Rat, Bolt-Cutter Ben, Grease Monkey, Skinhead Grunt).
4. At 50 respect, challenge Razor at the hangout — survive the scripted loss.
5. Razor demands the electronics crate from the warehouse.
6. Search the warehouse (40% combat encounter while searching).
7. Return the crate to Razor — real boss fight unlocks.
8. Beat Razor with the crowbar.
9. Victory: rank up to Street Thug. Crate loot carries to Ch4.

**Tool persistence:** Old weapons (brass knuckles, crowbar) stay in inventory
when replaced. Tools like the screwdriver persist indefinitely. These are reused
in unconventional ways in later chapters (e.g., pressing a button through a hole,
prying a panel to access wiring).

**Locations:** The Yard (hub), Pawn Shop, Boxcar Row, Loading Dock, Warehouse,
The Hangout (boss arena).

**Enemies:** Rail Rat, Bolt-Cutter Ben, Grease Monkey, Skinhead Grunt, Razor (boss).

**NPCs:**
- **Shifty** (Pawn Shop) — trades busted stereo for crowbar. Fights back (pipe, 25%).
- **Diesel Dave** (The Yard) — retired rail worker, gives crate location & patrol info.
- **Mute Jenny** (Boxcar Row) — trades food for hand-drawn warehouse map.

**Hazards:** Rail spikes and boxcar doors (yard), rusted nails and coupling snaps
(boxcar row), falling pallets (loading dock), chemical fumes and falling chains
(warehouse).

**Police:** 8% presence (railway security calls cops), 25% arrest, 50% cash loss, -5 respect.

## Chapter 4 — The Avenue *(planned)*

**Age 18–19.** A commercial district with alleyways, a dice game, and a
mysterious lab/warehouse at the far end. You're out of school — no safety net.

**Boss:** D-Block — rival gang lieutenant. Scar from ear to chin. He set you up
for the lab job and wants the data for himself.

**Mission flow:**
1. D-Block's runner (Little Chris) delivers the job: infiltrate the lab.
2. The lab has electronic security — can't just walk in.
3. Find Sparks the tinkerer in his basement workshop.
4. Trade Chapter 3's crate components → Sparks builds the hacking device.
5. Barkeep Ray at the dive bar gives intel on guard shift times.
6. Use the device to bypass lab security, retrieve the data drive.
7. Handle lab guards with knife if they intervene.
8. Confront D-Block. Take him down.

**Locations:** The Avenue (hub), Tinkerer's Workshop, Dive Bar, Dice Alley,
D-Block's Corner, The Lab.

**Enemies:** Corner Thug, Dice Game Enforcer, Tweaker, Lab Security Guard,
D-Block (boss).

**NPCs:**
- **Sparks** (Workshop) — builds hacking device from crate components.
- **Barkeep Ray** (Dive Bar) — intel on lab security & guard shifts. Sells drinks.
- **Little Chris** (Avenue) — D-Block's runner, delivers quest triggers.
- **Pawn Shop Jenny** (Avenue) — sells knives. Fights back (shotgun, 45% chance, 10% death).

**Hazards:** Curb-jumping cars and falling bottles (avenue), dirty syringes
(dice alley), UV light bursts and exposed wiring (lab).

**Police:** 15% presence, 35% arrest, 50% cash loss, -8 respect.

## Chapter 5 — The Row *(planned)*

**Age 20–22.** Corner stores, pawn shops, gang hangouts. You're high in the
gang but still a miscreant and a loner. Petty crime isn't sanctioned, but you
gotta do it to afford ammo and survival.

**Boss:** Mr. Fontaine — corrupt store owner with bodyguards and a .38 revolver.

**Store owners fight back.** Corner store clerks and armed shopkeepers will
resist robbery — clerks swing broom handles (35% chance), armed shopkeepers
fire weapons (encounter-based, 8% instant death chance). This is the chapter
where robbery has real consequences.

**Mission flow:**
1. Rob corner stores for cash (unsanctioned, risky — resource management).
2. Buy cheap pistol from Mack at the pawn shop ($50).
3. Rita at the laundromat gives intel on Fontaine's schedule.
4. Old Sarge warns you about armed shopkeepers and foreshadows "go professional."
5. Challenge Fontaine → scripted loss (bodyguards).
6. Case his operation via back office, learn routines, take him down.
7. Completion triggers "go professional" dialogue → unlocks Crew missions.

**Locations:** The Row (hub), Corner Store, Laundromat, Pawn Shop / Arms Contact,
Back Office, Fontaine's Fortified Shop (boss arena).

**Enemies:** Corner Store Clerk, Armed Shopkeeper (8% death chance), Street Hustler,
Bodyguard, Mr. Fontaine (boss).

**NPCs:**
- **Mack** (Pawn Shop) — sells cheap pistol & ammo. Fights back (revolver, 30%, 8% death).
- **Rita** (Laundromat) — intel on Fontaine's safe, bodyguard schedules, police timing.
- **Old Sarge** (The Row) — warnings about armed store owners, foreshadows Ch6 transition.

**Hazards:** Backfiring cars and lunging pit bulls (the row), detergent spills
(laundromat).

**Police:** 18% presence, 40% arrest, 60% cash loss, -10 respect.

## Chapter 6 — The Docks *(planned)*

**Age 25–28.** Warehouses, delivery depots, waterfront docks. You're running
with a crew now — official gang business.

**Boss:** Salvatore "The Fish" Moretti — mob capo. Silver hair, cigar, gold-plated
pistol. Three assassination attempts survived.

**Mission flow:**
1. Nails (crew partner) briefs you on van hijack jobs.
2. Hijack delivery vans at the depot — plan routes, timing, tools.
3. Van contents: cash, weapon parts, special components.
4. Eddie Books assigns multi-step missions: pick up from Fish Monger Sal, deliver elsewhere.
5. Fish Monger Sal gives intel on van schedules and warehouse layout.
6. Earn respect through heists.
7. Challenge the capo → scripted loss → dismantle his supply chain.
8. Confront and beat Moretti. Van loot funds Ch7 gear.

**Locations:** The Docks (hub), Container Yard, Delivery Depot, Fish Market,
The Pier, Capo's Warehouse (boss arena).

**Enemies:** Dock Worker, Smuggler, Van Driver, Capo's Enforcer,
Salvatore "The Fish" Moretti (boss).

**NPCs:**
- **Fish Monger Sal** (Fish Market) — intel on van schedules & warehouse access. Sells supplies.
- **Nails** (Docks) — crew partner for van hijack missions.
- **Eddie Books** (Warehouse) — Moretti's accountant, assigns multi-step deliveries.
- **Officer Ketch** (Docks) — harbour patrol, represents police threat.

**Hazards:** Snapping crane cables and wet dock slips (docks), rogue forklifts
and falling crates (container yard), reversing vans (depot), rotting planks and
wave surges (pier).

**Police:** 15% presence (harbour patrol), 35% arrest, 50% cash loss, -12 respect.

## Chapter 7 — The Heights *(planned)*

**Age 30–35.** Mansions, high-tech warehouses, black-market labs. You discover
the lab items from Ch4 were for something sinister your boss is building.

**Boss:** Viktor Kessler — rival syndicate leader in a robotic exo-suit.
Ex-military, German accent, hydraulic limbs, titanium plating. Without the
laser launcher, you can't scratch him.

**Mission flow:**
1. Ghost (legendary retired thief) reveals the sinister plot at the private club.
2. High-end heist missions: mansions, vaults, black-market labs.
3. Concierge Marco gives guard rotations and elevator codes at the penthouse.
4. Sylvia the art dealer identifies heist targets and buys stolen goods.
5. Challenge Kessler → scripted loss (exo-suit is too strong).
6. Assemble laser launcher from 3 components:
   - **Power Cell** — scavenged from the mansion heist.
   - **Focusing Array** — recovered from the black-market lab.
   - **Control Module** — from the Ch4 lab thread (repurposed).
7. Dr. Chen (disgraced researcher) assembles the weapon.
8. Fight Viktor Kessler on the rooftop with the laser launcher.

**Locations:** The Heights (hub), Private Club, Penthouse Tower, Black-Market Lab,
The Mansion, The Rooftop (boss arena).

**Enemies:** Private Security, Syndicate Soldier, Mansion Guard, Lab Scientist,
Viktor Kessler (boss).

**NPCs:**
- **Ghost** (Private Club) — reveals sinister plot, identifies 3 laser components.
- **Dr. Chen** (Lab) — assembles laser launcher from components.
- **Concierge Marco** (Penthouse) — guard rotations, elevator codes, Kessler's schedule.
- **Sylvia** (Heights) — art dealer, identifies heist targets, fences stolen goods.

**Hazards:** Falling window-washer buckets and cracking glass panels (heights),
snapping elevator cables and slamming security doors (penthouse), chemical
spills and electrical containment arcs (lab), guard dogs and motion-sensor
spotlights (mansion), rooftop wind gusts (rooftop).

**Police:** 20% presence (tactical unit), 40% arrest, 60% cash loss, -15 respect.

## Chapter 8 — The Crown *(planned)*

**Age 35+.** The whole city. Alexander Cross — the Kingpin who's been pulling
strings since Chapter 1 — is finally revealed. Every forward-thread item from
the entire game has a role in the final battle.

**Boss:** Alexander Cross, the City Kingpin. Golden Desert Eagle, detonator,
ceiling-mounted turrets. 250 HP. Multi-phase final fight.

**NPCs return from earlier chapters:**
- **The Prophet** (Old Block) — defected Kingpin insider, gives the dossier.
- **Nails** (Syndicate HQ) — crew partner from Ch6, cuts power on your signal.
- **Sparks** (Bunker) — tinkerer from Ch4, hacks security remotely.
- **Ghost** (HQ) — legendary thief from Ch7, final narrative sendoff.
- **Detective Shaw** (HQ) — honest cop, potential ally or threat (police wild card).

**Mission flow:**
1. Gather final intel from The Prophet on the old block.
2. Assemble final loadout from all accumulated weapons and items.
3. Phase 1: breach the complex (Nails cuts power, explosives, hacking device).
4. Phase 2: fight through elite guards and armoured mercs (rifles, shotgun, SMG).
5. Phase 3: underground bunker — The Ghost Hand (Kingpin's lieutenant). Sparks
   disables cameras and blast doors.
6. Phase 4: face Alexander Cross in his stronghold (laser launcher, all weapons).
7. You run the city — or burn it down trying.

**Locations:** Syndicate HQ (hub), The Old Block, Underground Bunker,
Kingpin's Stronghold (boss arena), The Helipad (climax).

**Enemies:** Elite Guard, Armoured Mercenary, The Ghost Hand (lieutenant),
Alexander Cross — the Kingpin (boss).

**Hazards:** Motion-sensor security doors and gas traps (HQ), automated turrets
and blast door pressure waves and steam pipe bursts (bunker), rotor wash gusts (helipad).

**Police:** 25% presence (SWAT), 45% arrest, 70% cash loss, -20 respect.

## Systems

### Store Owner Fight-Back
Shopkeepers across all chapters can fight back when you try to rob them.
Each has a `fight_back_chance`, damage range, and flavour text. Some (armed
shopkeepers, pawn dealers) have a `death_chance` — a small probability of
instant kill. The risk escalates with each chapter.

### Police
Starting in Chapter 2, police have a per-chapter presence level that determines
how often they appear. Getting caught during criminal activity triggers an
arrest roll — on failure you lose a percentage of your cash and a chunk of
respect. Police escalate from beat cops (Ch2) to SWAT (Ch8).

### Environmental Hazards
Every outdoor (and some indoor) location has a hazard list. Each hazard has a
text description, damage value, and roll chance. Only one hazard triggers per
move. Hazards scale from rat bites and rusty nails (Ch1) to automated turrets
and blast-door pressure waves (Ch8).

---

Features terminal pixel-art scene illustrations (ANSI true-colour).