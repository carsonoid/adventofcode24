import sys
import itertools
import math
from collections import deque, defaultdict
from .gridlib.gridlib import Grid, Cell

grid = Grid(filepath=sys.argv[1])
grid.print()


def bfs(start: Cell):
    q = deque()
    q.append((0, start, []))
    distances = defaultdict(lambda: float("inf"))

    while q:
        dist, cur, path = q.popleft()
        distances[cur.id] = dist
        path.append((cur.x, cur.y))

        if cur.value == "E":
            return distances, path

        for n in grid.cardinal_cells(cur):
            if n.id not in distances and n.value != "#":
                q.append((dist + 1, n, path.copy()))


start = grid.find("S")
end = grid.find("E")
distances, path = bfs(start)

saved_totals = defaultdict(int)

for i in range(len(path)):
    p1 = path[i]
    for j in range(i + 100, len(path)):
        p2 = path[j]
        d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        if d <= 20:
            saved_totals[j - i - d] += 1

total = 0
for saved, times in saved_totals.items():
    if saved >= 50:
        print(f"there are {times} cheats that save {saved} picoseconds")

    if saved >= 100:
        total += times
print("Total:", total)
