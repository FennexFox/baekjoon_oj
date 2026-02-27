MOD = 1234567
N = int(input().strip())

ans = 0
length = 1      # 현재 자릿수
start = 1       # 해당 자릿수 구간의 시작값 (1, 10, 100, ...)

while start * 10 <= N:
    count = 9 * start           # length자리 수의 개수
    ans = (ans + count * length) % MOD
    start *= 10
    length += 1

# 마지막 구간 처리 (start ~ N)
ans = (ans + (N - start + 1) * length) % MOD

print(ans)