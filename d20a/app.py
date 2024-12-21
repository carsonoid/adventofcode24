import sys
from collections import deque, defaultdict
from .gridlib.gridlib import Grid, Cell

grid = Grid(filepath=sys.argv[1])
grid.print()


def bfs(start: Cell):
    q = deque()
    q.append((0, start))
    distances = defaultdict(lambda: float("inf"))

    while q:
        dist, cur = q.popleft()
        distances[cur.id] = dist

        for n in grid.cardinal_cells(cur):
            if n.id not in distances and n.value != "#":
                q.append((dist + 1, n))

    return distances


skip_dirs = [
    [(0, -1), (0, -2)],
    [(1, 0), (2, 0)],
    [(0, 1), (0, 2)],
    [(-1, 0), (-2, 0)],
]


def bfs_skip(start: Cell, end_distances: dict[str, int]):
    q = deque()
    q.append((0, start))
    distances = defaultdict(lambda: float("inf"))
    cheats = defaultdict(int)

    while q:
        dist, cur = q.popleft()
        distances[cur.id] = dist

        for pair in skip_dirs:
            d1, d2 = pair
            s1 = grid.get_relative(cur, d1)
            if not s1 or s1.value != "#":
                continue
            s2 = grid.get_relative(cur, d2)
            if not s2 or s2.value not in [".", "E"]:
                continue

            new_time = dist + 2 + end_distances[s2.id]
            saved = end_distances[start.id] - new_time

            if saved < 0:
                continue

            cheats[saved] += 1

        for n in grid.cardinal_cells(cur):
            if n.id not in distances and n.value != "#":
                q.append((dist + 1, n))

    return cheats


start = grid.find("S")
end = grid.find("E")

end_distances = bfs(end)
print(end_distances[start.id])


total = 0

cheats = bfs_skip(start, end_distances)
for k, v in sorted(cheats.items()):
    print(v, k)
    if k >= 100:
        total += v

print(total)
