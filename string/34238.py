n, m = list(map(int, input().split()))
grid, count = [], 0

steps = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]

for _ in range(n):
    grid.append(input())

for i in range(n):
    for j in range(m):
        if grid[i][j] == "F":
            for o_x, o_y in steps:
                o_i, o_j = i + o_x, j + o_y
                if 0<=o_i<n and 0<=o_j<m and grid[o_i][o_j] == "O":
                    x_i, x_j = o_i + o_x, o_j + o_y
                    if 0<=x_i<n and 0<=x_j<m and grid[x_i][x_j] == "X":
                        count += 1

print(count)