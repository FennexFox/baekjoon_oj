# 주사위 (https://www.acmicpc.net/problem/1041)
# tier: Gold 5
# tags: Math, Implementation, Greedy
opp_pairs = [(0,5), (1,4), (2,3)]

n = int(input())
dice = list(map(int, input().split()))

mins = [min(dice[a], dice[b]) for a, b in opp_pairs]
min3 = sum(mins)
min2 = min3 - max(mins)
min1 = min(mins)

if n == 1:
    print(sum(dice) - max(dice))
else:
    print(min1*(5*n**2 - 16*n + 12) + min2*(8*n-12) + min3*4)