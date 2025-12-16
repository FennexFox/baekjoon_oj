# 나머지 합 (https://www.acmicpc.net/problem/11003)
# Platinum 5
# Data Structure, Prioirity Queue, Deque, Sliding Window Maximum using a Deque
from collections import deque

num_len, window_len = map(int, input().split())
nums = map(int, input().split())
window = deque()

for i, num in enumerate(nums):
    while window and window[-1][0] > num:
        window.pop()
    window.append([num, i])
    if i - window[0][1] >= window_len:
        window.popleft()
    
    print(window[0][0], end=" ")