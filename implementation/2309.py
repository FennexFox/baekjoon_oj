nums = sorted([int(input()) for _ in range(9)])
nots = sum(nums) - 100

for i, num_a in enumerate(nums):
    for num_b in nums[i+1:]:
        if num_a + num_b == nots:
            nums.remove(num_a)
            nums.remove(num_b)
            print("\n".join(map(str, nums)))
            exit()