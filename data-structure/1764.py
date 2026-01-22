# 듣보잡 (https://www.acmicpc.net/problem/1764)
# tier: Silver 4
# tags: Data Structure, String, Sort, Set and Map, Hash

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

unseen = {input() for _ in range(n)}
unheard = {input() for _ in range(m)}
answer = sorted(list(unseen & unheard))

print(len(answer))
print("".join(answer))