# 플로이드 (https://www.acmicpc.net/problem/11404)
# tier: Gold 4
# tags: Graph, Shortest Path, Floyd-Warshall

import sys
input = sys.stdin.readline
print = sys.stdout.write

INF = 10**9 + 1
city_num = int(input()) + 1

fares = [[INF for _ in range(city_num)] for _ in range(city_num)]

for _ in range(int(input())):
    start, end, fare = map(int, input().split())
    fares[start][end] = min(fare, fares[start][end])

for k in range(1, city_num):
    for i in range(1, city_num):
        for j in range(1, city_num):
            if i != j and fares[i][j] > fares[i][k] + fares[k][j]:
                fares[i][j] = fares[i][k] + fares[k][j]

out = []
for row in range(1, city_num):
    out.append(" ".join(str(x).replace("1000000001", "0") for x in fares[row][1:]))

print("\n".join(out))