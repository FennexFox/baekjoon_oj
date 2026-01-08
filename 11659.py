import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0]

for num in nums:
    dp.append(dp[-1]+num)

for _ in range(m):
    i, j = map(int, input().split())
    print(f"{dp[j]-dp[i-1]}\n")