n = int(input())

if n == 1:
    print(1906)
else:
    a = 10**(n-1) + 2*10**(n//2) + 1
    print(1905 + a)