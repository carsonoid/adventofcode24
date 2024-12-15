import sys
from .gridlib.gridlib import Grid, DirNorth, DirEast, DirSouth, DirWest


def move_cell_h(cell, dir) -> bool:
    next = grid.get_relative(cell, dir)

    if next.value == "#":
        return False

    if next.value in ["[", "]"]:
        if not move_cell_h(next, dir):
            return False

    if next.value == ".":
        cell.value, next.value = next.value, cell.value
        return True
    else:
        raise Exception(f"Unexpected value {next.value}")


def can_move_box_v(cell, dir) -> bool:
    if cell.value == "[":
        left, right = cell, grid.get_relative(cell, DirEast)
    else:
        left, right = grid.get_relative(cell, DirWest), cell

    next_left, next_right = grid.get_relative(left, dir), grid.get_relative(right, dir)

    if next_left.value == "#" or next_right.value == "#":
        return False

    if next_left.value == "." and next_right.value == ".":
        return True

    if next_left.value in ["[", "]"]:
        if not can_move_box_v(next_left, dir):
            return False

    if next_right.value in ["[", "]"]:
        if not can_move_box_v(next_right, dir):
            return False

    return True

    raise Exception(f"Unexpected values {next_left.value}, {next_right.value}")


def move_box_v(cell, dir) -> bool:
    if not can_move_box_v(cell, dir):
        return False

    if cell.value == "[":
        left, right = cell, grid.get_relative(cell, DirEast)
    else:
        left, right = grid.get_relative(cell, DirWest), cell

    next_left, next_right = grid.get_relative(left, dir), grid.get_relative(right, dir)
    if next_left.value == "#" or next_right.value == "#":
        return False

    if next_left.value in ["[", "]"]:
        move_box_v(next_left, dir)

    if next_right.value in ["[", "]"]:
        move_box_v(next_right, dir)

    left.value, next_left.value = next_left.value, left.value
    right.value, next_right.value = next_right.value, right.value
    return True


def move_robot_v(cell, dir) -> bool:
    next = grid.get_relative(cell, dir)

    match next.value:
        case "#":
            return False
        case ".":
            cell.value, next.value = next.value, cell.value
            return True
        case "[" | "]":
            if move_box_v(next, dir):
                cell.value, next.value = next.value, cell.value
                return True
            return False
        case _:
            raise Exception(f"Unexpected value {next.value}")


dirs = {
    "^": DirNorth,
    "v": DirSouth,
    "<": DirWest,
    ">": DirEast,
}

with open(sys.argv[1]) as f:
    gridstr, movesstr = f.read().split("\n\n")

newgridstr = ""
for c in list(gridstr):
    match c:
        case "#":
            newgridstr += "##"
        case "O":
            newgridstr += "[]"
        case ".":
            newgridstr += ".."
        case "@":
            newgridstr += "@."
        case "\n":
            newgridstr += "\n"
        case _:
            raise Exception(f"Unexpected character {c}")

grid = Grid(s=newgridstr, default_factory=str)
grid.print()


for m in filter(lambda x: x != "\n", list(movesstr.strip())):
    pos = grid.find("@")
    if m in ["^", "v"]:
        move_robot_v(pos, dirs[m])
    else:
        move_cell_h(pos, dirs[m])

    # print(m)
    # grid.print()

grid.print()

total = 0
for cell in grid:
    if cell.value == "[":
        total += 100 * cell.y + cell.x

print(total)
