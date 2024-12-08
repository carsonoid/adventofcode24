from typing import TypeVar, TypeAlias

# x, y
Direction: TypeAlias = tuple[int, int]

DirNorth: Direction = (0, -1)
DirNorthEast: Direction = (1, -1)
DirEast: Direction = (1, 0)
DirSouthEast: Direction = (1, 1)
DirSouth: Direction = (0, 1)
DirSouthWest: Direction = (-1, 1)
DirWest: Direction = (-1, 0)
DirNorthWest: Direction = (-1, -1)

CardinalDirections = [
    DirNorth,
    DirEast,
    DirSouth,
    DirWest,
]

AdjacentDirections = [
    DirNorth,
    DirEast,
    DirSouth,
    DirWest,
    DirNorthEast,
    DirSouthEast,
    DirSouthWest,
    DirNorthWest,
]

# x, y, value
Cell: TypeAlias = tuple[int, int, str]

U = TypeVar("U")


class Grid:
    rows = []

    def __init__(
        self, rows: list[list[U]] = None, filepath: str = None, s: str = None
    ) -> None:
        if rows:
            self.rows = rows
        elif filepath:
            with open(filepath) as input:
                self.rows = [[x for x in row.strip()] for row in input.readlines()]
        elif s:
            self.rows = [[x for x in row.split()] for row in s.split("\n")]

    def print(self) -> None:
        for row in self.rows:
            print("".join(str(x) for x in row))

    def in_bounds(self, c: Cell):
        x, y, _ = c
        return 0 <= x < len(self.rows[0]) and 0 <= y < len(self.rows)

    def get_at(self, x: int, y: int, dir: Direction = None) -> Cell:
        if dir:
            dx, dy = dir
            x, y = x + dx, y + dy
        if self.in_bounds((x, y, "")):
            return (x, y, self.rows[y][x])
        else:
            return None

    def set_at(self, x: int, y: int, value: str) -> None:
        if self.in_bounds((x, y, "")):
            self.rows[y][x] = value

    def get_relative(self, c: Cell, dir: Direction) -> Cell:
        return self.get_at(c[0], c[1], dir)

    # make it so we can "for" loop over the class by looping the cells
    def __iter__(self):
        for y, row in enumerate(self.rows):
            for x, cell in enumerate(row):
                yield (x, y, cell)

    def find(self, s):
        for cell in self:
            if cell[2] == s:
                return cell
        raise Exception("Not found")

    def cardinal_cells(self, c: Cell) -> list[Cell]:
        cells = []
        x, y, _ = c
        for dx, dy in [
            DirNorth,
            DirEast,
            DirSouth,
            DirWest,
        ]:
            nx, ny = x + dx, y + dy
            new_cell = (nx, ny, self.rows[ny][nx])
            if self.in_bounds(new_cell):
                cells.append(new_cell)
        return cells

    def adjacent_cells(self, c: Cell) -> list[Cell]:
        cells = []
        x, y, _ = c
        for dx, dy in [
            DirNorth,
            DirEast,
            DirSouth,
            DirWest,
        ]:
            nx, ny = x + dx, y + dy
            new_cell = (nx, ny, self.rows[ny][nx])
            if self.in_bounds(new_cell):
                cells.append(new_cell)
        return cells
