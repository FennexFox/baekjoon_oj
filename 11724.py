import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count_cc = -1 # 0번 노드에 대한 카운트 보정

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for i, node in enumerate(nodes):
    if visited[i]:
        continue
    my_stack = [node]
    while my_stack:
        this_node = my_stack.pop()
        for that_node in this_node:
            if visited[that_node]:
                continue
            visited[that_node] = True
            my_stack.append(nodes[that_node])
    else:
        count_cc += 1

print(count_cc)