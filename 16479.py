slope = int(input())
d1, d2 = map(int, input().split())
base = (d1 - d2)/2

print(slope**2 - base**2)