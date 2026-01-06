# 웜홀 (https://www.acmicpc.net/problem/1865)
# tier: Gold 3
# tags: Graph, Shortest Path, Bellman-Ford

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
    for i in range(1, n+2):
        is_updated = False
        for edge in edges:
            this_node, that_node, time = edge
            if path[that_node] > path[this_node] + time:
                path[that_node] = path[this_node] + time
                is_updated = True
        
        if not is_updated:
            break
        elif is_updated and i == n+1:
            negative_cycle = True
    
    print("YES" if negative_cycle else "NO")