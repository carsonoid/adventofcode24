from typing import TypeAlias

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


class Cell:
    id = ""
    x = 0
    y = 0
    value = ""

    def __init__(self, x: int, y: int, value: str) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.id = f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y}) {self.value}"


class Grid:
    def __init__(
        self,
        rows: list[list[Cell]] = None,
        filepath: str = None,
        s: str = None,
        default_factory=str,
    ) -> None:
        self.rows = []
        if rows:
            self.rows = rows
        elif filepath:
            with open(filepath) as input:
                y = 0
                for row in input.readlines():
                    row = row.strip()
                    self.rows.append([Cell(x, y, value) for x, value in enumerate(row)])
                    y += 1
        elif s:
            y = 0
            for row in s.split("\n"):
                row = row.strip()
                self.rows.append([Cell(x, y, value) for x, value in enumerate(row)])
                y += 1

    def print(self) -> None:
        for row in self.rows:
            print("".join(str(c.value) for c in row))

    def in_bounds(self, c: Cell):
        return 0 <= c.x < len(self.rows[0]) and 0 <= c.y < len(self.rows)

    def coord_in_bounds(self, x: int, y: int):
        return 0 <= x < len(self.rows[0]) and 0 <= y < len(self.rows)

    def get_at(self, x: int, y: int, dir: Direction = None) -> Cell:
        if dir:
            dx, dy = dir
            x, y = x + dx, y + dy
        if self.coord_in_bounds(x, y):
            return self.rows[y][x]
        else:
            return None

    def set_at(self, x: int, y: int, value: str) -> None:
        if self.coord_in_bounds(x, y):
            self.rows[y][x] = value

    def get_relative(self, c: Cell, dir: Direction) -> Cell:
        return self.get_at(c.x, c.y, dir)

    # make it so we can "for" loop over the class by looping the cells
    def __iter__(self):
        for y, row in enumerate(self.rows):
            for x, v in enumerate(row):
                yield self.rows[y][x]

    def find(self, s):
        for cell in self:
            if cell.value == s:
                return cell
        raise Exception("Not found")

    def cardinal_cells(self, c: Cell) -> list[Cell]:
        return list(filter(lambda x: x.value, self.all_cardinal_cells(c)))

    def all_cardinal_cells(self, c: Cell) -> list[Cell]:
        cells = []
        for dx, dy in [
            DirNorth,
            DirSouth,
            DirEast,
            DirWest,
        ]:
            nx, ny = c.x + dx, c.y + dy
            if self.coord_in_bounds(nx, ny):
                cells.append(self.rows[ny][nx])
            else:
                cells.append(Cell(nx, ny, None))
        return cells

    def adjacent_cells(self, c: Cell) -> list[Cell]:
        cells = []
        for dx, dy in [
            DirNorth,
            DirEast,
            DirSouth,
            DirWest,
        ]:
            nx, ny = c.x + dx, c.y + dy
            new_cell = (nx, ny, self.rows[ny][nx])
            if self.in_bounds(new_cell):
                cells.append(new_cell)
        return cells
