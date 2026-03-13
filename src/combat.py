"""Turn-based combat system."""
import random
import time

from ui import clear, slow_print, typewriter, choice_menu, divider
from graphics import scene_combat


class CombatResult:
    WIN = "win"
    LOSE = "lose"
    RUN = "run"
    SCRIPTED_LOSS = "scripted_loss"


def run_combat(player, enemy, scripted_loss=False):
    """Run a fight.  Returns a CombatResult constant.

    If *scripted_loss* is True the player cannot actually kill the enemy
    and the fight ends after they land a punch and take a few rounds.
    """
    punched = False
    turn = 0

    while True:
        turn += 1

        # ── draw the combat HUD ────────────────────────────────────
        clear()
        print(scene_combat())
        print()
        divider()
        print(f"  \033[91m⚔  FIGHT: You vs {enemy['name']}  ⚔\033[0m")
        divider()

        bar_p = _hp_bar(player.hp, player.max_hp)
        bar_e = _hp_bar(enemy["hp"], enemy["max_hp"])
        print(f"  You:            [{bar_p}] {player.hp}/{player.max_hp}")
        print(f"  {enemy['name'][:16]:<16}  [{bar_e}] {enemy['hp']}/{enemy['max_hp']}")
        if player.weapon:
            print(f"  Weapon: {player.weapon['name']}")
        print()

        # ── player turn ────────────────────────────────────────────
        actions = player.get_combat_actions()

        # insert usable healing items before "Run Away"
        heal_items = [i for i in player.inventory if i.get("heal")]
        for item in heal_items:
            actions.insert(-1, f"Use {item['name']} (+{item['heal']} HP)")

        print("  Your move:")
        idx = choice_menu(actions)
        action = actions[idx]
        print()

        # -- run away --
        if "Run Away" in action:
            if scripted_loss and not punched:
                slow_print(f"  You try to run but {enemy['name']} blocks your path!")
                slow_print(f"  {enemy['name']}: \"Where you think you're going?\"")
                time.sleep(0.4)
            else:
                if random.random() < 0.65:
                    slow_print("  You bolt and get away!")
                    time.sleep(0.4)
                    return CombatResult.RUN
                else:
                    slow_print(f"  You try to run but {enemy['name']} cuts you off!")
                    time.sleep(0.3)

        # -- use item --
        elif action.startswith("Use "):
            item_name = action.split("Use ")[1].split(" (+")[0]
            used = player.use_item(item_name)
            if used:
                slow_print(f"  You use the {used['name']}. +{used['heal']} HP!")
                time.sleep(0.3)

        # -- attack --
        else:
            damage = player.roll_damage(action)
            if scripted_loss:
                damage = max(1, damage // 2)
                punched = True

            enemy["hp"] -= damage
            verb = random.choice(["connects", "lands", "smacks", "hits"])
            slow_print(f"  You throw a {action.lower()}! "
                       f"It {verb} for {damage} damage!")
            time.sleep(0.3)

            if enemy["hp"] <= 0:
                if scripted_loss:
                    enemy["hp"] = 1
                else:
                    print()
                    typewriter(f"  {enemy['name']} goes down! You win!")
                    player.respect += enemy.get("respect_reward", 5)
                    slow_print(f"  +{enemy.get('respect_reward', 5)} Respect!")
                    time.sleep(0.8)
                    return CombatResult.WIN

        # ── enemy turn ─────────────────────────────────────────────
        time.sleep(0.3)

        # scripted-loss exit: end after player punched and a few rounds
        if scripted_loss and punched and turn >= 3:
            e_dmg = random.randint(enemy["damage_min"], enemy["damage_max"])
            player.take_damage(e_dmg)
            atk = random.choice(enemy.get("attacks", ["hits you"]))
            slow_print(f"  {enemy['name']} {atk} for {e_dmg} damage!")
            time.sleep(0.5)
            enemy["hp"] = enemy["max_hp"]  # reset for later fight
            return CombatResult.SCRIPTED_LOSS

        e_dmg = random.randint(enemy["damage_min"], enemy["damage_max"])
        player.take_damage(e_dmg)
        atk = random.choice(enemy.get("attacks", ["hits you"]))
        slow_print(f"  {enemy['name']} {atk} for {e_dmg} damage!")

        if player.is_dead():
            time.sleep(0.5)
            print()
            typewriter("  Everything goes dark...")
            time.sleep(0.8)
            return CombatResult.LOSE

        time.sleep(0.4)
        input("\n  Press Enter for next round...")


def _hp_bar(cur, mx, width=10):
    filled = max(0, int(width * cur / mx))
    return "█" * filled + "░" * (width - filled)
