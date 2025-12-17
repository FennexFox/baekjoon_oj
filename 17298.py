# 오큰수 (https://www.acmicpc.net/problem/17298)
# Gold 4
# Data Structure, Stack

import sys
input = sys.stdin.readline
print = sys.stdout.write

len = int(input())
nums = list(map(int, input().split()))
answer = [-1] * len
stack = []

for i, num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        answer[stack.pop()] = num
    stack.append(i)

print(" ".join(map(str, answer)))