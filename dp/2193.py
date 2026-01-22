# 이친수 (https://www.acmicpc.net/problem/2193)
# tier: Silver 3
# tags: Dynamic Programming

digits = int(input())
dp = [0, 1]

for i in range(2, digits+1):
    last_zero, last_one = dp
    dp = [last_zero + last_one, last_zero]

print(sum(dp))