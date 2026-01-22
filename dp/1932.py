# 정수 삼각형 (https://www.acmicpc.net/problem/1932)
# tier: Silver 1
# tags: Dynamic Programming

length = int(input())
dp = [0] * (length + 2)

for n in range(length):
    temp = list(map(int, input().split()))
    for i in range(n):
        temp[i] += max(dp[i], dp[i+1])
    dp[1:n+1] = temp

print(max(dp))