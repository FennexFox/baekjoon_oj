# 스티커 (https://www.acmicpc.net/problem/9465)
# tier: Silver 1
# tags: Dynamic Programming

import sys
input = sys.stdin.readline
print = sys.stdout.write

tests = int(input())
out = []

for _ in range(tests):
    columns = int(input())
    stickers_0, stickers_1 = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0, 0], [0, 0]]
    
    for column in range(columns):
        dp = [
            dp[1],
            [
                max(dp[1][1], dp[0][1]) + stickers_0[column],
                max(dp[1][0], dp[0][0]) + stickers_1[column]
            ],
        ]
    
    out.append(str(max(dp[1])))

print("\n".join(out))