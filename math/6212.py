a, b = map(int, input().split())
nums = "".join([str(x) for x in range(a, b+1)])

out = [0] * 10
for ch in nums:
    out[int(ch)] += 1

print(" ".join(map(str, out)))