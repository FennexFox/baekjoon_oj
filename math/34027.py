import sys
input = sys.stdin.readline
print = sys.stdout.write

out = ""
for _ in range(int(input())):
    num = int(input())
    out += "1\n" if not(num % num**0.5) else "0\n"

print(out)