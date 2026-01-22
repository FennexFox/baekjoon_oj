# N과 M (5) (https://www.acmicpc.net/problem/15654)
# tier: Silver 3
# tags: Backtracking

import sys
print = sys.stdout.write

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
path, visited = [], {num: False for num in nums}

def dfs():
    if len(path) == m:
        out = " ".join(map(str, path)) + "\n"
        print(out)
        return
    for num in nums:
        if not visited[num]:
            path.append(num)
            visited[num] = True
            dfs()
            path.pop()
            visited[num] = False

dfs()