# N과 M (2) (https://www.acmicpc.net/problem/15650)
# tier: Silver 3
# tags: Backtracking

n, m = map(int, input().split())
m = min(m, n-m)
num = denom = 1

while m > 0:
    num *= n
    denom *= m
    n -= 1
    m -= 1

comb = num // denom



lists = [] * comb