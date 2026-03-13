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

| Respect | Rank          | New Weapons              | New Actions               |
| ------- | ------------- | ------------------------ | ------------------------- |
| 0–10    | Push-over Kid | fists → loose brick      | run away, basic punch     |
| 10–25   | Fighter       | brick → brass knuckles   | take down bullies         |
| 25–50   | Punk          | chain, pipe              | petty theft               |
| 50–100  | Street Thug   | crowbar                  | shake down NPCs           |
| 100–200 | Grifter       | knife, cheap pistol      | rob corner stores         |
| 200–400 | Crew Member   | shotgun, SMG             | gang missions, steal vans |
| 400–800 | Syndicate     | explosives, rifles       | high-end heists           |
| 800+    | Boss Level    | special weapons          | final challenge available |

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

---

Features terminal pixel-art scene illustrations (ANSI true-colour).