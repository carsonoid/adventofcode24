import sys
import collections


def print_grid(g):
    [print("".join(row)) for row in g]


def get(g, y, x):
    if y < 0 or y >= len(g) or x < 0 or x >= len(g[0]):
        return "O"
    return g[y][x]


def duplicate(grid):
    return [row.copy() for row in grid]


def solve(g):
    # print("SOLVING")
    # print_grid(g)

    pdirs = collections.defaultdict(str)

    for y, row in enumerate(g):
        for x, c in enumerate(row):
            if c == "^":
                pos = (y, x)

    dir = "N"
    dirs = ["N", "E", "S", "W"]
    positions = collections.defaultdict(str)

    while True:
        positions[str(pos)] = True

        pdir = str(pos) + dir
        if pdir in pdirs:
            return None
        pdirs[str(pos) + dir] = dir

        if dir == "N":
            next = (pos[0] - 1, pos[1])
        if dir == "E":
            next = (pos[0], pos[1] + 1)
        if dir == "S":
            next = (pos[0] + 1, pos[1])
        if dir == "W":
            next = (pos[0], pos[1] - 1)

        c = get(g, *next)
        if c == "O":
            break

        if c == "#":
            dir = dirs[(dirs.index(dir) + 1) % 4]
        else:
            pos = next

    return len(positions.keys())


with open(sys.argv[1]) as input:
    grid = [list(x.strip()) for x in input.readlines()]


print_grid(grid)
print()

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "^":
            start = (y, x)


sum = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        print(y, x)

        if (y, x) == start:
            continue

        test_grid = duplicate(grid)
        test_grid[y][x] = "#"

        steps = solve(test_grid)
        if not steps:
            sum += 1
print(sum)
