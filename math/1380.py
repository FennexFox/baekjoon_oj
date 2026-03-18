import sys

input = sys.stdin.readline
print = sys.stdout.write

order = 0
while True:
    num = int(input())
    order += 1
    
    if not num:
        break

    names = [input() for _ in range(num)]
    nums = [int(input().split()[0]) for _ in range(2*num-1)]
    nums = sorted(nums, key=lambda x: nums.count(x))
    print(f"{order} {names[nums[0]-1]}")