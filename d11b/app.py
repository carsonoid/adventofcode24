import sys
import collections
from functools import cache

with open(sys.argv[1]) as f:
    data = [x for x in f.readline().strip().split()]


@cache
def split(s):
    if s == "0":
        return ["1"]
    elif len(s) % 2 == 0:
        mid = int(len(s) / 2)
        return [s[:mid], str(int(s[mid:]))]
    else:
        return [str(int(s) * 2024)]


stones = collections.defaultdict(int)

for stone in data:
    stones[stone] = 1

cur = stones
for i in range(75):
    next = collections.defaultdict(int)
    for stone, count in cur.items():
        for new_stone in split(stone):
            next[new_stone] += count
    cur = next

total = 0
for stone, count in cur.items():
    total += count

print(total)
