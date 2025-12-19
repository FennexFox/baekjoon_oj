# N과 M (5) (https://www.acmicpc.net/problem/15654)
# tier: Silver 3
# tags: Backtracking

import sys
print = sys.stdout.write

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
visited = []

def dfs(visited):
    if len(visited) == m:
        out = " ".join(map(str, visited)) + "\n"
        print(out)
        return
    for num in nums:
        if not num in visited:
            visited.append(num)
            dfs(visited)
            visited.pop()

dfs(visited)