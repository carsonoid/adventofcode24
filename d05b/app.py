import sys
import collections

with open(sys.argv[1]) as input:
    parts = input.read().split("\n\n")
    updates = [x.split(",") for x in parts[1].split()]

    page_map = collections.defaultdict(list)
    for p in [x.split("|") for x in parts[0].split()]:
        page_map[p[1]].append(p[0])

print(page_map)
for k, v in page_map.items():
    print(k, v)
print(updates)


def is_ordered(update: list) -> bool:
    seen = []
    for i, page in enumerate(update):
        if i == len(update) - 1:
            return True

        if update[i + 1] in page_map[page] and update[i + 1] not in seen:
            return False
        seen.append(page)


def can_append(page: str, remaining: list) -> bool:
    for before in page_map[page]:
        if before in remaining:
            return False

    return True


def get_middle_fixed(update: list) -> int:
    ret = []
    remaining = update.copy()
    middle = len(update) // 2
    while remaining:
        print(remaining)
        print("RET", ret)
        print(middle)
        remove = None
        for i, page in enumerate(remaining):
            if can_append(page, remaining):
                if len(ret) == middle:
                    return int(page)
                ret.append(page)
                remove = i
                break
        remaining.pop(remove)


sum = 0
for update in updates:
    if not is_ordered(update):
        sum += get_middle_fixed(update)
print(sum)
