# 이항 계수 2 (https://www.acmicpc.net/problem/11501)
# tier: Silver 2
# tags: Math, Dynamic Programming, Combination

n, m = map(int, input().split())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][i] = 1
    dp[i][1] = i
    dp[i][0] = 1

for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%10007

print(dp[n][m])