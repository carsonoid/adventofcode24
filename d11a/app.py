import sys
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


cur = data
for i in range(25):
    next = []
    # print(" ".join(cur))
    for x in cur:
        next.extend(split(x))
    cur = next

# print(" ".join(cur))
print(len(cur))
