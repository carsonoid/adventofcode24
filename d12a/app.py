import sys
import collections
from .gridlib.gridlib import Grid, Cell


grid = Grid(filepath=sys.argv[1], default_factory=str)
grid.print()

seen = set()


class Region:
    v = ""
    a = 0
    p = 0

    def __init__(self, v) -> None:
        self.v = v

    def price(self):
        return self.a * self.p

    def __str__(self) -> str:
        return f"Region {self.v} a: {self.a} p: {self.p}"


def search(cell: Cell, region: Region):
    if cell.id in seen:
        return
    seen.add(cell.id)
    region.a += 1

    cardinal = grid.cardinal_cells(cell)
    region.p += 4 - len(cardinal)
    for n in cardinal:
        if n.value == cell.value:
            search(n, region)
        else:
            region.p += 1


tot = 0
for cell in grid:
    region = Region(cell.value)
    search(cell, region)
    # print(region)
    tot += region.price()


print(tot)
