n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

stack, visited = [1],  [False] * (n+1)
while stack:
    this_node = stack.pop()
    visited[this_node] = True
    for next_node in graph[this_node]:
        if not visited[next_node]:
            stack.append(next_node)

print(sum(visited)-1)