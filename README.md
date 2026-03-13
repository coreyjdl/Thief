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

| Respect | Rank          | Age    | Era                    | New Weapons         | New Actions               |
| ------- | ------------- | ------ | ---------------------- | ------------------- | ------------------------- |
| 0–10    | Push-over Kid | 14     | Middle school          | fists → loose brick | run away, basic punch     |
| 10–25   | Fighter       | 15     | High school freshman   | brass knuckles      | take down bullies         |
| 25–50   | Punk          | 16–17  | High school upperclass | chain, pipe         | petty theft               |
| 50–100  | Street Thug   | 18–19  | Just out of school     | bat, crowbar        | shake down NPCs           |
| 100–200 | Grifter       | 20–22  | Early twenties         | knife, cheap pistol | rob corner stores         |
| 200–400 | Crew Member   | 25–28  | Late twenties          | shotgun, SMG        | gang missions, steal vans |
| 400–800 | Syndicate     | 30–35  | Thirties               | explosives, rifles  | high-end heists           |
| 800+    | Boss Level    | 35+    | The endgame            | special weapons     | final challenge           |

## Chapter 1 — The Block

Earn respect fighting street bullies until Marcus "Kicks" Delano notices you.
Step to him, survive his beatdown, then find a weapon (loose brick in the alley)
and steal $20 from Mom's purse to satisfy his demands. Take him down with the
brick to keep the money and rank up into Chapter 2.

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
3. Steal the car stereo from the boom car on your block.
4. Buy brass knuckles ($20) at the Head Shop (appears after Vinnie's mission triggers).
5. Bring the stereo and the knuckles back to Vinnie, then take him down.

**Shops:**
- **Head Shop** — brass knuckles ($20, gated behind Vinnie's mission).
- **Bodega** — energy drink ($3, +10 HP), bag of chips ($1, +3 HP).

Money comes from NPC fights ($1–$8 per win) plus the $20 kept from Chapter 1.

## Chapter 3 — The Yard *(planned)*

**Age 16–17.** An industrial rail yard on the wrong side of the tracks. Rusted
boxcars, chain-link fences, and warehouse shadows.

**Boss:** Skinhead gang leader who controls the yard and its turf.
**Weapons:** Chain, pipe.  **New actions:** Petty theft (boxcars, warehouses).

## Chapter 4 — The Avenue *(planned)*

**Age 18–19.** Pool halls, dive bars, back-alley dice games. You're out of
school now — no safety net.

**Boss:** Rival gang lieutenant who runs a crew on the avenue.
**Weapons:** Bat, crowbar.  **New actions:** Shake down NPCs, collect debts.

## Chapter 5 — The Row *(planned)*

**Age 20–22.** Commercial storefronts hiding dirty money — laundromats, bodegas,
corner stores all washing more than clothes.

**Boss:** Corrupt store owner with bodyguards.
**Weapons:** Knife, cheap pistol (first ranged weapon).  **New actions:** Rob corner stores.

## Chapter 6 — The Docks *(planned)*

**Age 25–28.** Waterfront shipping containers, fishing boats, and crab shacks
hiding serious operations. Organised crime territory.

**Boss:** Local mob capo controlling imports.
**Weapons:** Shotgun, SMG.  **New actions:** Gang missions, steal vans, cargo heists.

## Chapter 7 — The Heights *(planned)*

**Age 30–35.** Glass towers, private clubs, penthouse suites. The player has
climbed from the gutter to the skyline.

**Boss:** City crime boss or rival syndicate leader.
**Weapons:** Explosives, rifles.  **New actions:** High-end heists (banks, galleries).

## Chapter 8 — The Crown *(planned)*

**Age 35+.** The whole city. The mysterious kingpin who's been pulling strings
since Chapter 1 is finally revealed — or a corrupt official with a private army.

**Boss:** The Ultimate Boss — the final confrontation.
**Weapons:** Special / unique weapons earned through the story.

---

Features terminal pixel-art scene illustrations (ANSI true-colour).