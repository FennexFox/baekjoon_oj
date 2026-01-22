n = int(input())

INF = 1000
dist = [[0 if i==j else INF for i in range(n)] for j in range(n)]
for i in range(n):
    row = input()
    for j, conn in enumerate(row):
        if conn == "Y":
            dist[i][j] = 1

for k in range(n):
    dist_k = dist[k]
    for i in range(n):
        dist_i = dist[i]
        for j in range(n):
            if dist_i[j] > dist_i[k] + dist_k[j]:
                dist_i[j] = dist_i[k] + dist_k[j]

count = [
    sum(1 for j in range(n) if i != j and dist[i][j] <= 2)
    for i in range(n)
]
print(max(count))