# N과 M (12) (https://www.acmicpc.net/problem/15666)
# tier: Silver 2
# tags: Backtracking

import sys
print = sys.stdout.write

_, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))
path = [0] * m

def dfs(depth, start):
    if depth == m:
        print(" ".join(map(str, path)) + "\n")
        return
    for i in range(start, len(nums)):
        path[depth] = nums[i]
        dfs(depth + 1, i)

dfs(0, 0)