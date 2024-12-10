import sys
import collections
from .gridlib.gridlib import Grid

grid = Grid(filepath=sys.argv[1], default_factory=int)
grid.print()


def search(cell, ends):
    match cell.value:
        case 9:
            ends[cell.id] = ends[cell.id] + 1

    for n in grid.cardinal_cells(cell):
        if n.value == "." or cell.value == ".":
            continue
        if int(n.value) - int(cell.value) == 1:
            ends = search(n, ends)

    return ends


sum = 0
for cell in grid:
    if cell.value != 0:
        continue
    ends = search(cell, collections.defaultdict(int))
    print(ends)
    for k, v in ends.items():
        sum += v

print(sum)
