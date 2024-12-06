import sys

list1 = []
list2 = []
with open(sys.argv[1]) as input:
    for line in input.readlines():
        parts = line.strip().split()
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

print(list1, list2)

list1.sort()
list2.sort()

sum = 0
for i, _ in enumerate(list1):
    sum += abs(list1[i] - list2[i])

print(sum)
