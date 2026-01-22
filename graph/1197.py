# 최소 스패닝 트리 (https://www.acmicpc.net/problem/1197)
# tier: Gold 2
# tags: Graph, Minimum Spanning Tree

import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, e = map(int, input().split())
edges = []
nodes = [n for n in range(n+1)]

for _ in range(e):
    node1, node2, weight = map(int, input().split())
    heapq.heappush(edges, [weight, node1, node2])

def union(node1, node2):
    p1, p2 = find(node1), find(node2)
    if p1 != p2:
        nodes[p2] = p1
        return True

def find(node):
    if node == nodes[node]:
        return node
    else:
        nodes[node] = find(nodes[node])
        return nodes[node]

visited, answer = 0, 0

while visited < n - 1:
    weight, node1, node2 = heapq.heappop(edges)
    if union(node1, node2):
        visited += 1
        answer += weight

print(answer)
    