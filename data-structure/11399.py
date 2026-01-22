# ATM (https://www.acmicpc.net/problem/11399)
# tier: Silver 4
# tags: Greedy, Sort

len = int(input())
array = list(map(int, input().split())) + [float("inf")]
time = 0

for j in range(len):
    for i in range(j):
        if array[i] < array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

array = array[:-1]

for i, t in enumerate(array):
    time += (i+1) * t

print(time)