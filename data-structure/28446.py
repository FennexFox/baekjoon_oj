import sys
input = sys.stdin.readline
print = sys.stdout.write

m = int(input())
balls = dict()

for _ in range(m):
    temp = list(input().split())
    if temp[0] == "1":
        balls[temp[2]] = temp[1]
    elif temp[0] == "2":
        print(balls[temp[1]]+"\n")