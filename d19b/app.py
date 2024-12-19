import sys
from functools import cache

with open(sys.argv[1]) as f:
    towels, patterns = f.read().split("\n\n")
    towels = towels.strip().split(", ")
    patterns = patterns.split()

print(towels)
print(patterns)


@cache
def solve(pat: str) -> int:
    if not pat:
        return 1

    tot = 0
    for t in towels:
        if pat.startswith(t):
            tot += solve(pat.removeprefix(t))

    return tot


total = 0
for pat in patterns:
    tot = solve(pat)
    print(f"{pat}: {tot}")
    total += tot

print(total)
