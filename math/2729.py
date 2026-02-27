import sys

input = sys.stdin.readline
print = sys.stdout.write

r = int(input())

for _ in range(r):
    a, b = map(lambda x:int(x, 2), input().split())
    print(bin(a+b)[2:]+"\n")