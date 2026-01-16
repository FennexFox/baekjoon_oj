import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = [0 for _ in range(10001)]

for _ in range(n):
    num = int(input())
    nums[num] += 1

for i, count in enumerate(nums):
    for _ in range(count):
        print(str(i)+"\n")