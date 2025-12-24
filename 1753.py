# 최단경로 (https://www.acmicpc.net/problem/1753)
# tier: Gold 4
# tags: Graph, Shortest Path, Dijkstra

import sys, heapq

input = sys.stdin.readline
print = sys.stdout.write

nodes, edges = map(int, input().split())
root = int(input())
visited = [False] * (nodes + 1)
shortest = [float("inf")] * (nodes + 1)
adj_list = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    node1, node2, weight = map(int, input().split())
    adj_list[node1].append([node2, weight])

p_queue = [(0, root)]
shortest[root] = 0

while p_queue:
    this = heapq.heappop(p_queue)
    this_node = this[1]
    
    if visited[this_node]:
        continue
    visited[this_node] = True

    for this_edge in adj_list[this_node]:
        next_node = this_edge[0]
        edge_length = this_edge[1]
        if shortest[next_node] > shortest[this_node] + edge_length:
            shortest[next_node] = shortest[this_node] + edge_length
            heapq.heappush(p_queue, (shortest[next_node], next_node))

out = ""
for i in range(1, nodes+1):
    if visited[i]:
        out += f"{str(shortest[i])}\n"
    else:
        out += "INF\n"
print(out)