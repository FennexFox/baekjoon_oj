import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n):
    temp = list(map(int, input().split()))
    start = temp[0]
    
    for i in range(1, n*n, 2):
        edge = temp[i]
        if edge == -1:
            break
        weight = temp[i+1]
        tree[start].append([edge, weight])
    
def dfs(start, tree):
    distances = [-1] * (n+1)

    stack, distances[start] = [start], -1
    while stack:
        this_node = stack.pop()
        for that_node, weight in tree[this_node]:
            if distances[that_node] == -1:
                distances[that_node] = distances[this_node] + weight
                stack.append(that_node)
    
    return distances

def get_farthest(start, tree):
    distances = dfs(start, tree)
    
    f_node, f_dist = start, 0
    for i, dist in enumerate(distances):
        if dist > f_dist:
            f_node, f_dist = i, dist
    
    return f_node, f_dist

a, _ = get_farthest(1, tree)
_, diameter = get_farthest(a, tree)

print(diameter)