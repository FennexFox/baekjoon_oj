# 평범한 배낭 (https://www.acmicpc.net/problem/12865)
# tier: Gold 5
# tags: Dynamic Programming, Knapsack Problem

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w_and_v = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]

def kanpsack(n, k):
    if n < 1:
        return 0
    elif dp[n][k] != -1:
        return dp[n][k]
    else:
        w, v = w_and_v[n-1]
        to_add = (kanpsack(n-1, k-w) + v) if k-w >= 0 else 0
        not_to_add = kanpsack(n-1, k)
        value = max(to_add, not_to_add)
        dp[n][k] = value
        return value

print(kanpsack(n, k))