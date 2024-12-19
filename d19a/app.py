import sys
from functools import cache

with open(sys.argv[1]) as f:
    towels, patterns = f.read().split("\n\n")
    towels = towels.strip().split(", ")
    patterns = patterns.split()

print(towels)
print(patterns)


@cache
def solve(pat: str):
    if not pat:
        return True

    for t in towels:
        if pat.startswith(t):
            if solve(pat.removeprefix(t)):
                return True

    return False


total = 0
for pat in patterns:
    solvable = solve(pat)
    print(f"{pat}: {solvable}")
    if solvable:
        total += 1

print(total)
