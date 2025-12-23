# N과 M (9) (https://www.acmicpc.net/problem/15663)
# tier: Silver 2
# tags: Backtracking

import sys
print = sys.stdout.write

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
nums = {i: num for i, num in enumerate(nums)}
path, visited = [], {i: False for i in range(n)}
answer, answer_map = [], dict()

def get_combs():
    if len(path) == m:
        out = " ".join(map(str, path))
        if not answer_map.get(out, False):
            answer.append(out)
            answer_map.update({out: True})
        return
    else:
        for i in nums:
            if not visited[i]:
                visited[i] = True
                path.append(nums[i])
                get_combs()
                visited[i] = False
                path.pop()

get_combs()

answer = "\n".join(answer)
print(answer)