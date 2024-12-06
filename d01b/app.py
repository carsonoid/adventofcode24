import sys
import collections

list1 = []
counts = collections.defaultdict(int)
with open(sys.argv[1]) as input:
    for line in input.readlines():
        parts = line.strip().split()
        list1.append(int(parts[0]))
        counts[int(parts[1])] += 1

print(list1, counts)

sum = 0
for x in list1:
    sum += counts[x] * x

print(sum)
