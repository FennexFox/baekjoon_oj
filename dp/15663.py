# N과 M (9) (https://www.acmicpc.net/problem/15663)
# tier: Silver 2
# tags: Backtracking

import sys
print = sys.stdout.write

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
nums = {i: num for i, num in enumerate(nums)}
path, visited = [], {i: False for i in range(n)}
answer = []

def get_combs(depth):
    if depth == m:
        answer.append(" ".join(map(str, path)))
        return

    last = None
    for i in nums:
        if visited[i] or last == nums[i]:
            continue
    
        visited[i] = True
        last = nums[i]
        path.append(last)
        get_combs(depth + 1)
        visited[i] = False
        path.pop()

get_combs(0)
print("\n".join(answer))