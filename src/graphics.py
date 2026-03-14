"""Scene graphics — terminal pixel art using ANSI true-color + half-block characters.

Each scene function returns a rendered string that can be printed directly.
Scenes are 56 chars wide × ~11 terminal rows (22 pixel rows via ▀ half-blocks).
"""
import random

# ── colour palette ──────────────────────────────────────────────────────────
SKY         = (110, 160, 220)
SKY_LIGHT   = (155, 195, 240)
CLOUD       = (230, 235, 245)
SUN         = (255, 230, 80)

GRASS       = (55, 135, 45)
GRASS_DARK  = (40, 105, 30)
DIRT        = (130, 85, 40)

BRICK       = (155, 60, 50)
BRICK_DARK  = (115, 42, 32)
BRICK_BROWN = (135, 85, 45)
BRICK_TAN   = (185, 155, 110)
CONCRETE    = (155, 155, 150)
ASPHALT     = (50, 50, 55)
SIDEWALK    = (175, 170, 160)
WINDOW_LIT  = (255, 235, 140)
WINDOW_DARK = (55, 55, 85)
DOOR        = (85, 52, 22)
ROOF        = (55, 50, 45)
ROOF_TILE   = (140, 70, 40)

WALL        = (225, 210, 180)
FLOOR_WOOD  = (150, 105, 55)
COUCH       = (70, 90, 55)
TABLE       = (115, 70, 35)
PURSE       = (140, 35, 50)

METAL       = (130, 130, 140)
DUMPSTER    = (45, 85, 45)
FENCE       = (125, 125, 125)
AWNING      = (175, 35, 25)
AWNING_W    = (235, 225, 210)
HOOP        = (210, 125, 35)
NEON        = (45, 240, 45)
POLE        = (90, 90, 95)
BACKBOARD   = (200, 200, 200)

BLACK       = (0, 0, 0)
WHITE       = (245, 245, 245)
YELLOW      = (245, 210, 45)
YELLOW_LINE = (230, 200, 50)

CURTAIN     = (140, 55, 45)
TV_SCREEN   = (80, 120, 160)

TREE_TRUNK  = (95, 60, 28)
TREE_GREEN  = (30, 115, 25)
TREE_DARK   = (20, 85, 18)
BENCH_WOOD  = (120, 75, 35)
SWING_POST  = (110, 110, 115)
SWING_CHAIN = (150, 150, 140)
SWING_SEAT  = (100, 60, 30)
PUDDLE      = (50, 60, 80)


