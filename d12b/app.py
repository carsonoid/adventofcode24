import sys
import collections
from .gridlib.gridlib import Grid, Cell


grid = Grid(filepath=sys.argv[1], default_factory=str)
grid.print()

seen = set()


class Region:
    def __init__(self, v) -> None:
        self.v = v
        self.a = 0
        self.sides = collections.defaultdict(set)

    def price(self):
        return self.a * self.unique_sides()

    def __str__(self) -> str:
        return f"Region {self.v} a: {self.a} - sides: {self.unique_sides()}, price: {self.price()}"

    def add_side(self, a, p1, p2, pos):
        self.sides[f"{a}:{p1},{p2}"].add(pos)

    def unique_sides(self):
        count = 0
        for k, v in self.sides.items():
            count += 1
            side = sorted(list(v))
            cur = side[0]
            for i in range(1, len(side)):
                if abs(side[i] - cur) != 1:
                    count += 1
                cur = side[i]
        return count


def search(cell: Cell, region: Region):
    if cell.id in seen:
        return

    seen.add(cell.id)
    region.a += 1

    for n in grid.all_cardinal_cells(cell):
        if n.value == cell.value:
            search(n, region)
        else:
            if n.x == cell.x:
                region.add_side("y", n.y, cell.y, cell.x)
            if n.y == cell.y:
                region.add_side("x", n.x, cell.x, cell.y)


tot = 0
for cell in grid:
    if cell.id in seen:
        continue

    region = Region(cell.value)
    search(cell, region)
    print(region, "X")
    tot += region.price()


print(tot)
