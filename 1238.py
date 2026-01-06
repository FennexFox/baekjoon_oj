# 파티 (https://www.acmicpc.net/problem/1238)
# tier: Gold 3
# tags: Graph, Shortest Path, Dijkstra

import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

INF = 10 ** 6
n, m, x = map(int, input().split())
paths = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    paths[start].append([end, time])

def dijkstra(start, is_returning = False):
    p_queue = [(0, start)]
    visited, times = [False] * (n+1), [INF] * (n+1)
    times[start] = 0

    while p_queue:
        this = heapq.heappop(p_queue)
        this_node = this[1]
        
        if visited[this_node]:
            continue
        visited[this_node] = True
        
        for this_edge in paths[this_node]:
            next_node = this_edge[0]
            next_time = this_edge[1]
            if times[next_node] > times[this_node] + next_time:
                times[next_node] = times[this_node] + next_time
                heapq.heappush(p_queue, (times[next_node], next_node))
    
    if is_returning:
        return times[x]
    else:
        return times

times = dijkstra(x)

for start in range(1, n+1):
    if start == x:
        continue
    else:
        times[start] += dijkstra(start, True)

print(str(max(times[1:])))