import sys
import re

machines = []
with open(sys.argv[1]) as f:
    while True:
        try:
            ax, ay = re.match("Button A: X\+(\d+), Y\+(\d+)", f.readline()).groups()
            bx, by = re.match("Button B: X\+(\d+), Y\+(\d+)", f.readline()).groups()
            px, py = re.match("Prize: X=(\d+), Y=(\d+)", f.readline()).groups()
            f.readline()
            machines.append(map(int, [ax, ay, bx, by, px, py]))
        except:
            break


def solve(m):
    ax, ay, bx, by, px, py = m
    b = 100
    while b >= 0:
        a = 0
        while a <= 100:
            if (bx * b) + (ax * a) == px and (by * b) + (ay * a) == py:
                print("matched", b)
                return a * 3 + b
            a += 1
        b -= 1
    return 0


tokens = 0

for m in machines:
    tokens += solve(m)

print("TOKENS", tokens)
