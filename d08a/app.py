import sys
import collections
from .gridlib.gridlib import Grid
from .gridlib.gridlib import CardinalDirections, DirNorth

grid = Grid(filepath=sys.argv[1])
grid.print()

end_grid = Grid(filepath=sys.argv[1])


ants = collections.defaultdict(list)

for cell in grid:
    c = cell[2]
    if c != ".":
        ants[c].append(cell)

locs = set()

for ant, locations in ants.items():
    print(locations)
    for i, a in enumerate(locations):
        for j, b in enumerate(locations):
            if i == j:
                continue
            nx = a[0] + a[0] - b[0]
            ny = a[1] + a[1] - b[1]
            if grid.get_at(nx, ny):
                end_grid.set_at(nx, ny, "#")
                locs.add((nx, ny))

end_grid.print()
print(len(locs))
