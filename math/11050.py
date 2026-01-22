n, k = map(int, input().split())
k = min(k, n-k)

bico = 1
for i in range(k):
    bico *= (n-i)
    bico //= (i+1)

print(bico)