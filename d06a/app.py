import sys
import collections

with open(sys.argv[1]) as input:
    grid = [list(x.strip()) for x in input.readlines()]


def print_grid(g):
    [print("".join(row)) for row in g]


def get(y, x):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return "O"
    return grid[y][x]


print_grid(grid)

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "^":
            pos = (y, x)

dir = "N"
dirs = ["N", "E", "S", "W"]
positions = collections.defaultdict(str)

while True:
    positions[str(pos)] = True

    if dir == "N":
        next = (pos[0] - 1, pos[1])
    if dir == "E":
        next = (pos[0], pos[1] + 1)
    if dir == "S":
        next = (pos[0] + 1, pos[1])
    if dir == "W":
        next = (pos[0], pos[1] - 1)

    c = get(*next)
    if c == "O":
        break

    if c == "#":
        dir = dirs[(dirs.index(dir) + 1) % 4]
    else:
        pos = next


print(len(positions.keys()))
