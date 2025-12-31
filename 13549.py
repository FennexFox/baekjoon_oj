# 숨바꼭질 3 (https://www.acmicpc.net/problem/13549)
# tier: Gold 5
# tags: Graph, Shortest Path, BPS, 0-1 BPS, Dijkstra

import heapq

INF = 10**6
n, k = map(int, input().split())
count = [INF] * 100001
q = [[0, n]]

while q:
    steps, node = heapq.heappop(q)
    if node == k:
        break
    if steps < count[node]:
        count[node] = steps
        next = [node-1, node+1]
        for step in next:
            if 0<=step and step<=100000 and count[step]:
                heapq.heappush(q, [steps+1, step])
        teleport = 2*node if 0<=node and node<=50000 else 0
        if teleport:
            heapq.heappush(q, [steps, teleport])
                

print(steps)