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


printed = []


def do_cheat(
    start: Cell,
    search_start: Cell,
    start_dist: int,
    rem_dist: int,
    cheats: dict,
    cheat_dur: int,
    end_distances: dict,
):
    q = deque()
    q.append((0, search_start, cheat_dur))
    distances = defaultdict(lambda: float("inf"))

    while q:
        dist, cur, cheat_dur = q.popleft()

        # skip walls at the edges
        if (
            cur.x == grid.minX
            or cur.x == grid.maxX
            or cur.y == grid.minY
            or cur.y == grid.maxY
        ):
            continue

        distances[cur.id] = dist

        if cheat_dur == 0:
            return

        if cur.value in [".", "E"]:
            new_time = start_dist + dist + end_distances[cur.id]
            saved = rem_dist - new_time

            if saved == 74:  # TESTING
                id = start.id + cur.id
                if id not in printed:
                    printgrid = Grid(filepath=sys.argv[1])
                    # print(start_dist, dist, cheat_dur, saved)
                    print(
                        f"start_dist: {start_dist}, dist: {dist}, cheat_dur: {cheat_dur}, saved: {saved}"
                    )
                    printgrid.set_at(search_start.x, search_start.y, "1")
                    printgrid.set_at(cur.x, cur.y, "2")
                    printgrid.print()
                    printed.append(id)

            if saved > 0:
                cheats[saved].add(start.id + cur.id)

            continue

        for n in grid.cardinal_cells(cur):
            if n.id not in distances:
                q.append((dist + 1, n, cheat_dur - 1))


def bfs_for_cheats(start: Cell, cheat_dur: int, end_distances: dict):
    q = deque()
    q.append((0, start))
    distances = defaultdict(lambda: float("inf"))
    cheats = defaultdict(set)

    while q:
        dist, cur = q.popleft()
        distances[cur.id] = dist

        for n in grid.cardinal_cells(cur):
            if n.value == "#":
                do_cheat(
                    cur,
                    n,
                    dist + 1,
                    end_distances[start.id],
                    cheats,
                    cheat_dur,
                    end_distances,
                )

            if n.id not in distances and n.value != "#":
                q.append((dist + 1, n))

    return cheats


start = grid.find("S")
end = grid.find("E")

end_distances = bfs(end)
print(end_distances[start.id])


cheats = bfs_for_cheats(start, 20, end_distances)

print(cheats[74])

cuts_by_saved = defaultdict(int)
for saved, cuts in cheats.items():
    cuts_by_saved[saved] = len(cuts)

for saved, num in sorted(cuts_by_saved.items()):
    if saved >= 50:
        print(f"There are {num} cheats that save {saved} picoseconds")
