# 웜홀 (https://www.acmicpc.net/problem/1865)
# tier: Gold 3
# tags: Graph, Shortest Path, Bellman-Ford
import sys
input = sys.stdin.readline
print = sys.stdout.write

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())

    edges = []
    path = [0] * (n+1)

    for edge in range(m):
        start, end, time = map(int, input().split())
        edges.append((start, end, time))
        edges.append((end, start, time))
    for wormhole in range(w):
        start, end, time = map(int, input().split())
        edges.append((start, end, -time))
    
    negative_cycle = False
    for i in range(1, n+1):
        is_updated = False
        for edge in edges:
            this_node, that_node, time = edge
            if path[that_node] > path[this_node] + time:
                path[that_node] = path[this_node] + time
                is_updated = True
        
        if not is_updated:
            break
        elif is_updated and i == n:
            negative_cycle = True
    
    print("YES\n" if negative_cycle else "NO\n")