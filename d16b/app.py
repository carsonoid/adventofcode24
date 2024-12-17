import sys
import heapq
from .gridlib.gridlib import Grid, Cell, Direction, DirNorth, DirEast, DirSouth, DirWest


grid = Grid(filepath=sys.argv[1])
grid.print()

dirs = [
    DirEast,
    DirSouth,
    DirWest,
    DirNorth,
]


def get_moves(cell, di):
    return [
        (grid.get_relative(cell, dirs[di]), di, 1),  # forward
        (
            grid.get_relative(cell, dirs[(di + 1) % 4]),
            (di + 1) % 4,
            1001,
        ),  # 90 deg right
        (
            grid.get_relative(cell, dirs[(di + 3) % 4]),
            (di + 3) % 4,
            1001,
        ),  # 90 deg left
    ]


def solve(start, original_di=0):
    distances = {cell.id: float("inf") for cell in grid}
    distances[start.id] = 0
    pq = [(0, start, original_di)]

    while pq:
        cur_dist, cell, di = heapq.heappop(pq)

        if cur_dist > distances[cell.id]:
            continue

        if cell.value == "E":
            return cur_dist

        for n, di, cost in get_moves(cell, di):
            if n and n.value != "#":
                dist = cur_dist + cost
                if dist < distances[n.id]:
                    distances[n.id] = dist
                    heapq.heappush(pq, (dist, n, di))


start = grid.get_at(1, -2)
shortest = solve(start)

print(shortest)

cells = {}


def find_possible(cell, di, dist):
    if cell.id in cells:
        return

    if solve(cell, di) != dist:
        return

    cells[cell.id] = cell

    for n, di, cost in get_moves(cell, di):
        if n and n.value != "#":
            find_possible(n, di, dist - cost)


find_possible(start, 0, shortest)

printgrid = Grid(filepath=sys.argv[1])
for cell in cells.values():
    printgrid.set_at(cell.x, cell.y, "O")
printgrid.print()

print(len(cells))
