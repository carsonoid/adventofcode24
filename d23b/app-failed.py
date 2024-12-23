import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    links = [tuple(x.strip().split("-")) for x in f.readlines()]

print(links)


class Node:
    name: str
    edges: list

    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, node):
        self.edges.append(node)

    def __str__(self):
        return f"{self.name} <-> {','.join([x.name for x in self.edges])}"


def search(name, prev, node, depth, path, matches):
    print(depth, node)
    if depth == 0:
        if node.name == name:
            key = ",".join(sorted(path))
            matches[key] += 1
        return

    path.append(node.name)

    for edge in node.edges:
        if edge.name != prev:
            search(name, node.name, edge, depth - 1, path.copy(), matches)

    return matches


nodes = {}

for x, y in links:
    if x not in nodes:
        nodes[x] = Node(x)
    if y not in nodes:
        nodes[y] = Node(y)

    nodes[x].add_edge(nodes[y])
    nodes[y].add_edge(nodes[x])

connectionlen = len(list(nodes.values())[0].edges)
print(connectionlen)

i = 0
num = len(nodes)
matches = defaultdict(int)
for name in nodes.keys():
    i += 1
    print(f"{i}/{num}")
    search(name, "", nodes[name], connectionlen, [], matches)

print(matches)

max = 0
maxval = ""
for k, v in matches.items():
    if v > max:
        max = v
        maxval = k

print(maxval)
