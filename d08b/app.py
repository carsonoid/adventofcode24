import sys
import collections
from .gridlib.gridlib import Grid

grid = Grid(filepath=sys.argv[1])
grid.print()

end_grid = Grid(filepath=sys.argv[1])


ants = collections.defaultdict(list)

for cell in grid:
    c = cell.value
    if c != ".":
        ants[c].append(cell)

locs = set()

for ant, locations in ants.items():
    print(*locations)
    for i, a in enumerate(locations):
        for j, b in enumerate(locations):
            if i == j:
                continue
            dx = a.x - b.x
            dy = a.y - b.y
            x = a.x
            y = a.y
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
