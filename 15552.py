import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    num1, num2 = map(int, input().split())
    print(f"{num1 + num2}\n")