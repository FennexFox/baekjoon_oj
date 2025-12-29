# 1로 만들기 (https://www.acmicpc.net/problem/1463)
# tier: Silver 3
# tags: Dynamic Programming

num = int(input())
dp = [0] * (num+1)

for i in range(2, num+1):
    to_compare = [dp[i-1]]
    if not i % 3:
        to_compare.append(dp[i//3])
    if not i % 2:
        to_compare.append(dp[i//2])
    dp[i] = min(to_compare) + 1

print(dp[num])