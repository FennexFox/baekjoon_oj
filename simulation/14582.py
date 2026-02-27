a = list(map(int, input().split()))
b = list(map(int, input().split()))

geminies, gulivers = 0, 0

for x, y in zip(a, b):
    geminies += x
    if geminies > gulivers:
        print("Yes")
        exit()
    gulivers += y

print("No")