import sys
import re

with open(sys.argv[1]) as input:
    program = input.readlines()

print(program)

expr = re.compile("mul\((\d+),(\d+)\)")

sum = 0
for line in program:
    for x, y in expr.findall(line.strip()):
        print(int(x), int(y))
        sum += int(x) * int(y)

print("SUM:", sum)
