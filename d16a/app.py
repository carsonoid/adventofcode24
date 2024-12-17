import sys
import heapq
from .gridlib.gridlib import Grid, Cell, Direction, DirNorth, DirEast, DirSouth, DirWest


grid = Grid(filepath=sys.argv[1])
grid.print()

printgrid = Grid(filepath=sys.argv[1])

start = grid.get_at(1, -2)
end = grid.get_at(-2, 1)

dirs = [
    DirEast,
    DirSouth,
    DirWest,
    DirNorth,
]

distances = {cell.id: float("inf") for cell in grid}
distances[start.id] = 0
pq = [(0, start, 0)]


while pq:
    cur_dist, cell, di = heapq.heappop(pq)
    printgrid.set_at(cell.x, cell.y, "o")

    if cur_dist > distances[cell.id]:
        continue

    n = grid.get_relative(cell, dirs[di])
    if n and n.value != "#":
        dist = cur_dist + 1
        if dist < distances[n.id]:
            distances[n.id] = dist
            heapq.heappush(pq, (dist, n, di))

    turns = [
        (grid.get_relative(cell, dirs[(di + 1) % 4]), (di + 1) % 4),  # 90 deg right
        (grid.get_relative(cell, dirs[(di + 3) % 4]), (di + 3) % 4),  # 90 deg left
    ]

    for n, di in turns:
        if n and n.value != "#":
            dist = cur_dist + 1001
            if dist < distances[n.id]:
                distances[n.id] = dist
                heapq.heappush(pq, (dist, n, di))


printgrid.print()

print(distances[end.id])
