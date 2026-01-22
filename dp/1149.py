# RGB거리 (https://www.acmicpc.net/problem/1149)
# tier: Silver 1
# tags: Dynamic Programming

length = int(input())
dp = list(map(int, input().split()))

for i in range(length-1):
    costs = list(map(int, input().split()))
    dp_prev = dp.copy()
    for j in range(3):
        dp[j] = costs[j] + min(dp_prev[(j+1)%3], dp_prev[(j+2)%3])

print(min(dp))