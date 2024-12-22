import sys
import math
from functools import cache


@cache
def predict(x, times):
    for _ in range(times):
        x = ((x * 64) ^ x) % 16777216
        x = (math.floor(x / 32) ^ x) % 16777216
        x = ((x * 2048) ^ x) % 16777216
    return x


with open(sys.argv[1]) as f:
    buyers = [int(x) for x in f.read().strip().split("\n")]

tot = 0
for num in buyers:
    init_num = num
    num = predict(num, 2_000)
    tot += num
    print(f"{init_num} -> {num}")

print("Total: ", tot)
