# 피보나치 수 (6) (https://www.acmicpc.net/problem/11444)
# tier: Gold 2
# tags: Math, Divide and Conquer

num = int(input())
MOD = 1000000007

def mat_mul(a, b):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
         (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
         (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD]
    ]

def mat_pow(a, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2:
            result = mat_mul(result, a)
        a = mat_mul(a, a)
        n //= 2
    return result

def fib(n):
    if not n:
        return 0
    base = [[1, 1], [1, 0]]
    mat = mat_pow(base, n)
    return mat[0][1]

print(fib(num))