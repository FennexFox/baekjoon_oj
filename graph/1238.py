# 파티 (https://www.acmicpc.net/problem/1238)
# tier: Gold 3
# tags: Graph, Shortest Path, Dijkstra

import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

INF = 10 ** 6
n, m, x = map(int, input().split())
paths = [[] for _ in range(n+1)]
reverse_paths = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    paths[start].append([end, time])
    reverse_paths[end].append([start, time])

def dijkstra(graph):
    p_queue = [(0, x)]
    visited, times = [False] * (n+1), [INF] * (n+1)
    times[x] = 0

    while p_queue:
        this = heapq.heappop(p_queue)
        this_node = this[1]
        
        if visited[this_node]:
            continue
        visited[this_node] = True
        
        for this_edge in graph[this_node]:
            next_node = this_edge[0]
            next_time = this_edge[1]
            if times[next_node] > times[this_node] + next_time:
                times[next_node] = times[this_node] + next_time
                heapq.heappush(p_queue, (times[next_node], next_node))
    
    return times

times = [x+y for x, y in zip(dijkstra(paths)[1:], dijkstra(reverse_paths)[1:])]

print(str(max(times)))