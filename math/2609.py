n, m = map(int, input().split())

def gcd(n, m):
    n %= m
    return gcd(m, n) if n else m

gcd_nm = gcd(n, m)

print(gcd_nm)
print(n*m//gcd_nm)