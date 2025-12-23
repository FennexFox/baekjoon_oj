# 트리의 부모 찾기 (https://www.acmicpc.net/problem/11725)
# tier: Silver 2
# tags: Graph, Tree, DFS, BFS

length = int(input())
visited = [False] * (length + 1)
parent = [i for i in range(length + 1)]
linked_nodes = {i+1: [] for i in range(length)}

for i in range(length-1):
    node1, node2 = map(int, input().split())
    linked_nodes[node1].append(node2)
    linked_nodes[node2].append(node1)

def dfs(node):
    visited[node] = True
    for other_node in linked_nodes[node]:
        if not visited[other_node]:
            dfs(other_node)
            parent[other_node] = node

dfs(1)

print('\n'.join(map(str, parent[2:])))