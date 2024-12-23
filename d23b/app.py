import sys
import networkx as nx

graph = nx.Graph()
with open(sys.argv[1]) as f:
    for line in f.readlines():
        graph.add_edge(*line.strip().split("-"))


cliques = list(nx.enumerate_all_cliques(graph))
print(",".join(sorted(cliques[-1])))
