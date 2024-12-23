import sys

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
    if depth == 0:
        if node.name == name:
            matches.add(",".join(sorted(path)))
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

matches = set()
for name in nodes.keys():
    search(name, "", nodes[name], 3, [], matches)

for match in matches:
    print(match)

print(len(matches))

t_matches = set()
for match in matches:
    for c in match.split(","):
        if c.startswith("t"):
            t_matches.add(match)

print(t_matches)
print(len(t_matches))
