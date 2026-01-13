n = int(input())
dp = [1, 2, 4]

for _ in range(n):
    num = int(input())
    while len(dp)<num:
        dp.append(dp[-1] + dp[-2] + dp[-3])
    print(dp[num-1])