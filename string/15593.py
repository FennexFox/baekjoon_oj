n = int(input())
shifts = [list(map(int, input().split())) for _ in range(n)]

shifts = sorted(shifts, key=lambda x: (x[1], x[0]))
print(shifts)