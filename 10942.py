# 팰린드롬? (https://www.acmicpc.net/problem/10942)
# tier: Gold 4
# tags: Dynamic Programming
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = list(map(int, input().split()))
is_palindrome = [[False for _ in range(n)] for _ in range(n)]

for center in range(n):
    for is_even in (0, 1):
        i, j = center, center + is_even
        while i >= 0 and j < n and nums[i] == nums[j]:
            is_palindrome[i][j] = True
            i -= 1
            j += 1

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print("1\n" if is_palindrome[a-1][b-1] else "0\n")