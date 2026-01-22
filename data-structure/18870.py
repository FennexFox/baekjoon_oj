n = int(input())
nums = list(map(int, input().split()))
coord_comp = {v: str(i) for i, v in enumerate(sorted(set(nums)))}

print(" ".join(str(coord_comp[num]) for num in nums))