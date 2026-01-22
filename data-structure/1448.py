import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tri = sorted([int(input()) for _ in range(n)])

while n > 2:
    if sum(tri[n-3:n]) <= 2*tri[n-1]:
        n -= 1
    else:
        break

print(sum(tri[n-3:n]) if sum(tri[n-3:n]) > 2*tri[n-1] else -1)