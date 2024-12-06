import sys

dirs = [
    [-1, -1],  # NW
    [-1, 0],  # N
    [-1, 1],  # NE
    [0, -1],  # W
    [0, 1],  # E
    [1, -1],  # SW
    [1, 0],  # S
    [1, 1],  # SE
]


with open(sys.argv[1]) as input:
    grid = [list(x.strip()) for x in input.readlines()]

[print(row) for row in grid]


def search(
    y: int, x: int, grid: list[list[str]], word: list[str], dirs: list[list[int]]
) -> int:
    if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1:
        return 0

    c = grid[y][x]

    if c != word[0]:
        return 0

    sum = 0
    for d in dirs:
        if grid[y][x] == word[0]:
            if len(word) == 1:
                return True
            elif search(d[0] + y, d[1] + x, grid, word[1:], [d]):
                sum += 1
    return sum


sum = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        sum += search(y, x, grid, list("XMAS"), dirs)

print("SUM", sum)
