# ATM (https://www.acmicpc.net/problem/11399)
# tier: Silver 4
# tags: Greedy, Sort

length = int(input())
array = list(map(int, input().split()))
time = 0

for i, t in enumerate(sorted(array)):
    time += (length - i) * t

print(time)