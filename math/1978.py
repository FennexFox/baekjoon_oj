_ = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)

is_prime = [False, False] + [True] * (max_num-1)

for n in range(2, int(max_num**0.5)+1):
    if is_prime[n]:
        for i in range(n*n, max_num+1, n):
            is_prime[i] = False

print(sum(is_prime[n] for n in nums))