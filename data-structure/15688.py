import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = sorted(int(input()) for _ in range(n))
print("\n".join(map(str, nums)))