nums = list(map(int, input().split()))
eval = 0

for num in nums:
    eval += num ** 2

print(eval%10)