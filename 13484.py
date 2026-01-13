x = int(input())
n = int(input())
m = sum(int(input()) for _ in range(n))

print(x*(n+1)-m)