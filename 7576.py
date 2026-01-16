# 토마토 (https://www.acmicpc.net/problem/7576)
# tier: Gold 5
# tags: Graph, Grid, BFS, Shortest Path

from collections import deque
import sys
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

w, h = map(int, input().split())
tomatoes, rippen = [], deque([])
max_days = 0

for y in range(h):
    row = list(map(int, input().split()))
    for x, cell in enumerate(row):
        if cell == 1:
            rippen.append(((x, y), 0))
    tomatoes.append(row)

while rippen:
    (rippen_x, rippen_y), days = rippen.popleft()
    for dir_x, dir_y in directions:
        that_x = rippen_x + dir_x
        that_y = rippen_y+ dir_y
        if 0<=that_x<w and 0<=that_y<h and not tomatoes[that_y][that_x]:
            max_days = days+1
            rippen.append(((that_x, that_y), max_days))
            tomatoes[that_y][that_x] = -1

for row in tomatoes:
    if 0 in row:
        max_days = -1
        break

print(max_days)