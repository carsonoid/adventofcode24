import sys


with open(sys.argv[1]) as input:
    equations = []
    for result, params in [list(x.strip().split(": ")) for x in input.readlines()]:
        equations.append((int(result), [int(x) for x in params.split(" ")]))

print(equations)

operators = ["*", "+"]


def solvable(want, x, remaining):
    y = remaining[0]

    if x > want:
        return False

    if len(remaining) == 1:
        if x * y == want:
            return True
        elif x + y == want:
            return True
        elif int(str(x) + str(y)) == want:
            return True
        else:
            return False
    else:
        if solvable(want, x * y, remaining[1:]):
            return True
        elif solvable(want, x + y, remaining[1:]):
            return True
        elif solvable(want, int(str(x) + str(y)), remaining[1:]):
            return True
        return False


sum = 0
for equation in equations:
    if solvable(equation[0], equation[1][0], equation[1][1:]):
        sum += equation[0]

print(sum)
