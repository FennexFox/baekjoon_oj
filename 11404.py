# 플로이드 (https://www.acmicpc.net/problem/11404)
# tier: Gold 4
# tags: Graph, Shortest Path, Floyd-Warshall

import sys
input = sys.stdin.readline
print = sys.stdout.write

INF = 10**15
city_num = int(input()) + 1
bus_num = int(input())

fares = [[INF] * (city_num) for _ in range(city_num)]
for i in range(1, city_num):
    fares[i][i] = 0

for _ in range(bus_num):
    start, end, fare = map(int, input().split())
    if fares[start][end] > fare:
        fares[start][end] = fare

for m in range(1, city_num):
    row_m = fares[m]
    for i in range(1, city_num):
        row_i = fares[i]
        fare_im = row_i[m]
        if fare_im == INF:
            continue
        for j in range(1, city_num):
            fare_mj = row_m[j]
            if fare_mj == INF:
                continue
            fare_ij = row_i[j]
            fare_imj = fare_im + fare_mj
            if fare_ij > fare_imj:
                row_i[j] = fare_imj

out_lines = []
for i in range(1, city_num):
    row_i = fares[i]
    out_lines.append(" ".join("0" if row_i[j] == INF else str(row_i[j]) for j in range(1, city_num)))

print("\n".join(out_lines))