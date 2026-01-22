# 가장 긴 증가하는 부분 수열 (https://www.acmicpc.net/problem/11053)
# Silver 2
# Dynamic Programming, Longest Increasing Subsequence

array_len = int(input())
array = [int(i) for i in input().split()]
dp = [1] * array_len

for i in range(array_len):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))