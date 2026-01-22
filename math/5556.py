import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
k = int(input())

for _ in range(k):
    a, b = map(lambda x: min(int(x), (n+1)-int(x)), input().split())
    print(str(min(a, b)%3).replace("0", "3")+"\n")