import sys
from .gridlib.gridlib import Grid, Cell


class Numpad:
    name: str
    grid: Grid
    keys: dict
    pos: Cell

    def __init__(self, name, grid: Grid, parent=None):
        self.name = name
        self.grid = grid
        self.keys = {}
        for cell in grid:
            self.keys[cell.value] = cell
        self.pos = self.keys["A"]
        self.parent = parent

    def press(self, key, times=1):
        next = self.keys[key]
        x = next.x - self.pos.x
        y = next.y - self.pos.y
        keys = [key] * times
        print(f"{self.name} - next: {x} {y}")

        if self.parent:
            if x < 0:
                _, _, pkeys = self.parent.press("<", times=abs(x))
                keys.extend(pkeys)
            elif x > 0:
                _, _, pkeys = self.parent.press(">", times=x)
                keys.extend(pkeys)
            else:
                _, _, pkeys = self.parent.press("A")
                keys.extend(pkeys)

            _, _, pkeys = self.parent.press("A")
            keys.extend(pkeys)

        self.pos = next

        return x, y, keys


numpad_str = "789\n456\n123\n.0A"
arrowpad_str = ".^A\n<v>"


with open(sys.argv[1]) as f:
    codes = f.read().strip().split("\n")

r1 = Numpad("r1", Grid(s=arrowpad_str))
dp = Numpad("dp", Grid(s=numpad_str), r1)

print(dp.press("0"))
# print(dp.press("2"))
# print(dp.press("9"))
# print(dp.press("A"))
# tot = 0
# for k in "029A":
#     _, _, c = dp.press(k)
#     print(k, "cost", c)
#     tot += c
#     break

# print(tot)

# for code in codes:
#     print(code)
#     dp = Numpad(Grid(s=numpad_str))
#     r1 = Numpad(Grid(s=arrowpad_str), dp)
#     r2 = Numpad(Grid(s=arrowpad_str), r1)
#     hp = Numpad(Grid(s=arrowpad_str), r2)

#     for key in code:
#         dpv, dph = dp.press(key)
#         print(f"dp: {dpv} {dph}")
#         if dph < 0:
#             rh, rv = r1.press("<")
#             print(f"r1: {rv} {rh}")
#         if dph > 0:
#             rh, rv = r1.press(">")
#             print(f"r1: {rv} {rh}")
#         if dpv < 0:
#             rh, rv = r1.press("^")
#             print(f"r1: {rv} {rh}")
#         if dpv > 0:
#             rh, rv = r1.press("v")
#             print(f"r1: {rv} {rh}")
#         break
#     break
