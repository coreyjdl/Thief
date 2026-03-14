"""Main game loop, story events, and state management."""
import copy
import random
import time

from ui import (clear, typewriter, slow_print, narrate, divider,
                header, pause, choice_menu, status_bar, dialogue)
from graphics import SCENES, scene_title, scene_combat
from player import Player
from combat import run_combat, CombatResult
from worlds import (LOCATIONS, ITEMS, fresh_enemy, roll_loot,
                    loc_key_by_name, ENCOUNTER_INTROS, AMBIENT, AMBIENT_CH2,
                    CHAPTER_AMBIENT)


class Game:
    def __init__(self):
        self.player = Player()
        self.running = True
        self.ground_loot = []          # items lying around in current location
        self.turn = 0

    # ════════════════════════════════════════════════════════════════
    #  TOP-LEVEL FLOW
    # ════════════════════════════════════════════════════════════════
    def run(self):
        self.title_screen()
        self.intro()
        self.game_loop()

    def title_screen(self):
        clear()
        print(scene_title())
        print()
        header("T H I E F")
        print()
        slow_print("          A game about climbing from nothing.")
        print()
        divider()
        print()
        name = input("  What's your name, kid?  >>> ").strip()
        if name:
            self.player.name = name
        pause()

    def intro(self):
        clear()
        print(SCENES["home"]())
        print()
        divider()
        narrate(f"Another morning. Same cracked ceiling, same peeling walls.")
        time.sleep(0.3)
        narrate(f"You're {self.player.name}. Fourteen, small for your age,")
        narrate("and at the bottom of every food chain that matters.")
        time.sleep(0.3)
        narrate("")
        narrate("The block's got a pecking order. Always has.")
        narrate("And right now you're somewhere below the pigeons.")
        time.sleep(0.5)
        narrate("")
        narrate("But today's gonna be different.")
        narrate("Today you're going outside.")
        pause()

    # ════════════════════════════════════════════════════════════════
    #  MAIN GAME LOOP
    # ════════════════════════════════════════════════════════════════
    def game_loop(self):
        while self.running:
            self.turn += 1
            self._show_location()
            self._process_turn()

            if self.player.is_dead():
                self._game_over()
                return

    # ── display ─────────────────────────────────────────────────────
    def _show_location(self):
        clear()
        loc = LOCATIONS[self.player.location]

        scene_fn = SCENES.get(loc["scene"])
        if scene_fn:
            print(scene_fn())

        print()
        header(loc["name"])
        print()
        slow_print(f"  {loc['desc']}")
        print()

        # ambient flavour
        if not loc.get("interior") and random.random() < 0.30:
            ch = loc.get("chapter", 1)
            pool = CHAPTER_AMBIENT.get(ch, AMBIENT)
            print(f"  {random.choice(pool)}")
            print()

        # ground loot callout
        if self.ground_loot:
            for item in self.ground_loot:
                print(f"  You spot a {item['name']} on the ground.")
            print()

        status_bar(self.player)
        divider()

    # ── action menu ─────────────────────────────────────────────────
    def _build_actions(self):
        loc = LOCATIONS[self.player.location]
        actions = []

        # navigation — filter out chapter-gated locations
        for conn in loc["connections"]:
            dest = LOCATIONS[conn]
            chapter = dest.get("chapter", 1)
            if chapter >= 2 and not self.player.get_flag("beat_marcus"):
                continue
            if chapter >= 3 and not self.player.get_flag("beat_vinnie"):
                continue
            actions.append(f"Go to {dest['name']}")

        # dynamic connection: your_block → the_strip after Ch1
        if self.player.location == "your_block" and \
           self.player.get_flag("beat_marcus") and \
           "the_strip" not in loc["connections"]:
            actions.append(f"Go to {LOCATIONS['the_strip']['name']}")

        # dynamic connection: the_strip → the_yard after Ch2
        if self.player.location == "the_strip" and \
           self.player.get_flag("beat_vinnie") and \
           "the_yard" not in loc["connections"]:
            actions.append(f"Go to {LOCATIONS['the_yard']['name']}")

        # location-specific
        if self.player.location == "home":
            if self.player.get_flag("marcus_demands_money") and \
               not self.player.get_flag("stole_money"):
                actions.append("Take money from Mom's purse")
            elif not self.player.get_flag("marcus_demands_money"):
                actions.append("Look at Mom's purse")
            actions.append("Rest (heal to full)")

        # shop
        if loc.get("shop"):
            actions.append("Browse shop")

        # boom car stereo theft — need screwdriver to pop it out
        if self.player.location == "boom_car" and \
           self.player.get_flag("vinnie_demands_stereo") and \
           not self.player.has_item("Car Stereo") and \
           self.player.has_item("Screwdriver"):
            actions.append("Steal the car stereo")

        # pawn shop stereo trade
        if self.player.location == "pawn_shop" and \
           self.player.has_item("Car Stereo") and \
           not self.player.has_item("Crowbar"):
            actions.append("Trade the stereo")

        # warehouse crate search
        if self.player.location == "warehouse" and \
           self.player.get_flag("razor_demands_crate") and \
           not self.player.has_item("Electronics Crate"):
            actions.append("Search for the crate")

        # ground loot
        for item in self.ground_loot:
            actions.append(f"Pick up {item['name']}")

        # inventory
        if self.player.inventory or self.player.weapon:
            actions.append("Check inventory")

        actions.append("Look around")
        return actions

    def _process_turn(self):
        actions = self._build_actions()
        print("\n  What do you do?")
        idx = choice_menu(actions)
        action = actions[idx]
        print()

        if action.startswith("Go to "):
            self._move(action[6:])
        elif action == "Take money from Mom's purse":
            self._steal_money()
        elif action == "Look at Mom's purse":
            self._look_purse()
        elif action == "Rest (heal to full)":
            self._rest()
        elif action.startswith("Pick up "):
            self._pick_up(action[8:])
        elif action == "Check inventory":
            self._inventory()
        elif action == "Look around":
            self._look_around()
        elif action == "Browse shop":
            self._shop()
        elif action == "Steal the car stereo":
            self._steal_stereo()
        elif action == "Trade the stereo":
            self._trade_stereo()
        elif action == "Search for the crate":
            self._search_crate()

    # ════════════════════════════════════════════════════════════════
    #  MOVEMENT
    # ════════════════════════════════════════════════════════════════
    def _move(self, dest_name):
        dest = loc_key_by_name(dest_name)
        if not dest:
            slow_print("  You can't go there.")
            pause()
            return

        slow_print(f"  You head to {dest_name}...")
        time.sleep(0.4)
        self.player.location = dest

        # roll for loot
        self.ground_loot = roll_loot(dest)

        # weapons only appear after the mission starts
        if not self.player.get_flag("punched_marcus"):
            self.ground_loot = [i for i in self.ground_loot
                                if i.get("type") != "weapon"]

        # guarantee the brick spawns in the alley after the Marcus fight
        if (dest == "alley"
                and self.player.get_flag("punched_marcus")
                and not self.player.get_flag("brick_placed")
                and not self.player.weapon):
            brick = copy.deepcopy(ITEMS["loose_brick"])
            if not any(i["name"] == brick["name"] for i in self.ground_loot):
                self.ground_loot.append(brick)
            self.player.set_flag("brick_placed")

        # ── Chapter 1 story triggers ────────────────────────────────
        if dest == "schoolyard":
            if not self.player.get_flag("met_marcus"):
                if self.player.respect < 10:
                    self._marcus_brushoff()
                else:
                    self._marcus_intro()
                return
            if self.player.get_flag("marcus_demands_money"):
                if self.player.has_item("Mom's $20"):
                    self._marcus_pay()
                    return
                else:
                    self._marcus_waiting()
                    return

        # ── boom car hint (no screwdriver yet) ──────────────────────
        if dest == "boom_car" and \
           self.player.get_flag("vinnie_demands_stereo") and \
           not self.player.has_item("Car Stereo") and \
           not self.player.has_item("Screwdriver"):
            narrate("The stereo's bolted in with Phillips screws.")
            narrate("You'd need a screwdriver to get it out.")
            time.sleep(0.3)

        # ── Chapter 3 story triggers ────────────────────────────────
        if dest == "skinhead_hangout":
            if not self.player.get_flag("met_razor"):
                if self.player.respect < 50:
                    self._razor_brushoff()
                else:
                    self._razor_intro()
                return
            if self.player.get_flag("razor_demands_crate"):
                if self.player.has_item("Electronics Crate"):
                    self._razor_pay()
                    return
                else:
                    self._razor_waiting()
                    return

        # ── Chapter 2 story triggers ────────────────────────────────
        if dest == "parking_lot":
            if not self.player.get_flag("met_vinnie"):
                if self.player.respect < 25:
                    self._vinnie_brushoff()
                else:
                    self._vinnie_intro()
                return
            if self.player.get_flag("vinnie_demands_stereo"):
                if self.player.has_item("Car Stereo"):
                    self._vinnie_pay()
                    return
                else:
                    self._vinnie_waiting()
                    return

        # ── random encounter ────────────────────────────────────────
        loc = LOCATIONS[dest]
        if not loc.get("interior") and loc["encounter_chance"] > 0:
            if random.random() < loc["encounter_chance"]:
                self._random_encounter()
                return

        # ── environmental hazard ────────────────────────────────────
        self._roll_hazard()

    def _roll_hazard(self):
        """Roll for a minor environmental hazard at the current location."""
        loc = LOCATIONS[self.player.location]
        for hazard in loc.get("hazards", []):
            if random.random() < hazard["chance"]:
                print()
                slow_print(f"  {hazard['text']}")
                self.player.hp = max(1, self.player.hp - hazard["damage"])
                slow_print(f"  You lose {hazard['damage']} HP.")
                pause()
                return  # only one hazard per move

    # ════════════════════════════════════════════════════════════════
    #  RANDOM COMBAT ENCOUNTERS
    # ════════════════════════════════════════════════════════════════
    def _random_encounter(self):
        loc = LOCATIONS[self.player.location]
        pool = loc.get("enemies", [])
        if not pool:
            return

        enemy = fresh_enemy(random.choice(pool))
        print()
        slow_print(f"  {random.choice(ENCOUNTER_INTROS)}")
        time.sleep(0.4)
        slow_print(f"  It's {enemy['name']}!")
        slow_print(f"  {enemy['desc']}")
        print()
        dialogue(enemy["name"], enemy["taunt"])
        print()

        opts = ["Fight!", "Try to run"]
        c = choice_menu(opts)

        if c == 1:  # run
            if random.random() < 0.60:
                slow_print("  You bolt! Your legs carry you to safety.")
                pause()
                return
            else:
                slow_print("  You try to run but they cut you off!")
                time.sleep(0.4)

        result = run_combat(self.player, enemy)
        self._handle_combat_result(result, enemy)

    # chapter-appropriate healing drops (keyed by chapter number)
    _DROP_TABLE = {
        1: ["soda_can", "candy_bar"],
        2: ["energy_drink", "chips"],
        3: ["beef_jerky", "cheap_bandage"],
        4: ["malt_liquor", "first_aid_kit"],
        5: ["pain_pills", "protein_bar"],
        6: ["canned_food", "field_medkit"],
        7: ["energy_bar_pro", "trauma_kit"],
        8: ["combat_stim"],
    }

    def _current_chapter(self):
        """Return the chapter number for the player's current location."""
        loc = LOCATIONS.get(self.player.location, {})
        return loc.get("chapter", 1)

    def _handle_combat_result(self, result, enemy):
        if result == CombatResult.WIN:
            slow_print(f"  {enemy.get('defeat_text', 'They go down.')}")
            # money drop
            money_drop = enemy.get("money_drop")
            if money_drop:
                cash = random.randint(money_drop[0], money_drop[1])
                if cash > 0:
                    self.player.money += cash
                    slow_print(f"  You find ${cash} in their pockets!")
            # item drop — chapter-appropriate healing items
            if random.random() < 0.45:
                ch = self._current_chapter()
                pool = self._DROP_TABLE.get(ch, self._DROP_TABLE[1])
                drop_id = random.choice(pool)
                drop = ITEMS[drop_id].copy()
                self.player.add_item(drop)
                slow_print(f"  You find a {drop['name']}!")
            pause()
        elif result == CombatResult.LOSE:
            self._game_over()
        elif result == CombatResult.RUN:
            slow_print("  You escaped!")
            pause()

    # ════════════════════════════════════════════════════════════════
    #  MARCUS — STORY BEATS
    # ════════════════════════════════════════════════════════════════
    def _marcus_brushoff(self):
        """Player goes to schoolyard before earning enough respect."""
        clear()
        print(SCENES["schoolyard"]())
        print()
        divider()

        narrate("You step through the gap in the fence into the schoolyard.")
        time.sleep(0.3)
        narrate("A big kid is leaning against the basketball pole,")
        narrate("flanked by two others. He glances your way.")
        time.sleep(0.5)
        print()

        dialogue("Big Kid", "Who are you?", "91")
        time.sleep(0.3)
        narrate("He looks you up and down and turns back to his boys.")
        narrate("You're nobody to him. Not even worth shoving.")
        time.sleep(0.3)
        print()
        narrate("Maybe if you had some kind of reputation he'd notice you.")
        narrate("You should go earn some respect on the block first.")
        self.player.location = "park"
        pause()

    def _marcus_intro(self):
        """First encounter with Marcus 'Kicks' Delano.

        The player sees Marcus and can choose to approach and fight him.
        Attempting to fight is what triggers the story mission.
        """
        clear()
        print(SCENES["schoolyard"]())
        print()
        divider()

        narrate("You step through the gap in the fence into the schoolyard.")
        time.sleep(0.3)
        narrate("The concrete stretches out, empty except for one figure")
        narrate("leaning against the basketball pole.")
        time.sleep(0.5)
        print()
        narrate("He's big. Sixteen at least, with a crew-cut and a letterman")
        narrate("jacket two sizes too large. His sneakers are the whitest")
        narrate("things on the whole block — fresh Jordans, untouched.")
        time.sleep(0.5)
        print()
        narrate("Two other kids linger behind him like shadows with attitude.")
        time.sleep(0.3)

        self.player.set_flag("met_marcus")

        print()
        opts = ["Step to him", "Leave quietly"]
        c = choice_menu(opts)

        if c == 1:  # leave
            narrate("You back through the gap in the fence before anyone notices.")
            narrate("Probably smart. That kid looks like he eats freshmen.")
            self.player.location = "park"
            pause()
            return

        # Player chose to fight — this triggers the mission
        narrate("You walk across the concrete toward him.")
        narrate("Your heart is hammering but your feet keep moving.")
        time.sleep(0.3)
        print()

        dialogue("Marcus", "Well well. Look who wandered onto my court.", "91")
        time.sleep(0.5)
        narrate("He pushes off the pole and sizes you up.")
        time.sleep(0.3)

        dialogue("Marcus",
                 "You from down the block right? The quiet one. "
                 "See everybody on this block pays respect. "
                 "And I don't see you paying.", "91")
        time.sleep(0.5)
        print()

        dialogue(self.player.name, "I ain't paying you nothing.", "92")
        time.sleep(0.3)

        narrate("Marcus steps up close, towering over you.")
        dialogue("Marcus",
                 "Oh you got a mouth. Alright. "
                 "Let's see if those hands work too.", "91")
        time.sleep(0.5)
        print()

        pause("  Press Enter to fight...")
        marcus = fresh_enemy("marcus")
        result = run_combat(self.player, marcus, scripted_loss=True)

        if result == CombatResult.SCRIPTED_LOSS:
            self.player.set_flag("punched_marcus")
            print()
            divider()

            narrate("Marcus stands over you, barely winded. But then he")
            narrate("looks down at his feet.")
            time.sleep(0.5)
            print()
            narrate("There's a scuff on his left Jordan. A black mark running")
            narrate("right across the white toe.")
            time.sleep(0.5)
            print()
            dialogue("Marcus", "...", "91")
            time.sleep(0.5)
            dialogue("Marcus", "You scuffed. My. JORDANS.", "91")
            time.sleep(0.8)
            pause()
            print()
            narrate("His face twists from smug to furious.")
            time.sleep(0.3)
            dialogue("Marcus",
                     "Those are two-hundred-dollar shoes. You owe me "
                     "twenty bucks. TOMORROW.", "91")
            time.sleep(0.5)
            dialogue("Marcus",
                     "You don't pay? I'll take it out of your face. "
                     "Every. Single. Day.", "91")
            time.sleep(0.5)
            pause()
            print()
            narrate("Marcus and his crew walk off, leaving you on the ground.")
            narrate("Your lip is bleeding but something's different.")
            narrate("You actually fought back.")

            self.player.set_flag("marcus_demands_money")
            if self.player.hp < 5:
                self.player.hp = 5
            pause()

        elif result == CombatResult.RUN:
            narrate("You get away but you can hear Marcus laughing.")
            narrate("That didn't go how you planned. But it's not over.")
            self.player.set_flag("met_marcus")
            self.player.set_flag("punched_marcus")
            self.player.set_flag("marcus_demands_money")
            if self.player.hp < 5:
                self.player.hp = 5
            pause()

    def _marcus_waiting(self):
        print()
        dialogue("Marcus", "You got my money?", "91")
        dialogue(self.player.name, "Not yet...", "92")
        dialogue("Marcus", "Clock's ticking.", "91")
        print()
        narrate("Better find that money. Maybe check at home...")
        pause()

    def _marcus_pay(self):
        """Hand over the $20 — triggers the real fight."""
        clear()
        print(SCENES["schoolyard"]())
        print()
        divider()

        narrate("Marcus is leaning against the basketball pole, picking at his")
        narrate("nails like he owns the whole schoolyard. Because basically he does.")
        time.sleep(0.3)
        print()
        dialogue("Marcus", "Ah there you are. Got my money?", "91")
        time.sleep(0.3)

        print("  You hold out the crumpled twenty.")
        time.sleep(0.5)

        narrate("Marcus snatches it, looks at it, stuffs it in his pocket.")
        time.sleep(0.3)
        print()
        dialogue("Marcus", "Good dog.", "91")
        time.sleep(0.5)

        narrate("He shoves you hard. You stumble but don't fall.")
        time.sleep(0.3)
        narrate("Something snaps inside you.")
        time.sleep(0.5)
        print()

        dialogue(self.player.name, "I'm not your dog.", "92")
        time.sleep(0.5)
        dialogue("Marcus", "What did you just say to me?", "91")
        time.sleep(0.3)

        narrate("You see it on his face — he's not used to pushback.")
        narrate("His boys look uncertain. Nobody talks to Kicks like that.")
        time.sleep(0.5)
        print()

        dialogue(self.player.name,
                 "I said I'm not your dog. And you owe me twenty bucks.", "92")
        time.sleep(0.8)
        print()

        narrate("Marcus's grin fades. His fists clench.")
        dialogue("Marcus", "I'm gonna put you in the ground.", "91")
        time.sleep(0.5)

        self.player.remove_item("Mom's $20")
        self.player.money -= 20

        # heal player up for the real fight
        self.player.hp = max(self.player.hp, self.player.max_hp - 5)

        print()

        # check if player has the brick — needed to win
        has_weapon = self.player.weapon is not None

        if not has_weapon:
            narrate("You ball your fists but deep down you know bare knuckles")
            narrate("aren't gonna cut it against someone his size.")
            narrate("You need to find something to even the odds.")
            pause()
            # give the money back — fight doesn't happen yet
            self.player.add_item(ITEMS["moms_money"].copy())
            self.player.money += 20
            narrate("Marcus shoves you back through the fence.")
            dialogue("Marcus", "Come back when you're serious.", "91")
            pause()
            return

        pause("  This is it. Press Enter to fight for real...")

        marcus = fresh_enemy("marcus")
        marcus["max_hp"] = 35
        marcus["hp"] = 35
        marcus["damage_min"] = 3
        marcus["damage_max"] = 5

        result = run_combat(self.player, marcus)

        if result == CombatResult.WIN:
            # player gets the $20 back — keeps it into next chapter
            self.player.add_item(ITEMS["moms_money"].copy())
            self.player.money += 20
            self._win_chapter_one()
        elif result == CombatResult.LOSE:
            # merciful: don't end the game, let them retry
            slow_print("  You're knocked down... but not out.")
            self.player.hp = 10
            narrate("Marcus walks away thinking he won.")
            narrate("But you're getting back up. You'll find him again.")
            self.player.add_item(ITEMS["moms_money"].copy())
            self.player.money += 20
            pause()
        elif result == CombatResult.RUN:
            slow_print("  You run but this isn't over. Marcus still has your money.")
            narrate("Go back to the schoolyard when you're ready.")
            self.player.add_item(ITEMS["moms_money"].copy())
            self.player.money += 20
            self.player.set_flag("ran_from_marcus_fight")
            pause()

    def _win_chapter_one(self):
        """Victory over Marcus — chapter 1 complete."""
        clear()
        print(SCENES["schoolyard"]())
        print()
        divider()
        print()

        narrate("Marcus is on the ground. His precious Jordans are scuffed")
        narrate("to hell and his jacket's torn. He looks up at you with")
        narrate("something you've never seen on his face before.")
        time.sleep(0.5)
        narrate("")
        narrate("Fear.")
        time.sleep(0.8)
        print()

        narrate("The other kids who were watching — and there are always kids")
        narrate("watching — they're staring. Whispering.")
        time.sleep(0.3)
        narrate("")
        narrate(f"You just did what nobody thought was possible.")
        narrate(f"You beat Marcus 'Kicks' Delano.")
        time.sleep(0.5)
        narrate("")
        narrate("He scrambles up and limps away without looking back.")
        narrate("His boys follow but they glance at you over their shoulders.")
        narrate("Not with hate. With respect.")
        time.sleep(0.5)

        self.player.respect += 15
        self.player.set_flag("beat_marcus")

        print()
        header("R A N K   U P !")
        print()
        slow_print(f"  You are now: {self.player.get_rank()}")
        slow_print(f"  Respect: {self.player.respect}")
        print()
        divider()
        narrate("")
        narrate("Word travels fast on the block.")
        narrate("By tomorrow everyone's gonna know your name.")
        narrate(f"\"{self.player.name}\" — the kid who knocked out Kicks.")
        time.sleep(0.5)
        narrate("")
        narrate("This is just the beginning.")
        print()
        header("E N D   O F   C H A P T E R   1")
        print()
        slow_print("  New rank unlocked:  FIGHTER")
        slow_print("  New action:         Strong Punch")
        print()
        divider()
        pause()

        # ── transition to Chapter 2 ────────────────────────────────
        self._chapter_two_intro()

    # ════════════════════════════════════════════════════════════════
    #  CHAPTER 2 — THE STRIP
    # ════════════════════════════════════════════════════════════════
    def _chapter_two_intro(self):
        """Transition cutscene from Chapter 1 to Chapter 2."""
        clear()
        print(SCENES["the_strip"]())
        print()
        header("C H A P T E R   2  —  T H E   S T R I P")
        print()

        narrate("A few days pass. The bruises fade but the reputation doesn't.")
        time.sleep(0.3)
        narrate("Kids on the block step aside when you walk by now.")
        narrate("Even Marcus's old crew gives you a nod.")
        time.sleep(0.5)
        print()
        narrate("But the block's getting small. You've been hearing about")
        narrate("a stretch of shops and lots a few streets over — The Strip.")
        time.sleep(0.3)
        narrate("Older kids hang there. Tougher. The kind who don't")
        narrate("care that you beat up some high school bully.")
        time.sleep(0.5)
        print()
        narrate("Word is some greaser named Vinnie 'Chrome' Lucca runs things.")
        narrate("Got a cherry-red Chevelle he treats like a throne.")
        narrate("Nobody touches that car. Nobody.")
        time.sleep(0.3)
        print()
        narrate("Time to see what's out there.")
        pause()

        self.player.location = "your_block"
        self.player.hp = self.player.max_hp

        # bump up max HP for tougher chapter
        self.player.max_hp = 40
        self.player.hp = self.player.max_hp

    # ── Vinnie story beats ──────────────────────────────────────────
    def _vinnie_brushoff(self):
        """Player goes to parking lot before earning enough respect."""
        clear()
        print(SCENES["parking_lot"]())
        print()
        divider()

        narrate("You walk into the parking lot. A guy in a leather jacket")
        narrate("is leaning against a cherry-red Chevelle, polishing")
        narrate("the hood with a rag.")
        time.sleep(0.3)
        print()
        narrate("He doesn't even look up.")
        time.sleep(0.3)

        dialogue("Vinnie", "Get lost, kid.", "91")
        time.sleep(0.3)
        narrate("He flicks the rag at you dismissively.")
        narrate("You're nobody out here. Not yet.")
        print()
        narrate("Maybe if you had more of a reputation on the Strip...")
        self.player.location = "the_strip"
        pause()

    def _vinnie_intro(self):
        """Player has enough respect — Vinnie confrontation."""
        clear()
        print(SCENES["parking_lot"]())
        print()
        divider()

        narrate("You walk into the parking lot. The Chevelle gleams under")
        narrate("the streetlight like a jewel. Vinnie leans against the")
        narrate("driver's door, cigarette dangling from his lip.")
        time.sleep(0.5)
        print()
        narrate("This time he looks up.")
        time.sleep(0.3)

        dialogue("Vinnie",
                 "I know you. You're that kid who dropped Kicks "
                 "over on Cedar Street.", "91")
        time.sleep(0.5)

        narrate("He takes a long drag and flicks ash on the ground.")
        time.sleep(0.3)

        dialogue("Vinnie",
                 "Beating up high schoolers don't mean nothing over here. "
                 "This is adult territory.", "91")
        time.sleep(0.5)

        self.player.set_flag("met_vinnie")
        print()
        opts = ["Step to him", "Walk away"]
        c = choice_menu(opts)

        if c == 1:
            narrate("You back off. He's bigger than Marcus by a lot.")
            narrate("Probably smart to earn some more respect first.")
            self.player.location = "the_strip"
            pause()
            return

        # Player chose to fight
        narrate("You walk right up to the Chevelle.")
        time.sleep(0.3)

        dialogue(self.player.name, "I'm not a kid.", "92")
        time.sleep(0.3)

        narrate("Vinnie pushes off the car, flicks his cigarette away.")
        narrate("He's got six inches and fifty pounds on you easy.")
        time.sleep(0.3)

        dialogue("Vinnie",
                 "Yeah? Then you won't mind if I teach you "
                 "some manners.", "91")
        time.sleep(0.5)
        print()

        pause("  Press Enter to fight...")
        vinnie = fresh_enemy("vinnie")
        result = run_combat(self.player, vinnie, scripted_loss=True)

        if result == CombatResult.SCRIPTED_LOSS:
            self.player.set_flag("punched_vinnie")
            print()
            divider()

            narrate("Vinnie barely broke a sweat. But as you hit the ground")
            narrate("your shoe scraped against the Chevelle's quarter panel.")
            time.sleep(0.5)
            print()
            narrate("A long white scratch runs right down the cherry-red paint.")
            time.sleep(0.5)
            print()
            dialogue("Vinnie", "...", "91")
            time.sleep(0.5)
            dialogue("Vinnie", "You scratched my car.", "91")
            time.sleep(0.8)
            pause()
            print()

            narrate("His jaw tightens. For a second you think he's going to")
            narrate("kill you. But then he takes a breath.")
            time.sleep(0.3)

            dialogue("Vinnie",
                     "That paint job cost more than your house. You're "
                     "gonna pay for it. You know that Buick on the block "
                     "with the big speakers? Bring me the stereo.", "91")
            time.sleep(0.5)
            dialogue("Vinnie",
                     "Don't come back without it. Or I come find you.", "91")
            time.sleep(0.5)
            pause()
            print()
            narrate("Vinnie turns back to his car, running a finger over")
            narrate("the scratch. You can tell he's holding back rage.")
            narrate("Better find that car stereo.")

            self.player.set_flag("vinnie_demands_stereo")
            if self.player.hp < 5:
                self.player.hp = 5
            pause()

        elif result == CombatResult.RUN:
            narrate("You get away but Vinnie's laughter follows you.")
            narrate("That scratch on his car isn't going anywhere.")
            self.player.set_flag("met_vinnie")
            self.player.set_flag("punched_vinnie")
            self.player.set_flag("vinnie_demands_stereo")
            if self.player.hp < 5:
                self.player.hp = 5
            pause()

    def _vinnie_waiting(self):
        print()
        dialogue("Vinnie", "Where's my stereo?", "91")
        dialogue(self.player.name, "Still looking...", "92")
        dialogue("Vinnie",
                 "The Buick on the block. Big speakers. Rip it out. "
                 "Don't make me ask again.", "91")
        print()
        narrate("Better find that boom car and get the stereo.")
        pause()

    def _vinnie_pay(self):
        """Hand over the car stereo — triggers the real fight."""
        clear()
        print(SCENES["parking_lot"]())
        print()
        divider()

        narrate("Vinnie is buffing out the scratch on his Chevelle")
        narrate("with a rag and a look of pure hatred.")
        time.sleep(0.3)
        print()
        dialogue("Vinnie", "You got it?", "91")
        time.sleep(0.3)

        narrate("You hold up the JVC head unit, wires dangling.")
        time.sleep(0.5)

        narrate("Vinnie snatches it, turns it over, nods.")
        time.sleep(0.3)
        print()
        dialogue("Vinnie", "Not bad. Maybe you're useful after all.", "91")
        time.sleep(0.5)

        narrate("He tosses the stereo onto his passenger seat")
        narrate("and turns back to you.")
        time.sleep(0.3)

        dialogue("Vinnie", "Now get out of my lot.", "91")
        time.sleep(0.3)

        dialogue(self.player.name, "No.", "92")
        time.sleep(0.5)

        dialogue("Vinnie", "Excuse me?", "91")
        time.sleep(0.3)

        dialogue(self.player.name,
                 "I did your errand. Now I want your respect.", "92")
        time.sleep(0.5)

        narrate("Vinnie stares at you. Then he starts laughing.")
        time.sleep(0.3)
        dialogue("Vinnie",
                 "Respect? You want RESPECT?", "91")
        time.sleep(0.5)
        narrate("His laughter dies. His eyes go cold.")
        dialogue("Vinnie", "Earn it.", "91")
        time.sleep(0.5)

        self.player.remove_item("Car Stereo")

        # heal player up for the real fight
        self.player.hp = max(self.player.hp, self.player.max_hp - 5)

        print()

        # check if player has brass knuckles — needed to win
        has_knuckles = (self.player.weapon is not None and
                        self.player.weapon.get("damage_bonus", 0) >= 3)

        if not has_knuckles:
            narrate("You look at your fists. A brick worked on Marcus")
            narrate("but this guy's built different. You need something")
            narrate("heavier. Something metal.")
            narrate("Maybe the Head Shop on the Strip has what you need.")
            pause()
            # give stereo back — fight doesn't happen yet
            self.player.add_item(ITEMS["car_stereo"].copy())
            narrate("Vinnie shoves the stereo back at you.")
            dialogue("Vinnie", "Come back when you're ready to go.", "91")
            pause()
            return

        pause("  Time to finish this. Press Enter to fight for real...")

        vinnie = fresh_enemy("vinnie")
        vinnie["max_hp"] = 45
        vinnie["hp"] = 45
        vinnie["damage_min"] = 4
        vinnie["damage_max"] = 7

        result = run_combat(self.player, vinnie)

        if result == CombatResult.WIN:
            self._win_chapter_two()
        elif result == CombatResult.LOSE:
            slow_print("  You're on the pavement... but you'll be back.")
            self.player.hp = 10
            narrate("Vinnie walks away thinking he won.")
            narrate("But you're not done. Find him at the parking lot.")
            self.player.add_item(ITEMS["car_stereo"].copy())
            pause()
        elif result == CombatResult.RUN:
            slow_print("  You run. No shame — just strategy.")
            narrate("Go back to the parking lot when you're ready.")
            self.player.add_item(ITEMS["car_stereo"].copy())
            self.player.set_flag("ran_from_vinnie_fight")
            pause()

    def _win_chapter_two(self):
        """Victory over Vinnie — chapter 2 complete."""
        clear()
        print(SCENES["parking_lot"]())
        print()
        divider()
        print()

        narrate("Vinnie is on his knees next to his Chevelle,")
        narrate("blood on his leather jacket, hair finally out of place.")
        narrate("He looks up at you with something new in his eyes.")
        time.sleep(0.5)
        narrate("")
        narrate("Disbelief.")
        time.sleep(0.8)
        print()

        narrate("The older kids who were watching from the Strip")
        narrate("are dead silent. Then someone starts a slow clap.")
        time.sleep(0.3)
        narrate("")
        narrate(f"You just did what nobody on the Strip thought possible.")
        narrate(f"You beat Vinnie 'Chrome' Lucca.")
        time.sleep(0.5)
        narrate("")
        narrate("He pulls himself up using his car door.")
        narrate("Looks at the scratch. Looks at you.")
        time.sleep(0.3)

        dialogue("Vinnie", "...Not bad, kid. Not bad at all.", "91")
        time.sleep(0.5)
        narrate("He limps away. His boys follow at a distance.")
        time.sleep(0.5)

        # keep the stereo — player already handed it over
        self.player.respect += 20
        self.player.set_flag("beat_vinnie")

        print()
        header("R A N K   U P !")
        print()
        slow_print(f"  You are now: {self.player.get_rank()}")
        slow_print(f"  Respect: {self.player.respect}")
        print()
        divider()
        narrate("")
        narrate("The Strip knows your name now.")
        narrate("The block was just the beginning.")
        narrate(f"\"{self.player.name}\" — the kid who dropped Chrome.")
        time.sleep(0.5)
        narrate("")
        narrate("You're moving up. And there's no going back.")
        print()
        header("E N D   O F   C H A P T E R   2")
        print()
        slow_print("  New rank unlocked:  PUNK")
        pause()

        # ── transition to Chapter 3 ────────────────────────────────
        self._chapter_three_intro()

    # ════════════════════════════════════════════════════════════════
    #  CHAPTER 3 — THE YARD
    # ════════════════════════════════════════════════════════════════
    def _chapter_three_intro(self):
        """Transition cutscene from Chapter 2 to Chapter 3."""
        clear()
        print(SCENES["the_yard"]())
        print()
        header("C H A P T E R   3  —  T H E   Y A R D")
        print()

        narrate("A week goes by. Vinnie's crew avoids you on the Strip.")
        time.sleep(0.3)
        narrate("You're fifteen going on sixteen and you've already outgrown")
        narrate("two neighbourhoods.")
        time.sleep(0.5)
        print()
        narrate("Past the last bus stop on Linden Ave, the pavement turns")
        narrate("to gravel and the streetlights stop. The old rail yard")
        narrate("sprawls like a rusted skeleton — boxcars, loading docks,")
        narrate("chain-link topped with razor wire.")
        time.sleep(0.3)
        print()
        narrate("They say a skinhead crew runs things out here. Their")
        narrate("leader goes by Razor. Carries a straight blade in his")
        narrate("boot. Nobody messes with him.")
        time.sleep(0.5)
        print()
        narrate("There's a pawn shop on the edge of the yard. Guy named")
        narrate("Shifty runs it. Might be interested in that car stereo")
        narrate("you've been carrying around.")
        time.sleep(0.3)
        print()
        narrate("Time to see what the yard's about.")
        pause()

        self.player.location = "the_strip"

        # bump up max HP for tougher chapter
        self.player.max_hp = 55
        self.player.hp = self.player.max_hp

    # ── Razor story beats ───────────────────────────────────────────
    def _razor_brushoff(self):
        """Player goes to the hangout before earning enough respect."""
        clear()
        print(SCENES["skinhead_hangout"]())
        print()
        divider()

        narrate("You walk up to the gutted office trailer. A steel drum")
        narrate("fire crackles out front. Two skinheads sit on crates,")
        narrate("watching you with flat eyes.")
        time.sleep(0.3)
        print()

        dialogue("Skinhead", "Who the hell are you?", "91")
        time.sleep(0.3)

        narrate("One of them stands up. He's got four inches on you.")
        time.sleep(0.3)

        dialogue("Skinhead",
                 "Nobody comes back here. Walk away before we make "
                 "you crawl away.", "91")
        time.sleep(0.3)

        narrate("You're not ready for this. Not yet.")
        self.player.location = "loading_dock"
        pause()

    def _razor_intro(self):
        """Player has enough respect — Razor confrontation."""
        clear()
        print(SCENES["skinhead_hangout"]())
        print()
        divider()

        narrate("You push past the grunts at the fire and walk up to")
        narrate("the trailer door. It swings open before you knock.")
        time.sleep(0.5)
        print()
        narrate("A tall, lean figure steps out. Shaved head. Cold eyes.")
        narrate("A straight razor glints in his boot strap.")
        time.sleep(0.3)

        dialogue("Razor",
                 "I know who you are. You're the kid who dropped "
                 "Chrome over on the Strip.", "91")
        time.sleep(0.5)

        narrate("He tilts his head like he's sizing up a stray dog.")
        time.sleep(0.3)

        dialogue("Razor",
                 "Doesn't mean anything out here. This yard is "
                 "mine. Every rail, every crate, every bolt.", "91")
        time.sleep(0.5)

        self.player.set_flag("met_razor")
        print()
        opts = ["Step to him", "Walk away"]
        c = choice_menu(opts)

        if c == 1:
            narrate("Smart. He's got crew everywhere.")
            narrate("Come back when you've got more weight to throw around.")
            self.player.location = "loading_dock"
            pause()
            return

        # Player chose to fight
        narrate("You step up to the trailer steps.")
        time.sleep(0.3)

        dialogue(self.player.name, "I didn't come here to look around.", "92")
        time.sleep(0.3)

        narrate("Razor pulls the blade from his boot strap. Slow.")
        narrate("Casual. Like he's done it a thousand times.")
        time.sleep(0.3)

        dialogue("Razor",
                 "Then let me teach you what this yard does to "
                 "trespassers.", "91")
        time.sleep(0.5)
        print()

        pause("  Press Enter to fight...")
        razor = fresh_enemy("skinhead_boss")
        result = run_combat(self.player, razor, scripted_loss=True)

        if result == CombatResult.SCRIPTED_LOSS:
            self.player.set_flag("punched_razor")
            print()
            divider()

            narrate("Razor barely broke a sweat. You're on your back in")
            narrate("the gravel, tasting blood. His crew laughs from the")
            narrate("fire barrel.")
            time.sleep(0.5)
            print()
            narrate("But Razor doesn't walk away. He crouches down.")
            time.sleep(0.3)

            dialogue("Razor",
                     "You got guts, kid. Stupid guts. Tell you what.", "91")
            time.sleep(0.5)

            narrate("He points toward the far end of the yard — past")
            narrate("the boxcars, toward the old warehouse.")
            time.sleep(0.3)

            dialogue("Razor",
                     "There's an electronics crate in that warehouse. "
                     "Circuit boards, wiring, components. I need it. "
                     "Bring it to me and maybe I'll let you walk this "
                     "yard without my boys jumping you every five "
                     "minutes.", "91")
            time.sleep(0.5)
            dialogue("Razor",
                     "Don't come back without it.", "91")
            time.sleep(0.5)
            pause()
            print()

            narrate("Razor disappears into the trailer. His boys go back")
            narrate("to their fire. You're alone with a busted lip and a")
            narrate("mission.")

            self.player.set_flag("razor_demands_crate")
            self.player.hp = 10
            self.player.location = "loading_dock"
            pause()

    def _razor_waiting(self):
        """Player returns to hangout without the crate."""
        clear()
        print(SCENES["skinhead_hangout"]())
        print()
        divider()

        narrate("The grunts at the fire barrel block your path.")
        time.sleep(0.3)
        dialogue("Skinhead",
                 "Razor said don't come back without the crate. "
                 "Try the warehouse.", "91")
        time.sleep(0.3)
        self.player.location = "loading_dock"
        pause()

    def _razor_pay(self):
        """Player returns with the electronics crate — real fight."""
        clear()
        print(SCENES["skinhead_hangout"]())
        print()
        divider()

        narrate("You drop the heavy crate at Razor's feet.")
        narrate("He crouches, pops the latch, and rifles through it.")
        time.sleep(0.5)
        print()

        dialogue("Razor",
                 "Circuit boards. Wiring harnesses. Yeah, this "
                 "is the one.", "91")
        time.sleep(0.3)

        narrate("He stands and looks at you. Not impressed exactly.")
        narrate("More like reconsidering.")
        time.sleep(0.3)

        dialogue("Razor",
                 "You did the job. I'll give you that.", "91")
        time.sleep(0.5)

        self.player.remove_item("Electronics Crate")
        print()

        dialogue(self.player.name,
                 "We done here? Or you got something else to say?",
                 "92")
        time.sleep(0.5)

        narrate("Razor's jaw tightens. He glances at his crew.")
        narrate("Then back at you.")
        time.sleep(0.3)

        dialogue("Razor",
                 "Yeah. I got one more thing.", "91")
        time.sleep(0.3)

        narrate("He pulls the razor from his boot.")
        time.sleep(0.5)

        dialogue("Razor",
                 "Nobody does a job for me and walks away even. "
                 "That's not how this yard works.", "91")
        time.sleep(0.5)
        print()

        pause("  Press Enter to fight...")

        razor = fresh_enemy("skinhead_boss")
        # weaken him slightly — you did earn it
        razor["damage_min"] = 5
        razor["damage_max"] = 8

        result = run_combat(self.player, razor)

        if result == CombatResult.WIN:
            self._win_chapter_three()
        elif result == CombatResult.LOSE:
            slow_print("  You're face-down in the gravel... but not finished.")
            self.player.hp = 10
            narrate("Razor walks away. But you'll be back.")
            narrate("Find him at the hangout.")
            pause()
        elif result == CombatResult.RUN:
            slow_print("  You run. No shame — just strategy.")
            narrate("Go back to the hangout when you're ready.")
            pause()

    def _win_chapter_three(self):
        """Victory over Razor — chapter 3 complete."""
        clear()
        print(SCENES["skinhead_hangout"]())
        print()
        divider()
        print()

        narrate("Razor hits the gravel. The straight blade skids away")
        narrate("under a rail car. His crew stares, frozen.")
        time.sleep(0.5)
        narrate("")
        narrate("Nobody moves.")
        time.sleep(0.8)
        print()

        narrate("Razor spits blood and pulls himself up against the")
        narrate("trailer wall. He looks at you with something cold")
        narrate("and grudging.")
        time.sleep(0.5)

        dialogue("Razor",
                 "...This ain't over.", "91")
        time.sleep(0.3)

        narrate("But it is.")
        time.sleep(0.5)
        print()

        narrate("The grunts at the fire barrel look at each other.")
        narrate("One by one they walk away, leaving Razor alone.")
        narrate("The yard just changed hands.")
        time.sleep(0.5)

        self.player.respect += 20
        self.player.set_flag("beat_razor")

        print()
        header("R A N K   U P !")
        print()
        slow_print(f"  You are now: {self.player.get_rank()}")
        slow_print(f"  Respect: {self.player.respect}")
        print()
        divider()
        narrate("")
        narrate("Word spreads through the rail yard by nightfall.")
        narrate("The kid who dropped Chrome just dropped Razor too.")
        narrate(f"\"{self.player.name}\" — the name people whisper")
        narrate("when they hear gravel crunch behind them.")
        time.sleep(0.5)
        narrate("")
        narrate("The yard's yours. But the city keeps going.")
        print()
        header("E N D   O F   C H A P T E R   3")
        print()
        slow_print("  New rank unlocked:  STREET THUG")
        slow_print("  Coming soon:        The Avenue, bigger scores...")
        print()
        divider()
        print()
        slow_print("  Thanks for playing the demo!")
        slow_print("  More chapters coming soon...")
        print()

        self.running = False
        pause("  Press Enter to exit...")

    def _trade_stereo(self):
        """Trade the car stereo for a crowbar at the pawn shop."""
        clear()
        print(SCENES["pawn_shop"]())
        print()
        divider()

        narrate("Shifty peers at the car stereo through smudged glasses,")
        narrate("turning it over in his hands.")
        time.sleep(0.5)
        print()

        dialogue("Shifty",
                 "JVC head unit. Aftermarket. Wires are yanked "
                 "though — hard to resell.", "93")
        time.sleep(0.3)

        narrate("He sets it on the counter and scratches his chin.")
        time.sleep(0.3)

        dialogue("Shifty",
                 "Tell you what. I got a crowbar in back that's "
                 "worth more than this. But I'll trade you straight "
                 "up. Deal?", "93")
        time.sleep(0.5)
        print()

        opts = ["Take the deal", "Keep the stereo"]
        c = choice_menu(opts)

        if c == 0:
            self.player.remove_item("Car Stereo")
            self.player.add_item(ITEMS["crowbar"].copy())
            self.player.set_flag("traded_stereo")

            narrate("Shifty slides the crowbar across the counter.")
            narrate("Cold steel with a comfortable curve.")
            time.sleep(0.3)
            print()
            slow_print("  [Traded: Car Stereo → Crowbar]")
            if self.player.weapon and \
               self.player.weapon.get("name") == "Crowbar":
                slow_print("  [Equipped: Crowbar (+5 damage)]")
            pause()
        else:
            narrate("\"Suit yourself,\" Shifty shrugs.")
            pause()

    def _search_crate(self):
        """Search the warehouse for the electronics crate."""
        clear()
        print(SCENES["warehouse"]())
        print()
        divider()

        narrate("The warehouse is massive — rows of crates stacked")
        narrate("to the ceiling, dusty light cutting through high")
        narrate("windows. You move through the shadows, checking")
        narrate("labels.")
        time.sleep(0.5)
        print()

        # random encounter chance during the search
        if random.random() < 0.40:
            narrate("A skinhead grunt rounds the corner and spots you.")
            time.sleep(0.3)
            enemy = fresh_enemy("skinhead_grunt")
            dialogue(enemy["name"], enemy["taunt"])
            print()
            result = run_combat(self.player, enemy)
            self._handle_combat_result(result, enemy)
            if self.player.hp <= 0:
                return
            print()
            narrate("You keep searching...")
            time.sleep(0.3)

        narrate("Behind a stack of pallets you find it — a metal crate")
        narrate("with 'ELEC COMPONENTS' stenciled on the side.")
        time.sleep(0.3)
        narrate("It's heavy but you can carry it.")
        time.sleep(0.3)
        print()

        self.player.add_item(ITEMS["crate_loot"].copy())
        slow_print("  [Obtained: Electronics Crate]")
        slow_print("  [Bring it to Razor at the hangout.]")
        pause()

    # ════════════════════════════════════════════════════════════════
    #  SHOP SYSTEM
    # ════════════════════════════════════════════════════════════════
    def _shop(self):
        loc = LOCATIONS[self.player.location]
        shop = loc.get("shop", {})
        if not shop:
            slow_print("  Nothing to buy here.")
            pause()
            return

        # filter items based on story state
        available = {}
        for item_id, price in shop.items():
            # brass knuckles only appear after Vinnie's mission starts
            if item_id == "brass_knuckles" and \
               not self.player.get_flag("vinnie_demands_stereo"):
                continue
            # crowbar is trade-only (handled by _trade_stereo)
            if item_id == "crowbar":
                continue
            available[item_id] = price

        if not available:
            narrate("The guy behind the counter eyes you.")
            dialogue("Shopkeeper",
                     "Nothing here for you right now. Come back later.", "93")
            pause()
            return

        print(f"  ┌──────────────────────────────┐")
        print(f"  │           SHOP                │")
        print(f"  ├──────────────────────────────┤")
        opts = []
        item_ids = []
        for item_id, price in available.items():
            item = ITEMS[item_id]
            label = f"{item['name']} (${price})"
            print(f"  │  {label:<28}│")
            opts.append(f"Buy {item['name']} (${price})")
            item_ids.append((item_id, price))
        print(f"  │                              │")
        print(f"  │  Your cash: ${self.player.money:<17}│")
        print(f"  └──────────────────────────────┘")

        opts.append("Leave")
        print()
        c = choice_menu(opts)

        if c < len(item_ids):
            iid, price = item_ids[c]
            if self.player.money < price:
                slow_print("  You don't have enough cash.")
                pause()
                return
            self.player.money -= price
            bought = ITEMS[iid].copy()
            is_weapon = bought.get("type") == "weapon"
            self.player.add_item(bought)
            slow_print(f"  You buy the {bought['name']}.")
            if bought.get("desc"):
                slow_print(f"  {bought['desc']}")
            if is_weapon and self.player.weapon == bought:
                slow_print(f"  [Equipped: {bought['name']}"
                           f" (+{bought['damage_bonus']} damage)]")

            # Steal screwdriver off the counter when buying knuckles
            if iid == "brass_knuckles" and \
               self.player.location == "head_shop" and \
               not self.player.has_item("Screwdriver"):
                print()
                time.sleep(0.3)
                narrate("As the guy turns to put your cash in the register,")
                narrate("you notice a flathead screwdriver sitting on the")
                narrate("counter. You palm it before he turns back around.")
                self.player.add_item(ITEMS["screwdriver"].copy())
                slow_print("  [Obtained: Screwdriver]")

            pause()
        else:
            pause()

    # ════════════════════════════════════════════════════════════════
    #  STEAL STEREO
    # ════════════════════════════════════════════════════════════════
    def _steal_stereo(self):
        clear()
        print(SCENES["boom_car"]())
        print()
        divider()

        narrate("The Buick sits on its blocks, speakers still thumping.")
        narrate("Nobody's around. The bass covers any noise you'd make.")
        time.sleep(0.3)
        print()

        opts = ["Rip out the stereo", "Leave it alone"]
        c = choice_menu(opts)

        if c == 0:
            narrate("You pop the door open — it wasn't even locked.")
            time.sleep(0.3)
            narrate("The head unit's aftermarket. Four Phillips screws")
            narrate("hold it in. Good thing you pocketed that screwdriver.")
            time.sleep(0.3)
            narrate("Four turns each and the unit slides right out.")
            narrate("The speakers go dead. The block suddenly feels quieter.")
            time.sleep(0.3)
            print()

            self.player.add_item(ITEMS["car_stereo"].copy())
            self.player.set_flag("stole_stereo")

            slow_print("  [Obtained: Car Stereo]")
            slow_print("  [Now bring it to Vinnie at the parking lot.]")
            pause()
        else:
            narrate("Not yet. But Vinnie's deadline weighs on you.")
            pause()

    # ════════════════════════════════════════════════════════════════
    #  BASIC ACTIONS
    # ════════════════════════════════════════════════════════════════
    def _steal_money(self):
        clear()
        print(SCENES["home"]())
        print()
        divider()

        narrate("You look at Mom's purse sitting on the table.")
        narrate("She's in the other room watching her stories.")
        time.sleep(0.3)
        print()

        opts = ["Take the money", "Leave it alone"]
        c = choice_menu(opts)

        if c == 0:
            narrate("Your hands shake as you open the clasp.")
            time.sleep(0.3)
            narrate("A twenty, a few singles, some change.")
            narrate("You take the twenty and close the purse.")
            time.sleep(0.3)
            print()
            narrate("Your stomach knots up. She works doubles for this money.")
            narrate("But Marcus wasn't bluffing and you know it.")

            self.player.add_item(ITEMS["moms_money"].copy())
            self.player.set_flag("stole_money")
            self.player.money += 20

            print()
            slow_print("  [Obtained: Mom's $20]")
            slow_print("  [First crime committed. No turning back now.]")
            pause()
        else:
            narrate("You pull your hand back. Not yet.")
            narrate("But Marcus's deadline is ticking.")
            pause()

    def _look_purse(self):
        narrate("Mom's purse sits on the table. Worn leather, stuffed with")
        narrate("receipts and grocery lists. She keeps cash in there.")
        narrate("You've got no reason to take it. Yet.")
        pause()

    def _rest(self):
        narrate("You crash on the couch and close your eyes.")
        narrate("The TV plays reruns of something you don't care about.")
        time.sleep(0.5)
        self.player.hp = self.player.max_hp
        slow_print(f"  HP fully restored to {self.player.max_hp}/{self.player.max_hp}!")
        pause()

    def _pick_up(self, item_name):
        for item in self.ground_loot:
            if item["name"] == item_name:
                is_weapon = item.get("type") == "weapon"
                old_weapon = self.player.weapon
                self.player.add_item(item)
                self.ground_loot.remove(item)
                slow_print(f"  You grab the {item['name']}.")
                if item.get("desc"):
                    slow_print(f"  {item['desc']}")
                if is_weapon and self.player.weapon == item:
                    slow_print(f"  [Equipped: {item['name']} (+{item['damage_bonus']} damage)]")
                pause()
                return
        slow_print("  Nothing to pick up.")
        pause()

    def _inventory(self):
        print("  ┌──────────────────────────────┐")
        print("  │         INVENTORY             │")
        print("  ├──────────────────────────────┤")
        if self.player.weapon:
            wname = self.player.weapon['name']
            print(f"  │  ⚔ {wname:<26}│")
        if self.player.inventory:
            for item in self.player.inventory:
                heal = f" (+{item['heal']} HP)" if item.get("heal") else ""
                label = f"{item['name']}{heal}"
                print(f"  │  • {label:<26}│")
        elif not self.player.weapon:
            print("  │  (empty)                    │")
        print(f"  │  Cash: ${self.player.money:<21}│")
        print("  └──────────────────────────────┘")

        # offer to use healing items
        usable = [i for i in self.player.inventory if i.get("heal")]
        if usable and self.player.hp < self.player.max_hp:
            print()
            print("  Use an item?")
            opts = [f"Use {i['name']} (+{i['heal']} HP)" for i in usable]
            opts.append("Close")
            c = choice_menu(opts)
            if c < len(usable):
                used = usable[c]
                self.player.use_item(used["name"])
                slow_print(f"  You use the {used['name']}. +{used['heal']} HP!")
        else:
            pause()

    def _look_around(self):
        loc_id = self.player.location
        flavour = {
            "home": (
                "Your house. Thin walls, old carpet, the smell of whatever "
                "Mom cooked last night. It's not much but it's yours."
            ),
            "your_block": (
                "Same old block. Mr. Henderson's car hasn't moved in two years. "
                "The Ortiz kids are playing in their yard. You can head to the "
                "park, the corner store, or cut through the alley."
            ),
            "park": (
                "The swing set squeaks in the breeze. One chain is broken. "
                "The bench has initials carved into every surface. "
                "Through the trees you can see the schoolyard."
            ),
            "schoolyard": (
                "Marcus's territory."
                if not self.player.get_flag("beat_marcus") else
                "The schoolyard feels different now. Quieter."
            ),
            "corner_store": (
                "The corner store's barred windows glow fluorescent. "
                "A hand-written sign says 'NO LOITERING.' There's an overturned "
                "milk crate someone uses as a chair."
            ),
            "alley": (
                "It stinks like garbage and rain. The dumpster lid is half open. "
                "The walls are covered in old tags. Not a place to linger."
            ),
            "the_strip": (
                "Neon signs buzz. A few shops are still open — a bodega, "
                "some sketchy place called Dragon Claw Emporium. "
                "The parking lot behind the strip is where the real "
                "action is."
            ),
            "head_shop": (
                "Fake swords, throwing stars, incense, and a counter full "
                "of stuff that's definitely not for decoration. The guy "
                "with the ponytail watches you like a hawk."
            ),
            "bodega": (
                "Narrow aisles crammed with chips, drinks, and canned stuff. "
                "The cooler hums. The owner taps a bat behind the counter "
                "whenever someone reaches for something too fast."
            ),
            "parking_lot": (
                "Vinnie's territory."
                if not self.player.get_flag("beat_vinnie") else
                "The lot feels emptier without Vinnie holding court."
            ),
            "boom_car": (
                "An old Buick on cinder blocks. The speakers in the back "
                "are massive — the bass carries for blocks. "
                + ("The stereo's been ripped out. It's quiet now."
                   if self.player.get_flag("stole_stereo") else
                   "The JVC head unit glows behind the dusty windshield.")
            ),
            "the_yard": (
                "Rusted tracks stretch in every direction. Chain-link "
                "fencing topped with razor wire. The air smells like "
                "diesel and old metal. Not a place to wander alone."
            ),
            "pawn_shop": (
                "Grimy storefront packed with other people's stuff. "
                "Guitars, power tools, jewelry. Shifty watches you "
                "from behind the counter."
            ),
            "boxcar_row": (
                "A line of old freight cars on a dead-end siding. "
                "Some are rusted shut, others pried open. Rats "
                "scurry inside. Skinheads stash things here."
            ),
            "loading_dock": (
                "A concrete platform with jammed roller doors. "
                "Pallets stacked high. A dead forklift sits "
                "abandoned. Deals happen here on neutral ground."
            ),
            "warehouse": (
                "A cavernous metal building full of crates and "
                "shadows. High windows let in dusty light. "
                + ("The electronics crate is gone — you already "
                   "grabbed it."
                   if self.player.has_item("Electronics Crate") or
                   self.player.get_flag("beat_razor") else
                   "Somewhere in here is the crate Razor wants.")
            ),
            "skinhead_hangout": (
                "Razor's territory."
                if not self.player.get_flag("beat_razor") else
                "The hangout's quieter now. Razor's crew scattered."
            ),
        }
        narrate(flavour.get(loc_id, "Nothing special."))
        pause()

    # ════════════════════════════════════════════════════════════════
    #  GAME OVER
    # ════════════════════════════════════════════════════════════════
    def _game_over(self):
        clear()
        print()
        print()
        header("G A M E   O V E R")
        print()
        narrate("You wake up on the concrete, head pounding.")
        narrate("Someone took whatever you had in your pockets.")
        narrate("The block doesn't care about your story.")
        print()
        opts = ["Try again", "Quit"]
        c = choice_menu(opts)
        if c == 0:
            self.player.hp = self.player.max_hp
            self.player.location = "home"
            self.ground_loot = []
            self.game_loop()
        else:
            self.running = False
