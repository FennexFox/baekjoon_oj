max_x = max_y = -(10**5)
min_x = min_y = 10**5

for _ in range(int(input())):
    x, y = map(int, input().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

print((max_x - min_x) * (max_y - min_y))