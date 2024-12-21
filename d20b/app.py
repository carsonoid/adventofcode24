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

max_comb = math.comb(len(path), 2)
i = 0
for p1, p2 in itertools.combinations(path, 2):
    i += 1
    if i % 1000 == 0:
        print(f"Progress: {i}/{max_comb}")
    taken = path.index(p1)
    remaining = len(path) - 1 - path.index(p2)
    d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    if d <= 20:
        time = taken + remaining + d
        saved = len(path) - 1 - time
        saved_totals[saved] += 1

total = 0
for saved, times in saved_totals.items():
    if saved >= 50:
        print(f"there are {times} cheats that save {saved} picoseconds")

    if saved >= 100:
        total += times
print("Total:", total)
