# N-Quen (https://www.acmicpc.net/problem/9663)
# tier: Gold 3
# tags: Graph, BFS 

from collections import deque

n, m = map(int, input().split())
start, maze = (0,0), []

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distances = [[-1 for _ in range(m)] for _ in range(n)]
max_d = -1

for _ in range(n):
    maze.append(input())
    
def bfs(start, map, directions, distances):
    dist = distances
    dist[start[1]][start[0]] = max_distance = 1
    farthest_nodes = [(start)]

    q = deque([start])
    while q:
        this_x, this_y = q.popleft()
        
        for x, y in directions:
            that_x, that_y = this_x + x, this_y + y
            
            if not (0<=that_x<m and 0<=that_y<n):
                continue
            if dist[that_y][that_x] == -1 and map[that_y][that_x] == "0":
                that_distance = dist[this_y][this_x] + 1
                if that_distance > max_distance:
                    farthest_nodes = []
                    max_distance = that_distance
                farthest_nodes.append((that_x, that_y))
                dist[that_y][that_x] = that_distance
                q.append((that_x, that_y))

    return dist, max_distance, farthest_nodes

distances, f_dist, f_nodes = bfs((0,0), maze, steps, distances)
f_nodes = deque(f_nodes)

if distances[n-1][m-1] != -1:
    max_d = distances[n-1][m-1]
else:
    for f_node in f_nodes:
        f_x, f_y = f_node
        candid = []
        for x, y in steps:
            new_x, new_y = f_x + x, f_y + y
            if 0<=new_x<m and 0<=new_y<n and distances[new_y][new_x] == -1:
                new_dists, _, _ = bfs((new_x,new_y), maze, steps, distances)
                if new_dists[n-1][m-1] != -1:
                    candid.append(new_dists[n-1][m-1])
        if candid:
            max_d = f_dist + min(candid)

print(max_d)