# 트리의 지름 (https://www.acmicpc.net/problem/1967)
# tier: Gold 4
# tags: Graph, Tree, DFS, BFS, Diameter of Tree

import sys
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, weight = map(int, input().split())
    edges[a].append((b, weight))
    edges[b].append((a, weight))
    
def dfs(start, edges):
    distances = [0 if i == start else -1 for i in range(n+1)]
    stack = [start]
    while stack:
        this_node = stack.pop()
        for that_node, weight in edges[this_node]:
            if distances[that_node] == -1:
                distances[that_node] = distances[this_node] + weight
                stack.append(that_node)
    return distances

def get_farthest(start, edges, n):
    distances = dfs(start, edges)
    
    far_node, far_dist = start, 0
    for i in range(n+1):
        if distances[i] > far_dist:
            far_node, far_dist = i, distances[i]
    
    return far_node, far_dist

a, _ = get_farthest(1, edges, n)
_, far_dist = get_farthest(a, edges, n)

print(far_dist)