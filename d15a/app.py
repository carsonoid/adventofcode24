import sys
from .gridlib.gridlib import Grid, DirNorth, DirEast, DirSouth, DirWest


def move_cell(cell, dir) -> bool:
    next = grid.get_relative(cell, dir)

    if next.value == "#":
        return False

    if next.value == "O":
        if not move_cell(next, dir):
            return False

    if next.value == ".":
        cell.value, next.value = next.value, cell.value
        return True
    else:
        raise Exception(f"Unexpected value {next.value}")


dirs = {
    "^": DirNorth,
    "v": DirSouth,
    "<": DirWest,
    ">": DirEast,
}

with open(sys.argv[1]) as f:
    gridstr, movesstr = f.read().split("\n\n")

grid = Grid(s=gridstr, default_factory=str)
grid.print()


for m in filter(lambda x: x != "\n", list(movesstr.strip())):
    pos = grid.find("@")
    move_cell(pos, dirs[m])

grid.print()

total = 0
for cell in grid:
    if cell.value == "O":
        total += 100 * cell.y + cell.x

print(total)
