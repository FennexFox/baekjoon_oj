# N과 M (4) (https://www.acmicpc.net/problem/1197)
# tier: Silver 3
# tags: Backtracking

import sys
print = sys.stdout.write

n, m = map(int, input().split())
path = []

def dfs(start):
    if len(path) == m:
        print(" ".join(map(str, path)) + "\n")
        return
    else:
        for x in range(start, n+1):
            path.append(x)
            dfs(x)
            path.pop()

dfs(1)