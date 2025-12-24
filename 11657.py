# 타임머신 (https://www.acmicpc.net/problem/11657)
# tier: Gold 4
# tags: Graph, Shortest Path, Bellman-Ford

import sys
input = sys.stdin.readline
print = sys.stdout.write

nodes, edges = map(int, input().split())
edge_list = []
path_list = [[0] + [float("inf")] * (nodes-1)]

for _ in range(edges):
    node1, node2, weight = map(int, input().split())
    edge_list.append([node1, node2, weight])

for n in range(nodes):
    last = path_list[-1].copy()
    for edge in edge_list:
        this_node, that_node, weight = edge
        if last[that_node-1] > last[this_node-1] + weight:
            last[that_node-1] = last[this_node-1] + weight
    path_list.append(last)

out = ""
if path_list[-1] == path_list[-2]:
    out = "\n".join(map(str, path_list[-1][1:])).replace("inf", "-1")
else:
    out = "-1"

print(out)