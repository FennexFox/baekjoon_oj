# 트리의 부모 찾기 (https://www.acmicpc.net/problem/11725)
# tier: Silver 2
# tags: Graph, Tree, DFS, BFS

import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, i):
        self.name = i
        self.parent = None
        self.unsorted_links = set()
    
    def __call__(self, other):
        self.unsorted_links.add(other)
        other.unsorted_links.add(self)
    
    def __str__(self):
        return (str(self.parent.name) + "\n") if self.parent else ""

    def dfs(self):
        while self.unsorted_links:
            link = self.unsorted_links.pop()
            if self in link.unsorted_links:
                link.unsorted_links.remove(self)
            link.parent = self
            link.dfs()
            
        
length = int(input())
graph = [Node(i+1) for i in range(length)]

for _ in range(length-1):
    node1, node2 = [graph[i-1] for i in map(int, input().split())]
    node1(node2)

graph[0].dfs()

out = []
for i in range(length):
    out.append(graph[i])

print("".join(map(str, out)))