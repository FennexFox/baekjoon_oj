# N과 M (12) (https://www.acmicpc.net/problem/15666)
# tier: Silver 2
# tags: Backtracking

import sys
print = sys.stdout.write

_, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
path, answer = [], []

def dfs(depth):
    if depth == m:
        answer.append(" ".join(map(str, path)))
        return
    else:
        for num in nums:
            if path and num < path[-1]:
                continue
            path.append(num)
            dfs(depth+1)
            path.pop()

dfs(0)
print("\n".join(answer))