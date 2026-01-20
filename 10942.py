# 팰린드롬? (https://www.acmicpc.net/problem/10942)
# tier: Gold 4
# tags: Dynamic Programming
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = list(map(int, input().split()))
is_palindrome = [[True if i==j else False for j in range(n)] for i in range(n)]

for center in range(n-1):
    if nums[center] == nums[center+1]:
        is_palindrome[center][center+1] = True
    for offset in range(min(center, n-1-center)):
        i, j = center - offset, center + offset
        if not is_palindrome[i][j]:
            break
        if nums[i-1] == nums[j+1]:
            is_palindrome[i-1][j+1] = True
    for offset in range(min(center, n-2-center)):
        i, j = center- offset, center + offset + 1
        if not is_palindrome[i][j]:
            break
        if nums[i-1] == nums[j+1]:
            is_palindrome[i-1][j+1] = True

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print("1\n" if is_palindrome[a-1][b-1] else "0\n")