import sys
import re
import numpy as np

machines = []
with open(sys.argv[1]) as f:
    while True:
        try:
            ax, ay = re.match("Button A: X\+(\d+), Y\+(\d+)", f.readline()).groups()
            bx, by = re.match("Button B: X\+(\d+), Y\+(\d+)", f.readline()).groups()
            px, py = re.match("Prize: X=(\d+), Y=(\d+)", f.readline()).groups()
            f.readline()
            machines.append(map(int, [ax, ay, bx, by, px, py]))
        except AttributeError:
            break


def solve(m):
    ax, ay, bx, by, px, py = m
    px = px + 10000000000000
    py = py + 10000000000000
    a = np.array([[ax, bx], [ay, by]]).astype(int)
    b = np.array([px, py]).astype(int)
    s = np.linalg.solve(a, b)

    if np.all(np.abs(s - np.round(s)) < 1e-3):
        return s[0] * 3 + s[1]
    return 0


tokens = 0

for m in machines:
    tokens += solve(m)

print("TOKENS", tokens)
