import sys
import re

with open(sys.argv[1]) as input:
    program = input.readlines()

expr = re.compile("(do\(\)|mul\((\d+),(\d+)\))")
expr = re.compile("(do\(\)|don't\(\)|mul\((\d+),(\d+)\))")

enabled = True
sum = 0
for line in program:
    for matched, x, y in expr.findall(line.strip()):
        print(matched, x, y)
        if matched.startswith("mul") and enabled:
            print(int(x), int(y))
            sum += int(x) * int(y)
        elif matched == "do()":
            enabled = True
        elif matched == "don't()":
            enabled = False

print("SUM:", sum)
