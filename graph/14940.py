import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

h, w = map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

this_xy = (-1, -1)
dist = []
for y in range(h):
    grid_row = list(map(int, input().split()))
    dist_row = [-1 if v else 0 for v in grid_row]

    try:
        target_x = grid_row.index(2)
        dist_row[target_x] = 0
        this_xy = (target_x, y)
    except ValueError:
        pass

    dist.append(dist_row)

queue = deque([this_xy])
while queue:
    this_x, this_y = queue.popleft()
    this_dist = dist[this_y][this_x]
    for direction_x, direction_y in directions:
        coord_x = this_x+direction_x
        coord_y = this_y+direction_y
        if 0<=coord_x<w and 0<=coord_y<h and dist[coord_y][coord_x] == -1:
            dist[coord_y][coord_x] = this_dist + 1
            queue.append((coord_x, coord_y))

print("\n".join(" ".join(map(str, row)) for row in dist))