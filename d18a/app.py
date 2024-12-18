import sys
import heapq
from .gridlib.gridlib import Grid, Cell, Direction, DirNorth, DirEast, DirSouth, DirWest

filename = sys.argv[1]
size = int(sys.argv[2])
limit = int(sys.argv[3])

grid = Grid(s=("." * size + "\n") * size)

with open(sys.argv[1]) as f:
    for line in f.readlines()[:limit]:
        x, y = [int(x) for x in line.strip().split(",")]
        grid.set_at(x, y, "#")


def solve(start, end, steps):
    distances = {cell.id: float("inf") for cell in grid}
    distances[start.id] = 0
    pq = [(0, start, steps)]

    while pq:
        cur_dist, cell, steps = heapq.heappop(pq)
        steps.append(cell)

        if cur_dist > distances[cell.id]:
            continue

        if cell == end:
            return steps

        for n in grid.cardinal_cells(cell):
            if n and n.value != "#":
                dist = cur_dist + 1
                if dist < distances[n.id]:
                    distances[n.id] = dist
                    heapq.heappush(pq, (dist, n, steps.copy()))


start = grid.get_at(0, 0)
start.value = "S"
end = grid.get_at(size - 1, size - 1)
end.value = "E"
grid.print()
steps = solve(start, end, [])

steps.pop(0)

for cell in steps:
    cell.value = "O"

grid.print()

print("STEPS", len(steps))
