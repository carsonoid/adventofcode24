import sys
import heapq
from .gridlib.gridlib import Grid, Cell, Direction, DirNorth, DirEast, DirSouth, DirWest

filename = sys.argv[1]
size = int(sys.argv[2])

grid = Grid(s=("." * size + "\n") * size)

bytes = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        x, y = [int(x) for x in line.strip().split(",")]
        bytes.append((x, y))


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


for byte in bytes:
    grid.set_at(*byte, "#")
    steps = solve(start, end, [])
    if not steps:
        print(f"NO EXIT AT: {byte[0]},{byte[1]}")
        exit()
