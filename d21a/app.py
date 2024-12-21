import sys
from .gridlib.gridlib import Grid, Cell


class Arrowpad:
    name: str
    grid: Grid
    keys: dict
    pos: Cell

    def __init__(self, name):
        self.name = name
        self.grid = Grid(s=".^A\n<v>")
        self.keys = {}
        for cell in self.grid:
            self.keys[cell.value] = cell
        self.pos = self.keys["A"]

    def press(self, key):
        next = self.keys[key]
        x = next.x - self.pos.x
        y = next.y - self.pos.y
        keys = []
        if x < 0:
            keys.extend(["<"] * abs(x))
        elif x > 0:
            keys.extend([">"] * x)

        if y < 0:
            keys.extend(["^"] * abs(y))
        elif y > 0:
            keys.extend(["v"] * y)

        keys.append("A")

        self.pos = next

        return keys

    def press_all(self, keys):
        all = []
        for key in keys:
            all.extend(self.press(key))
        return all


class Numpad:
    name: str
    grid: Grid
    keys: dict
    pos: Cell

    def __init__(self, name):
        self.name = name
        self.grid = Grid(s="789\n456\n123\n.0A")
        self.keys = {}
        for cell in self.grid:
            self.keys[cell.value] = cell
        self.pos = self.keys["A"]

    def press(self, key):
        next = self.keys[key]
        x = next.x - self.pos.x
        y = next.y - self.pos.y
        keys = []
        if x < 0:
            keys.extend(["<"] * abs(x))
        elif x > 0:
            keys.extend([">"] * x)

        if y < 0:
            keys.extend(["^"] * abs(y))
        elif y > 0:
            keys.extend(["v"] * y)

        keys.extend("A")
        self.pos = next

        return keys

    def press_all(self, keys):
        all = []
        for key in keys:
            all.extend(self.press(key))
        return all


with open(sys.argv[1]) as f:
    codes = f.read().strip().split("\n")


tot = 0
codes = ["456A"]
for code in codes:
    dp = Numpad("dp")
    ap1 = Arrowpad("ap1")
    ap2 = Arrowpad("ap2")

    print(code)
    l1 = dp.press_all(code)
    print("".join(l1))

    l2 = ap1.press_all("".join(l1))
    print("".join(l2))

    l3 = ap2.press_all("".join(l2))
    print("".join(l3))

    complexity = len(l3) * int(code.rstrip("A"))
    print(len(l3), int(code.rstrip("A")), complexity)
    tot += complexity

print(tot)
