import sys

corners1 = [
    [
        [-1, -1],  # NW
        [1, 1],  # SE
    ],
    [
        [1, 1],  # SE
        [-1, -1],  # NW
    ],
]

corners2 = [
    [
        [-1, 1],  # NE
        [1, -1],  # SW
    ],
    [
        [1, -1],  # SW
        [-1, 1],  # NE
    ],
]


with open(sys.argv[1]) as input:
    grid = [list(x.strip()) for x in input.readlines()]

# [print(row) for row in grid]


def show(y, x):
    print()
    print(
        grid[y + -1][x + -1],
        ".",
        grid[y + -1][x + 1],
        "\n",
        ".",
        grid[y + 0][x + 0],
        ".",
        "\n",
        grid[y + 1][x + -1],
        ".",
        grid[y + 1][x + 1],
        "\n",
        sep="",
    )


def check_corners(y: int, x: int, corners: list) -> bool:
    for pair in corners:
        p1, p2 = pair
        if grid[y + p1[0]][x + p1[1]] == "M" and grid[y + p2[0]][x + p2[1]] == "S":
            return True
    return False


def search(y: int, x: int) -> bool:
    if check_corners(y, x, corners1) and check_corners(y, x, corners2):
        show(y, x)
        return True
    return False


sum = 0
for y, row in enumerate(grid):
    if y == 0 or y == len(grid) - 1:
        continue
    for x, c in enumerate(row):
        if x == 0 or x == len(row) - 1 or c != "A":
            continue
        sum += search(y, x)

print("SUM", sum)