# ── canvas engine ───────────────────────────────────────────────────────────
class Canvas:
    """A tiny pixel-art canvas rendered via ANSI half-blocks."""

    def __init__(self, width, height, bg):
        self.w = width
        self.h = height
        self.px = [[bg] * width for _ in range(height)]

    # primitives
    def rect(self, x, y, w, h, c):
        for dy in range(h):
            for dx in range(w):
                self._put(x + dx, y + dy, c)

    def circle(self, cx, cy, r, c):
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                if dx * dx + dy * dy <= r * r:
                    self._put(cx + dx, cy + dy, c)

    def oval(self, cx, cy, rx, ry, c):
        for dy in range(-ry, ry + 1):
            for dx in range(-rx, rx + 1):
                if (dx * dx) / max(rx * rx, 1) + (dy * dy) / max(ry * ry, 1) <= 1:
                    self._put(cx + dx, cy + dy, c)

    def tri_up(self, x, y, w, h, c):
        """Upward-pointing triangle (roofs)."""
        for dy in range(h):
            frac = dy / max(h - 1, 1)
            hw = int((w / 2) * frac)
            cx = x + w // 2
            for dx in range(cx - hw, cx + hw + 1):
                self._put(dx, y + dy, c)

    def line_h(self, x, y, length, c):
        for dx in range(length):
            self._put(x + dx, y, c)

    def line_v(self, x, y, length, c):
        for dy in range(length):
            self._put(x, y + dy, c)

    def gradient_v(self, x, y, w, h, c_top, c_bot):
        for dy in range(h):
            t = dy / max(h - 1, 1)
            r = int(c_top[0] + (c_bot[0] - c_top[0]) * t)
            g = int(c_top[1] + (c_bot[1] - c_top[1]) * t)
            b = int(c_top[2] + (c_bot[2] - c_top[2]) * t)
            for dx in range(w):
                self._put(x + dx, y + dy, (r, g, b))

    def _put(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[y][x] = c

    # rendering
    def render(self):
        lines = []
        h = self.h if self.h % 2 == 0 else self.h - 1
        for row in range(0, h, 2):
            buf = []
            for col in range(self.w):
                top = self.px[row][col]
                bot = self.px[row + 1][col] if row + 1 < self.h else BLACK
                if top == bot:
                    buf.append(f"\033[48;2;{top[0]};{top[1]};{top[2]}m ")
                else:
                    buf.append(
                        f"\033[38;2;{top[0]};{top[1]};{top[2]};"
                        f"48;2;{bot[0]};{bot[1]};{bot[2]}m▀"
                    )
            buf.append("\033[0m")
            lines.append("".join(buf))
        return "\n".join(lines)


# ── helper painters ─────────────────────────────────────────────────────────
def _house(c, x, y, w, h, brick, roof):
    rh = h // 3
    c.tri_up(x, y, w, rh, roof)
    c.rect(x, y + rh, w, h - rh, brick)
    dw, dh = max(w // 5, 2), (h - rh) // 2
    c.rect(x + w // 2 - dw // 2, y + h - dh, dw, dh, DOOR)
    ww, wh = max(w // 6, 2), max((h - rh) // 4, 2)
    wy = y + rh + 2
    c.rect(x + 2, wy, ww, wh, WINDOW_LIT)
    c.rect(x + w - 2 - ww, wy, ww, wh, WINDOW_LIT)


def _tree(c, x, y, trunk_h=5, cr=4):
    c.rect(x - 1, y, 2, trunk_h, TREE_TRUNK)
    c.circle(x, y - cr + 1, cr, TREE_GREEN)
    c.circle(x - 1, y - cr, cr - 1, TREE_DARK)


# ── scene functions ─────────────────────────────────────────────────────────
def scene_title():
    c = Canvas(56, 22, BLACK)
    bldgs = [
        (2, 8, 6, 14), (9, 5, 5, 17), (15, 10, 7, 12),
        (23, 3, 4, 19), (28, 7, 8, 15), (37, 11, 5, 11),
        (43, 6, 7, 16), (51, 9, 5, 13),
    ]
    for bx, by, bw, bh in bldgs:
        c.rect(bx, by, bw, bh, (30, 30, 40))
        for wy in range(by + 1, by + bh - 1, 3):
            for wx in range(bx + 1, bx + bw - 1, 3):
                if random.random() > 0.4:
                    c._put(wx, wy, WINDOW_LIT)
    c.circle(48, 3, 2, (220, 220, 200))
    c.rect(0, 20, 56, 2, ASPHALT)
    for sx in range(5, 50, 10):
        c.line_h(sx, 21, 4, YELLOW_LINE)
    return c.render()


def scene_your_block():
    c = Canvas(56, 22, SKY)
    c.oval(12, 2, 5, 2, CLOUD)
    c.oval(38, 3, 4, 1, CLOUD)
    c.circle(50, 3, 2, SUN)
    _house(c, 2, 6, 12, 12, BRICK, ROOF)
    _house(c, 16, 7, 11, 11, BRICK_BROWN, ROOF_TILE)
    _house(c, 29, 6, 12, 12, BRICK_TAN, ROOF)
    _house(c, 43, 7, 11, 11, BRICK_DARK, ROOF_TILE)
    c.rect(0, 18, 56, 2, SIDEWALK)
    c.rect(0, 20, 56, 2, ASPHALT)
    for sx in range(4, 50, 10):
        c.line_h(sx, 21, 3, YELLOW_LINE)
    return c.render()


def scene_home():
    c = Canvas(56, 22, WALL)
    c.rect(0, 0, 56, 3, (180, 165, 140))
    # window
    c.rect(36, 4, 14, 10, SKY_LIGHT)
    c.rect(36, 4, 14, 1, CURTAIN)
    c.rect(36, 5, 2, 9, CURTAIN)
    c.rect(48, 5, 2, 9, CURTAIN)
    c.line_v(43, 4, 10, METAL)
    # couch
    c.rect(4, 13, 16, 5, COUCH)
    c.rect(4, 13, 16, 2, (60, 80, 50))
    c.rect(4, 13, 2, 5, (55, 75, 45))
    c.rect(18, 13, 2, 5, (55, 75, 45))
    # table + purse
    c.rect(24, 14, 8, 2, TABLE)
    c.rect(25, 16, 1, 2, TABLE)
    c.rect(30, 16, 1, 2, TABLE)
    c.rect(26, 13, 4, 1, PURSE)
    c.rect(27, 12, 2, 1, PURSE)
    # TV
    c.rect(6, 10, 8, 3, (80, 60, 35))
    c.rect(7, 8, 6, 3, TV_SCREEN)
    # floor
    c.rect(0, 18, 56, 4, FLOOR_WOOD)
    c.line_h(0, 19, 56, (135, 95, 50))
    c.line_h(0, 21, 56, (135, 95, 50))
    return c.render()


def scene_park():
    c = Canvas(56, 22, SKY)
    c.oval(20, 2, 6, 2, CLOUD)
    c.oval(42, 1, 4, 1, CLOUD)
    _tree(c, 6, 10, 5, 4)
    _tree(c, 48, 9, 6, 5)
    # bench
    c.rect(20, 14, 12, 1, BENCH_WOOD)
    c.rect(20, 15, 1, 2, METAL)
    c.rect(31, 15, 1, 2, METAL)
    c.rect(20, 12, 1, 3, METAL)
    c.rect(31, 12, 1, 3, METAL)
    c.rect(20, 12, 12, 1, BENCH_WOOD)
    # swing set
    c.line_v(37, 6, 11, SWING_POST)
    c.line_v(44, 6, 11, SWING_POST)
    c.line_h(37, 6, 8, SWING_POST)
    c.line_v(39, 7, 7, SWING_CHAIN)
    c.rect(38, 14, 3, 1, SWING_SEAT)
    c.line_v(42, 7, 3, SWING_CHAIN)
    # ground
    c.rect(0, 17, 56, 5, GRASS)
    c.rect(14, 18, 8, 4, DIRT)
    c.rect(12, 19, 12, 3, DIRT)
    return c.render()


def scene_schoolyard():
    c = Canvas(56, 22, SKY)
    # school building
    c.rect(5, 3, 46, 10, BRICK)
    c.rect(5, 2, 46, 1, ROOF)
    for wx in range(8, 48, 6):
        c.rect(wx, 5, 4, 4, WINDOW_DARK)
        c.line_v(wx + 2, 5, 4, METAL)
        c.line_h(wx, 7, 4, METAL)
    c.rect(24, 7, 8, 6, DOOR)
    c.rect(28, 7, 1, 6, (70, 42, 18))
    c._put(26, 10, YELLOW)
    c._put(29, 10, YELLOW)
    c.rect(22, 13, 12, 1, CONCRETE)
    # fence
    for fx in range(0, 56, 2):
        c.line_v(fx, 14, 3, FENCE)
    c.line_h(0, 14, 56, METAL)
    c.line_h(0, 16, 56, METAL)
    # basketball hoop
    c.line_v(45, 8, 9, POLE)
    c.rect(42, 8, 3, 2, BACKBOARD)
    c.rect(41, 10, 4, 1, HOOP)
    # ground
    c.rect(0, 17, 56, 5, CONCRETE)
    c.line_h(35, 19, 16, WHITE)
    c.line_h(35, 21, 16, WHITE)
    c.line_v(35, 19, 3, WHITE)
    return c.render()


def scene_corner_store():
    c = Canvas(56, 22, SKY)
    # left building
    c.rect(0, 4, 12, 14, BRICK_DARK)
    c.rect(2, 6, 4, 4, WINDOW_DARK)
    c.rect(7, 6, 4, 4, WINDOW_DARK)
    c.rect(2, 11, 4, 4, WINDOW_LIT)
    # store
    c.rect(14, 5, 26, 13, BRICK_TAN)
    for ax in range(14, 40):
        col = AWNING if (ax // 2) % 2 == 0 else AWNING_W
        c._put(ax, 9, col)
        c._put(ax, 10, col)
    c.rect(16, 11, 8, 6, (200, 220, 230))
    c.rect(30, 11, 8, 6, (200, 220, 230))
    c.line_v(20, 11, 6, METAL)
    c.line_v(34, 11, 6, METAL)
    c.rect(25, 12, 4, 6, (140, 160, 170))
    c._put(28, 15, YELLOW)
    for nx in (17, 18, 20, 21):
        c._put(nx, 12, NEON)
    # right building
    c.rect(42, 3, 14, 15, BRICK)
    c.rect(44, 5, 4, 4, WINDOW_LIT)
    c.rect(50, 5, 4, 4, WINDOW_DARK)
    c.rect(44, 10, 4, 4, WINDOW_DARK)
    c.rect(50, 10, 4, 4, WINDOW_LIT)
    # ground
    c.rect(0, 18, 56, 2, SIDEWALK)
    c.rect(0, 20, 56, 2, ASPHALT)
    for sx in range(4, 50, 14):
        c.line_h(sx, 21, 3, YELLOW_LINE)
    return c.render()


def scene_alley():
    c = Canvas(56, 22, (15, 15, 25))
    c.rect(14, 0, 28, 3, (45, 50, 75))
    # walls
    c.rect(0, 0, 13, 22, BRICK)
    c.rect(43, 0, 13, 22, BRICK)
    for wy in range(0, 22, 3):
        c.line_h(1, wy, 12, (140, 50, 40))
        c.line_h(43, wy, 12, (140, 50, 40))
    c.rect(6, 3, 4, 4, WINDOW_DARK)
    c.rect(46, 5, 4, 4, WINDOW_LIT)
    # dumpster
    c.rect(16, 14, 8, 5, DUMPSTER)
    c.rect(16, 14, 8, 1, (55, 100, 55))
    c.rect(16, 15, 1, 4, (35, 70, 35))
    # puddle
    c.oval(35, 19, 4, 1, PUDDLE)
    # ground
    c.rect(14, 20, 28, 2, (40, 38, 42))
    # fire escape
    c.line_h(42, 8, 3, METAL)
    c.line_v(42, 8, 6, METAL)
    c.line_h(42, 14, 3, METAL)
    return c.render()


def scene_woods():
    c = Canvas(56, 22, (35, 55, 30))
    # sky through canopy
    c.gradient_v(0, 0, 56, 6, (60, 90, 50), (35, 55, 30))
    # canopy gaps
    for gx in [12, 28, 42]:
        c.rect(gx, 1, 3, 2, (80, 130, 70))
    # tree trunks
    for tx in [5, 18, 33, 48]:
        c.rect(tx, 4, 3, 16, TREE_TRUNK)
        c.rect(tx - 1, 5, 1, 6, (75, 50, 22))
    # canopy foliage
    c.oval(6, 2, 5, 3, TREE_GREEN)
    c.oval(19, 1, 6, 3, TREE_DARK)
    c.oval(34, 2, 5, 3, TREE_GREEN)
    c.oval(49, 1, 4, 3, TREE_DARK)
    # ground cover
    c.rect(0, 18, 56, 4, (45, 65, 30))
    c.rect(0, 20, 56, 2, DIRT)
    # debris — broken bottle
    c._put(25, 19, (140, 180, 200))
    c._put(26, 19, (140, 180, 200))
    # old mattress
    c.rect(38, 18, 7, 2, (100, 85, 75))
    c.rect(38, 18, 7, 1, (120, 100, 85))
    return c.render()


def scene_abandoned_lot():
    c = Canvas(56, 22, SKY)
    c.gradient_v(0, 0, 56, 8, SKY_LIGHT, SKY)
    # clouds
    c.oval(8, 2, 5, 2, CLOUD)
    c.oval(40, 3, 4, 2, CLOUD)
    # fence left/right
    for fx in range(0, 14, 3):
        c.line_v(fx, 8, 10, FENCE)
    c.line_h(0, 8, 14, FENCE)
    c.line_h(0, 12, 14, FENCE)
    for fx in range(42, 56, 3):
        c.line_v(fx, 8, 10, FENCE)
    c.line_h(42, 8, 14, FENCE)
    c.line_h(42, 12, 14, FENCE)
    # gap in fence
    c.rect(14, 10, 2, 6, (45, 65, 30))
    # crumbling foundation
    c.rect(20, 15, 18, 3, CONCRETE)
    c.rect(20, 15, 18, 1, (135, 130, 125))
    # rebar sticking up
    c.line_v(24, 13, 3, METAL)
    c.line_v(32, 12, 4, METAL)
    # weeds
    for wx in [16, 22, 30, 40, 45]:
        c.line_v(wx, 17, 3, GRASS_DARK)
        c._put(wx, 17, GRASS)
    # ground
    c.rect(0, 18, 56, 4, DIRT)
    c.rect(14, 19, 28, 3, (105, 75, 35))
    # broken glass scatter
    for gx in [19, 27, 35]:
        c._put(gx, 19, (180, 200, 220))
    return c.render()


def scene_construction_site():
    c = Canvas(56, 22, SKY)
    c.gradient_v(0, 0, 56, 6, SKY_LIGHT, SKY)
    # crane arm
    c.line_h(2, 1, 25, METAL)
    c.line_v(2, 1, 5, METAL)
    c.line_v(25, 1, 3, METAL)
    # cable from crane
    c.line_v(20, 3, 6, (100, 100, 105))
    # concrete pillars
    c.rect(8, 6, 4, 16, CONCRETE)
    c.rect(28, 6, 4, 16, CONCRETE)
    c.rect(44, 8, 4, 14, CONCRETE)
    # floor slab (2nd floor)
    c.rect(6, 10, 28, 2, (140, 135, 130))
    # exposed rebar
    c.line_v(14, 6, 4, (160, 60, 40))
    c.line_v(36, 8, 3, (160, 60, 40))
    # orange safety fence (fallen over)
    c.rect(0, 16, 8, 1, (230, 120, 20))
    c.rect(48, 17, 8, 1, (230, 120, 20))
    # lumber pile
    c.rect(38, 16, 6, 2, (170, 120, 60))
    c.rect(39, 15, 4, 1, (160, 110, 50))
    # ground
    c.rect(0, 18, 56, 4, DIRT)
    c.rect(0, 20, 56, 2, CONCRETE)
    # debris
    c._put(18, 19, METAL)
    c._put(42, 19, METAL)
    return c.render()


def scene_combat():
    c = Canvas(56, 16, (60, 55, 70))
    c.gradient_v(0, 0, 56, 6, (40, 35, 55), (60, 55, 70))
    c.line_v(8, 2, 10, POLE)
    c.rect(6, 2, 5, 1, METAL)
    c.circle(8, 3, 1, YELLOW)
    c.rect(0, 12, 56, 4, ASPHALT)
    for sx in range(10, 50, 15):
        c.line_h(sx, 14, 4, YELLOW_LINE)
    return c.render()


# ── Chapter 2 scenes ────────────────────────────────────────────────────────
CAR_RED     = (180, 30, 25)
CAR_CHROME  = (190, 195, 200)
LEATHER     = (60, 35, 20)
NEON_PINK   = (255, 50, 120)
NEON_BLUE   = (50, 120, 255)
SPEAKER     = (40, 40, 45)
SHOP_WALL   = (170, 130, 90)


def scene_the_strip():
    c = Canvas(56, 22, (55, 50, 75))
    # sky gradient — dusk feel
    c.gradient_v(0, 0, 56, 6, (70, 50, 90), (55, 50, 75))
    # left building — head shop
    c.rect(0, 4, 16, 14, BRICK_DARK)
    c.rect(2, 6, 5, 4, WINDOW_LIT)
    c.rect(9, 6, 5, 4, WINDOW_LIT)
    c.rect(5, 12, 5, 6, DOOR)
    for nx in (2, 3, 5, 6):
        c._put(nx, 5, NEON_PINK)
    # center building — bodega
    c.rect(18, 5, 20, 13, SHOP_WALL)
    for ax in range(18, 38):
        col = AWNING if (ax // 2) % 2 == 0 else AWNING_W
        c._put(ax, 9, col)
        c._put(ax, 10, col)
    c.rect(20, 11, 6, 6, (200, 220, 230))
    c.rect(30, 11, 6, 6, (200, 220, 230))
    c.rect(26, 12, 4, 6, (130, 150, 160))
    c._put(29, 15, YELLOW)
    for nx in (20, 21, 23, 24):
        c._put(nx, 5, NEON)
    # right building
    c.rect(40, 3, 16, 15, BRICK)
    c.rect(42, 5, 4, 4, WINDOW_DARK)
    c.rect(48, 5, 4, 4, WINDOW_LIT)
    c.rect(42, 10, 4, 4, WINDOW_LIT)
    # neon sign glow
    for nx in range(41, 53):
        c._put(nx, 3, NEON_BLUE)
    # ground
    c.rect(0, 18, 56, 2, SIDEWALK)
    c.rect(0, 20, 56, 2, ASPHALT)
    for sx in range(4, 50, 10):
        c.line_h(sx, 21, 3, YELLOW_LINE)
    return c.render()


def scene_head_shop():
    c = Canvas(56, 22, (45, 35, 55))
    # walls — dark interior
    c.rect(0, 0, 56, 18, (55, 40, 60))
    # shelves on the wall
    for sy in (3, 8, 13):
        c.rect(2, sy, 20, 1, (90, 60, 35))
        c.rect(34, sy, 20, 1, (90, 60, 35))
    # items on shelves (colourful spots)
    for sx in range(4, 20, 4):
        c.rect(sx, 2, 2, 1, METAL)
    for sx in range(36, 52, 4):
        c.rect(sx, 7, 2, 1, (200, 50, 50))
    for sx in range(4, 20, 5):
        c.rect(sx, 12, 2, 1, YELLOW)
    # display case / counter
    c.rect(18, 14, 20, 2, (80, 55, 30))
    c.rect(20, 14, 16, 1, (130, 160, 180))
    # brass knuckles on display
    c.rect(26, 13, 4, 1, METAL)
    # floor
    c.rect(0, 18, 56, 4, (70, 55, 40))
    c.line_h(0, 19, 56, (60, 45, 32))
    c.line_h(0, 21, 56, (60, 45, 32))
    return c.render()


def scene_bodega():
    c = Canvas(56, 22, WALL)
    c.rect(0, 0, 56, 3, (200, 190, 170))
    # cooler
    c.rect(2, 3, 12, 12, (130, 160, 180))
    c.rect(3, 4, 4, 10, (90, 140, 170))
    c.rect(8, 4, 5, 10, (90, 140, 170))
    c.line_v(7, 3, 12, METAL)
    # shelves
    for sy in (4, 8, 12):
        c.rect(20, sy, 16, 1, (100, 70, 40))
    for sx in range(21, 35, 3):
        c.rect(sx, 3, 2, 1, (220, 30, 30))
        c.rect(sx, 7, 2, 1, (30, 150, 30))
        c.rect(sx, 11, 2, 1, (200, 180, 40))
    # counter
    c.rect(40, 12, 14, 3, (100, 70, 40))
    c.rect(42, 11, 4, 1, (120, 120, 130))
    # floor
    c.rect(0, 16, 56, 6, (140, 130, 115))
    c.line_h(0, 18, 56, (125, 115, 100))
    c.line_h(0, 20, 56, (125, 115, 100))
    return c.render()


def scene_parking_lot():
    c = Canvas(56, 22, (55, 50, 75))
    c.gradient_v(0, 0, 56, 8, (70, 50, 90), (55, 50, 75))
    # back wall / fence
    c.rect(0, 8, 56, 2, FENCE)
    for fx in range(0, 56, 3):
        c.line_v(fx, 6, 4, METAL)
    # the Chevelle — centre stage
    c.rect(16, 12, 24, 5, CAR_RED)
    c.rect(14, 14, 3, 2, CAR_RED)
    c.rect(39, 14, 3, 2, CAR_RED)
    c.rect(18, 12, 8, 2, (120, 160, 200))    # windshield
    c.rect(30, 12, 6, 2, (120, 160, 200))    # rear window
    c.rect(27, 12, 3, 2, CAR_RED)            # roof pillar
    c.rect(14, 16, 4, 1, (25, 25, 25))       # front tire
    c.rect(38, 16, 4, 1, (25, 25, 25))       # rear tire
    c.rect(15, 15, 2, 1, CAR_CHROME)         # front bumper
    c.rect(39, 15, 2, 1, CAR_CHROME)         # rear bumper
    c.rect(14, 13, 2, 1, YELLOW)             # headlight
    c.rect(40, 13, 2, 1, (200, 30, 30))      # taillight
    # random parked car
    c.rect(2, 13, 10, 4, (60, 60, 90))
    c.rect(4, 13, 4, 2, (100, 130, 160))
    c.rect(2, 17, 3, 1, (25, 25, 25))
    c.rect(9, 17, 3, 1, (25, 25, 25))
    # ground
    c.rect(0, 17, 56, 5, ASPHALT)
    # parking lines
    for px in range(6, 50, 14):
        c.line_v(px, 18, 4, (80, 80, 70))
    return c.render()


def scene_boom_car():
    c = Canvas(56, 22, SKY)
    c.oval(10, 2, 4, 1, CLOUD)
    c.circle(48, 3, 2, SUN)
    # the boom car — old Buick on blocks
    c.rect(10, 10, 28, 6, (70, 70, 100))
    c.rect(8, 12, 3, 3, (70, 70, 100))
    c.rect(37, 12, 3, 3, (70, 70, 100))
    c.rect(13, 10, 8, 3, (100, 130, 160))    # windshield
    c.rect(28, 10, 6, 3, (100, 130, 160))    # rear window
    # speakers in back seat
    c.rect(24, 11, 4, 2, SPEAKER)
    c.rect(25, 11, 2, 2, (60, 60, 65))
    # cinder blocks (no tires)
    c.rect(10, 16, 3, 2, CONCRETE)
    c.rect(35, 16, 3, 2, CONCRETE)
    # music notes
    c._put(20, 7, YELLOW)
    c._put(23, 6, YELLOW)
    c._put(26, 8, YELLOW)
    # ground
    c.rect(0, 18, 56, 4, GRASS)
    c.rect(5, 19, 40, 3, DIRT)
    return c.render()


# ── Chapter 3 scenes ────────────────────────────────────────────────────────
RUST        = (160, 80, 35)
RUST_DARK   = (110, 55, 25)
GRAVEL      = (100, 95, 85)
CHAIN_LINK  = (145, 145, 140)
RAIL        = (95, 90, 85)
BOXCAR_BLUE = (55, 70, 110)
BOXCAR_RED  = (130, 45, 35)
CRATE       = (140, 100, 55)
FIRE_ORANGE = (240, 140, 30)
FIRE_YELLOW = (255, 210, 50)


def scene_the_yard():
    c = Canvas(56, 22, (80, 100, 130))
    c.gradient_v(0, 0, 56, 6, (100, 110, 140), (80, 100, 130))
    c.oval(8, 2, 5, 1, CLOUD)
    # chain-link fence across top
    for x in range(0, 56, 2):
        c._put(x, 6, CHAIN_LINK)
    # barbed wire
    for x in range(1, 56, 4):
        c._put(x, 5, METAL)
    # boxcar left
    c.rect(2, 8, 16, 7, BOXCAR_BLUE)
    c.rect(4, 9, 4, 3, RUST)
    c.rect(10, 9, 4, 3, RUST_DARK)
    c.rect(8, 12, 4, 3, (35, 35, 40))  # open door
    # boxcar right
    c.rect(34, 9, 14, 6, BOXCAR_RED)
    c.rect(36, 10, 3, 2, RUST)
    c.rect(42, 10, 3, 2, RUST_DARK)
    # rail tracks
    c.rect(0, 16, 56, 1, RAIL)
    c.rect(0, 18, 56, 1, RAIL)
    for x in range(2, 54, 6):
        c.rect(x, 16, 4, 3, (80, 55, 30))  # ties
    # gravel ground
    c.rect(0, 19, 56, 3, GRAVEL)
    return c.render()


def scene_pawn_shop():
    c = Canvas(56, 22, (60, 55, 75))
    # building
    c.rect(6, 4, 44, 14, BRICK_TAN)
    c.rect(6, 3, 44, 1, ROOF)
    # sign area
    c.rect(16, 5, 24, 3, (30, 30, 35))
    # windows
    c.rect(10, 9, 8, 5, WINDOW_LIT)
    c.rect(38, 9, 8, 5, WINDOW_LIT)
    # stuff in windows (guitars, tools)
    c.rect(11, 11, 2, 3, (150, 80, 30))  # guitar
    c.rect(14, 12, 3, 2, METAL)          # tool
    c.rect(39, 11, 2, 3, CRATE)          # box
    c.rect(43, 12, 2, 2, METAL)          # wrench
    # door
    c.rect(24, 9, 8, 9, DOOR)
    c.rect(29, 13, 1, 1, YELLOW)  # knob
    # sidewalk
    c.rect(0, 18, 56, 4, SIDEWALK)
    return c.render()


def scene_boxcar_row():
    c = Canvas(56, 22, (75, 90, 115))
    c.gradient_v(0, 0, 56, 5, (90, 100, 130), (75, 90, 115))
    # row of boxcars receding
    c.rect(0, 7, 14, 8, BOXCAR_RED)
    c.rect(2, 8, 3, 3, RUST)
    c.rect(7, 8, 3, 3, RUST_DARK)
    c.rect(16, 8, 12, 7, BOXCAR_BLUE)
    c.rect(18, 9, 3, 2, RUST)
    c.rect(23, 9, 3, 2, RUST_DARK)
    c.rect(20, 12, 4, 3, (35, 35, 40))  # open door
    c.rect(30, 9, 12, 6, (90, 85, 70))  # tan boxcar
    c.rect(32, 10, 3, 2, RUST)
    c.rect(44, 8, 12, 7, BOXCAR_RED)
    c.rect(46, 9, 3, 3, RUST_DARK)
    # rails
    c.rect(0, 16, 56, 1, RAIL)
    for x in range(2, 54, 5):
        c.rect(x, 16, 3, 1, (80, 55, 30))
    # gravel
    c.rect(0, 17, 56, 5, GRAVEL)
    return c.render()


def scene_loading_dock():
    c = Canvas(56, 22, (70, 80, 110))
    # dock platform
    c.rect(0, 10, 56, 3, CONCRETE)
    c.rect(0, 9, 56, 1, (130, 130, 125))  # edge
    # roller doors
    c.rect(4, 4, 10, 6, METAL)
    c.rect(5, 4, 8, 1, (100, 100, 105))
    c.rect(18, 4, 10, 6, METAL)
    c.rect(19, 4, 8, 1, (100, 100, 105))
    c.rect(32, 4, 10, 6, (110, 110, 115))  # slightly open
    c.rect(33, 8, 8, 2, (35, 35, 40))      # gap
    # wall above
    c.rect(0, 2, 56, 2, BRICK_DARK)
    # pallets
    c.rect(46, 6, 6, 4, CRATE)
    c.rect(47, 5, 4, 1, CRATE)
    c.rect(48, 4, 2, 1, CRATE)
    # forklift
    c.rect(42, 11, 6, 2, YELLOW)
    c.rect(41, 13, 2, 1, (25, 25, 25))  # tire
    c.rect(47, 13, 2, 1, (25, 25, 25))  # tire
    # ground
    c.rect(0, 13, 56, 9, ASPHALT)
    return c.render()


def scene_warehouse():
    c = Canvas(56, 22, (35, 35, 40))
    # metal walls
    c.rect(0, 0, 4, 22, METAL)
    c.rect(52, 0, 4, 22, METAL)
    # ceiling beams
    c.rect(4, 1, 48, 1, (60, 60, 65))
    c.rect(4, 0, 48, 1, (50, 50, 55))
    # high windows — dusty light
    c.rect(15, 2, 6, 3, (120, 130, 140))
    c.rect(35, 2, 6, 3, (120, 130, 140))
    # crate stacks
    c.rect(6, 8, 8, 6, CRATE)
    c.rect(7, 6, 6, 2, CRATE)
    c.rect(8, 5, 4, 1, (130, 90, 45))
    c.rect(18, 10, 6, 4, CRATE)
    c.rect(19, 8, 4, 2, (130, 90, 45))
    c.rect(32, 9, 8, 5, CRATE)
    c.rect(33, 7, 6, 2, CRATE)
    c.rect(44, 10, 6, 4, (130, 90, 45))
    # floor
    c.rect(4, 16, 48, 6, CONCRETE)
    # chain hanging
    c.line_v(26, 1, 8, CHAIN_LINK)
    return c.render()


def scene_skinhead_hangout():
    c = Canvas(56, 22, (60, 55, 70))
    c.gradient_v(0, 0, 56, 5, (70, 55, 75), (60, 55, 70))
    # office trailer
    c.rect(10, 6, 30, 10, (150, 145, 130))
    c.rect(10, 5, 30, 1, METAL)  # roof
    # windows
    c.rect(14, 8, 5, 3, WINDOW_LIT)
    c.rect(25, 8, 5, 3, WINDOW_LIT)
    c.rect(33, 8, 5, 3, WINDOW_DARK)
    # door
    c.rect(20, 9, 4, 7, DOOR)
    c.rect(22, 12, 1, 1, YELLOW)  # knob
    # steps
    c.rect(19, 16, 6, 1, CONCRETE)
    # fire barrel
    c.rect(44, 11, 4, 5, (50, 45, 40))
    c.rect(45, 10, 2, 1, FIRE_ORANGE)
    c.rect(45, 9, 2, 1, FIRE_YELLOW)
    # graffiti "RAZOR" (just red marks)
    for x in range(12, 18):
        c._put(x, 13, (200, 30, 30))
    # ground
    c.rect(0, 17, 56, 5, GRAVEL)
    return c.render()


# map of location id → scene function
SCENES = {
    "home": scene_home,
    "your_block": scene_your_block,
    "park": scene_park,
    "schoolyard": scene_schoolyard,
    "corner_store": scene_corner_store,
    "alley": scene_alley,
    "woods": scene_woods,
    "abandoned_lot": scene_abandoned_lot,
    "construction_site": scene_construction_site,
    "the_strip": scene_the_strip,
    "head_shop": scene_head_shop,
    "bodega": scene_bodega,
    "parking_lot": scene_parking_lot,
    "boom_car": scene_boom_car,
    "the_yard": scene_the_yard,
    "pawn_shop": scene_pawn_shop,
    "boxcar_row": scene_boxcar_row,
    "loading_dock": scene_loading_dock,
    "warehouse": scene_warehouse,
    "skinhead_hangout": scene_skinhead_hangout,
}
