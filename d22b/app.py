import sys
import math
from collections import deque, defaultdict


def predict(x, times):
    for _ in range(times):
        x = ((x * 64) ^ x) % 16777216
        x = (math.floor(x / 32) ^ x) % 16777216
        x = ((x * 2048) ^ x) % 16777216
    return x


def get_price_diff(before, after):
    b1 = before % 10
    a1 = after % 10
    return a1 - b1


def set_seq_prices(x, sequence_prices):
    init = x
    last_four = deque([], maxlen=4)
    for _ in range(2_000):
        before = x
        x = predict(x, 1)

        diff = get_price_diff(before, x)
        last_four.append(str(diff))
        if len(last_four) == 4:
            if not sequence_prices[(",".join(last_four))][init]:
                sequence_prices[(",".join(last_four))][init] = x % 10


with open(sys.argv[1]) as f:
    buyers = [int(x) for x in f.read().strip().split("\n")]

sequence_prices = defaultdict(lambda: defaultdict(int))
for buyer in buyers:
    set_seq_prices(buyer, sequence_prices)

best = 0
for num_buyers in reversed(range(len(buyers))):
    for seq, possible_buyers in sequence_prices.items():
        if len(possible_buyers.keys()) == num_buyers:
            price = 0
            for buyer in buyers:
                price += possible_buyers[buyer]
            if price > best:
                best = price
print(best)
