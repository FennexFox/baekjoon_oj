# N과 M (2) (https://www.acmicpc.net/problem/15650)
# tier: Silver 3
# tags: Backtracking
import sys
print = sys.stdout.write

n, m = map(int, input().split())
compbos = [[]]

def expand_array(n, arrays):
    next = []
    for array in arrays:
        last = array[-1] if array else 0
        next += [array + [num+1] for num in range(last, n)]
    return next

while len (compbos[-1]) < m:
    compbos = expand_array(n, compbos)

out = []
for array in compbos:
    out.append(" ".join(map(str, array)))
print("\n".join(out))