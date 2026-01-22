import sys
input = sys.stdin.readline
print = sys.stdout.write

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = int(input())

for _ in range(t):
    w, h, k = map(int, input().split())
    grid = [[0 for _ in range(w)] for _ in range(h)]
    cabbages, group_num = [], 0
    
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
        cabbages.append((x, y))

    while cabbages:
        start_x, start_y = cabbages.pop()
        if not(grid[start_y][start_x]):
            continue
        else:
            grid[start_y][start_x] = 0
        stack = [(start_x, start_y)]
        
        while stack:
            this_x, this_y = stack.pop()
            for direction_x, direction_y in directions:
                next_x = this_x + direction_x
                next_y = this_y + direction_y
                if 0<=next_x<w and 0<=next_y<h and grid[next_y][next_x]:
                    stack.append((next_x, next_y))
                    grid[next_y][next_x] = 0
        else:
            group_num += 1
    
    print(str(group_num)+"\n")