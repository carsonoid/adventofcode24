import sys
import collections
from .gridlib.gridlib import Grid
from .gridlib.gridlib import CardinalDirections, DirNorth

grid = Grid(filepath=sys.argv[1])
grid.print()

cur = grid.find("^")
dir = DirNorth
positions = collections.defaultdict(str)

while True:
    positions[str(cur)] = True

    next = grid.get_relative(cur, dir)
    if not next:
        break

    if next[2] == "#":
        dir = CardinalDirections[(CardinalDirections.index(dir) + 1) % 4]
    else:
        cur = next

print(len(positions.keys()))
