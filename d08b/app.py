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
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            x = a[0]
            y = a[1]
            end_grid.set_at(x, y, "#")
            locs.add((x, y))
            while True:
                x += dx
                y += dy
                if not grid.get_at(x, y):
                    break

                end_grid.set_at(x, y, "#")
                locs.add((x, y))

end_grid.print()
print(len(locs))
