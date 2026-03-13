"""Player state — HP, respect, inventory, rank, flags."""
import random

RANKS = [
    (0,   "Push-over Kid"),
    (10,  "Fighter"),
    (25,  "Punk"),
    (50,  "Street Thug"),
    (100, "Grifter"),
    (200, "Crew Member"),
    (400, "Syndicate"),
    (800, "Boss Level"),
]


class Player:
    def __init__(self):
        self.name = "Kid"
        self.hp = 30
        self.max_hp = 30
        self.respect = 0
        self.money = 0
        self.inventory = []
        self.weapon = None              # equipped weapon item (or None)
        self.location = "home"
        self.flags = {}

    # ── rank helpers ────────────────────────────────────────────────
    def get_rank(self):
        rank = RANKS[0][1]
        for threshold, name in RANKS:
            if self.respect >= threshold:
                rank = name
        return rank

    def get_rank_index(self):
        idx = 0
        for i, (threshold, _) in enumerate(RANKS):
            if self.respect >= threshold:
                idx = i
        return idx

    # ── HP ──────────────────────────────────────────────────────────
    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
        return self.hp <= 0

    def is_dead(self):
        return self.hp <= 0

    # ── inventory ───────────────────────────────────────────────────
    def has_item(self, item_name):
        return any(i["name"] == item_name for i in self.inventory)

    def add_item(self, item):
        # auto-equip weapons if better than current
        if item.get("type") == "weapon":
            cur_bonus = self.weapon.get("damage_bonus", 0) if self.weapon else 0
            if item.get("damage_bonus", 0) > cur_bonus:
                self.weapon = item
                return
        self.inventory.append(item)

    def remove_item(self, item_name):
        self.inventory = [i for i in self.inventory if i["name"] != item_name]

    def use_item(self, item_name):
        for item in self.inventory:
            if item["name"] == item_name:
                if item.get("heal"):
                    self.heal(item["heal"])
                self.inventory.remove(item)
                return item
        return None

    # ── flags (story state) ─────────────────────────────────────────
    def set_flag(self, flag, value=True):
        self.flags[flag] = value

    def get_flag(self, flag, default=False):
        return self.flags.get(flag, default)

    # ── combat helpers ──────────────────────────────────────────────
    def get_combat_actions(self):
        actions = ["Weak Punch"]
        if self.get_rank_index() >= 1:
            actions.append("Strong Punch")
        actions.append("Run Away")
        return actions

    def roll_damage(self, action):
        bonus = self.weapon.get("damage_bonus", 0) if self.weapon else 0
        if action == "Weak Punch":
            return random.randint(2, 5) + bonus
        if action == "Strong Punch":
            return random.randint(4, 8) + bonus
        return 0
