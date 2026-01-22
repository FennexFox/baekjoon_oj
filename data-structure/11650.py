import sys
input = sys.stdin.readline
print = sys.stdout.write

coords = [list(map(int, input().split())) for _ in range(int(input()))]
coords.sort(key=lambda x: (x[0], x[1]))

for coord in coords:
    print(" ".join(map(str, coord))+"\n")