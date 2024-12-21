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

    def __lt__(self, value: object) -> bool:
        if isinstance(value, Cell):
            return self.id < value.id
        return False

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Cell):
            return self.x == value.x and self.y == value.y
        return False


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
                    if not row:
                        continue
                    self.rows.append([Cell(x, y, value) for x, value in enumerate(row)])
                    y += 1
        elif s:
            y = 0
            for row in s.split("\n"):
                row = row.strip()
                if not row:
                    continue
                self.rows.append([Cell(x, y, value) for x, value in enumerate(row)])
                y += 1

        self.minX = 0
        self.minY = 0
        self.maxX = len(self.rows[0]) - 1
        self.maxY = len(self.rows) - 1

    def print(self) -> None:
        for row in self.rows:
            print("".join(str(c.value) for c in row))

    def man_dist(self, a: Cell, b: Cell) -> int:
        return abs(a.x - b.x) + abs(a.y - b.y)

    def in_bounds(self, c: Cell):
        return 0 <= c.x < len(self.rows[0]) and 0 <= c.y < len(self.rows)

    def coord_in_bounds(self, x: int, y: int):
        return 0 <= x < len(self.rows[0]) and 0 <= y < len(self.rows)

    def get_at(self, x: int, y: int) -> Cell:
        if not self.coord_in_bounds(x, y):
            return None

        try:
            return self.rows[y][x]
        except IndexError:
            return None
        except:
            raise

    def set_at(self, x: int, y: int, value: str) -> None:
        x, y = self._adjust_index(x, y)
        if self.coord_in_bounds(x, y):
            self.rows[y][x].value = value

    def get_relative(self, c: Cell, dir: Direction) -> Cell:
        dx, dy = dir
        x, y = c.x + dx, c.y + dy
        return self.get_at(x, y)

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
            if 0 <= nx < len(self.rows[0]) and 0 <= ny < len(self.rows):
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

    def _adjust_index(self, x: int, y: int) -> tuple[int, int]:
        if x < 0:
            x = len(self.rows[0]) + x
        if y < 0:
            y = len(self.rows) + y
        return x, y
