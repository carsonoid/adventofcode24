import sys
import collections

with open(sys.argv[1]) as input:
    parts = input.read().split("\n\n")
    updates = [x.split(",") for x in parts[1].split()]

    page_map = collections.defaultdict(list)
    for p in [x.split("|") for x in parts[0].split()]:
        page_map[p[1]].append(p[0])

print(page_map)
print(updates)


def is_ordered(update: list) -> bool:
    seen = []
    for i, page in enumerate(update):
        if i == len(update) - 1:
            return True

        if update[i + 1] in page_map[page] and update[i + 1] not in seen:
            return False
        seen.append(page)


def get_middle(update: list) -> int:
    return int(update[len(update) // 2])


sum = 0
for update in updates:
    if is_ordered(update):
        sum += get_middle(update)
print(sum)
