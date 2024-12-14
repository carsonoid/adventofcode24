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

print(robots)

for r in robots:
    move(r, 100)

print(robots)

xmid = int(width / 2)
ymid = int(height / 2)
quads = {1: 0, 2: 0, 3: 0, 4: 0}
for r in robots:
    if r.x < xmid and r.y < ymid:
        quads[1] += 1
    elif r.x > xmid and r.y < ymid:
        quads[2] += 1
    elif r.x < xmid and r.y > ymid:
        quads[3] += 1
    elif r.x > xmid and r.y > ymid:
        quads[4] += 1

print(quads)
print(quads[1] * quads[2] * quads[3] * quads[4])
