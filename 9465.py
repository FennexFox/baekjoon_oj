# 스티커 (https://www.acmicpc.net/problem/9465)
# tier: Silver 1
# tags: Dynamic Programming

import sys
input = sys.stdin.readline
print = sys.stdout.write

tests = int(input())
out = []

def solve():
    _ = input()
    stickers_0 = list(map(int, input().split()))
    stickers_1 = list(map(int, input().split()))

    that_0 = this_0 = that_1 = this_1 = 0
    for s_0, s_1 in zip(stickers_0, stickers_1):
        new_0 = max(this_1, that_1) + s_0
        new_1 = max(this_0, that_0) + s_1
        
        that_0, that_1, this_0, this_1 = this_0, this_1, new_0, new_1

    return str(max(this_0, this_1))

for _ in range(tests):
    out.append(solve())

print("\n".join(out))