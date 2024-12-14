import sys
import re
from dataclasses import dataclass


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


width, height = int(sys.argv[2]), int(sys.argv[3])
print(f"width={width}, height={height}")


def move(robot, times):
    robot.x = (robot.x + (robot.dx * times)) % width
    robot.y = (robot.y + (robot.dy * times)) % height


robots = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        x, y, dx, dy = re.match(
            "p=([\d-]+),([\d-]+) v=([\d-]+),([\d-]+)", line
        ).groups()
        robots.append(Robot(int(x), int(y), int(dx), int(dy)))

seconds = 0


def move_all(times):
    for r in robots:
        move(r, times)
    global seconds
    seconds += times


move_all(171)
print(seconds)


while True:
    move_all(101)

    line = ""
    for y in range(height):
        for x in range(width):
            if any(r.x == x and r.y == y for r in robots):
                line += "#"
            else:
                line += "."
        line += "\n"

    print(f"seconds={seconds}")
    print(line)
