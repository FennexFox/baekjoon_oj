import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

h, w = map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

this_xy = (0, 0)
grid, visited = [], []
for y in range(h):
    grid_row = list(map(int, input().split()))
    visited_row = [False for _ in range(w)]

    if 2 in grid_row:
        target_x = grid_row.index(2) if 2 in grid_row else -1
        this_xy = [target_x, y]
        visited_row[target_x] = True

    grid.append(grid_row)
    visited.append(visited_row)

dist = [[0 for _ in range(w)] for _ in range(h)]
queue = deque([this_xy])
while queue:
    this_node = queue.popleft()
    for direction in directions:
        coord = (min(max(this_node[0]+direction[0],0),w-1),
                min(max(this_node[1]+direction[1],0),h-1))
        if not visited[coord[1]][coord[0]] and grid[coord[1]][coord[0]]:
            visited[coord[1]][coord[0]] = True
            dist[coord[1]][coord[0]] = dist[this_node[1]][this_node[0]] + 1
            queue.append(coord)

for x in range(w):
    for y in range(h):
        if grid[y][x] == 1 and not dist[y][x]:
            dist[y][x] = -1

[print(" ".join(map(str, row))+"\n") for row in dist]