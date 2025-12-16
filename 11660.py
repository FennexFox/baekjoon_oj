# 구간 합 구하기 5 (https://www.acmicpc.net/problem/11660)
# Standard
# Dynamic Programming, Prefix Sum

table_size, query_count = map(int, input().split())
table_sum = [[0] * (table_size + 1) for _ in range(table_size + 1)]
result = []

for i in range(1, table_size + 1):
    row = list(map(int, input().split()))
    for j in range(1, table_size + 1):
        table_sum[i][j] = row[j - 1] + table_sum[i - 1][j] + table_sum[i][j - 1] - table_sum[i - 1][j - 1]

for _ in range(query_count):
    x1, y1, x2, y2 = map(int, input().split())
    result.append(str(table_sum[x2][y2] - table_sum[x1 - 1][y2] - table_sum[x2][y1 - 1] + table_sum[x1 - 1][y1 - 1]))

print("\n".join(result))