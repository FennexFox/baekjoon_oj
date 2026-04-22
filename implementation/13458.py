import math

_ = input()
a = map(int, input().split())
b, c = map(int, input().split())

out = 0
for students in a:
    out += 1 + math.ceil(max((students-b),0) / c)

print(out)