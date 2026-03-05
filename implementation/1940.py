import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
ns = sorted(map(int, input().split()))

left, right = 0, n - 1
count = 0

while left < right:
    pair_sum = ns[left] + ns[right]

    if pair_sum == m:
        count += 1
        left += 1
        right -= 1
    elif pair_sum < m:
        left += 1
    else:
        right -= 1

print(count)
