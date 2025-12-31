# 숨바꼭질 3 (https://www.acmicpc.net/problem/13549)
# tier: Gold 5
# tags: Graph, Shortest Path, BPS, 0-1 BPS, Dijkstra

from collections import deque

INF, MAX = 10**9, 10**5
n, k = map(int, input().split())
count = [INF] * 100001
count[n] = 0
q = deque([n])

if n >= k:
    print(n-k)
else:
    while q:
        node = q.popleft()
        steps = count[node]

        if node == k:
            print(count[node])
            break

        teleport = 2*node if 0<=node and node<=MAX//2 else 0
        if teleport and count[teleport] > steps:
            q.appendleft(teleport)
            count[teleport] = steps

        for step in (node-1, node+1):
            if 0<=step and step<=MAX and count[step] > steps+1:
                q.append(step)
                count[step] = steps+1