# 36진수 (https://www.acmicpc.net/problem/1036)
# tier: Gold 2
# tags: Math, Implementation, Greedy

n = int(input())

nums, total, digits = [], 0, set()
for _ in range(n):
    num = input()
    nums.append(num)
    total += int(num, 36)
    digits |= set(num)

sum_diffs = []
for digit in digits:
    new_nums = [int(num.replace(digit, "Z"), 36) for num in nums]
    sum_diffs.append((sum(new_nums)-total, digit))

k = int(input())
replace_map = {d: "Z" for _, d in sorted(sum_diffs, reverse=True)[:k]}
nums = list(map(lambda x: x.translate(x.maketrans(replace_map)), nums))
new_total = sum(map(lambda x: int(x, 36), nums))

answer = ""
base36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while new_total > 0:
    digit = new_total%36
    answer = base36[digit] + answer
    new_total //= 36

print(answer if answer else 0)
