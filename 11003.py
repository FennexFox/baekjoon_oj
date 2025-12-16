# 나머지 합 (https://www.acmicpc.net/problem/11003)
# Platinum 5
# Data Structure, Prioirity Queue, Deque, Sliding Window Maximum using a Deque
import sys
from collections import deque
input = sys.stdin.readline

num_len, window_len = map(int, input().split())
nums = list(map(int, input().split()))
window = deque()

for i in range(len(nums)):
    while window and nums[window[-1]] > nums[i]:
        window.pop()
    window.append(i)
    if i - window[0] >= window_len:
        window.popleft()
    
    print(nums[window[0]], end=" ")