# 회의실 배정 (https://www.acmicpc.net/problem/1931)
# tier: Gold 5
# tags: Greedy, Sort

import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times = sorted(times, key=lambda x: (x[1], x[0]))

prev, answer = [0, 0], 0
for time in times:
    if time[0] >= prev[1]:
        answer += 1
        prev = time

print(answer)