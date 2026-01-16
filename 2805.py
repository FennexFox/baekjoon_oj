import math

n, m = map(int, input().split())
trees = [0] + sorted(list(map(int, input().split()))) + [0] # 패딩

if n == 1:
    print(trees[1] - m)
    exit()

prefix_sum = [0, sum(trees)]
for tree in trees[1:-1]:
    prefix_sum.append(prefix_sum[-1] - tree)


i = step = n//2
while True:
    h_trees = n-i
    lower = prefix_sum[i] - (h_trees+1)*trees[i-1]
    upper = prefix_sum[i+1] - (h_trees)*trees[i]
    
    dir = 0
    if m < upper:
        dir = 1
    elif m > lower:
        dir = -1
        
    if not dir:
        shortage = m - upper
        height = trees[i] - math.ceil(shortage / (h_trees+1))
        print(height)
        break
    else:
        step = max(1, step//2)
        i += dir * step