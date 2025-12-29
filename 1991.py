# 트리 순회 (https://www.acmicpc.net/problem/1991)
# tier: Silver 1
# tags: Tree, Recursion

import sys
print = sys.stdout.write

length = int(input())
nodes, visited = dict(), dict()
answer = []

for _ in range(length):
    parent, left, right = input().split()
    nodes[parent] = [left, right]

def preorder(node):
    answer.append(node)
    for child in nodes[node]:
        if child == ".":
            continue
        elif visited.get(child, True):
            preorder(child)
            visited[child] = False

def inorder(node):
    for is_right, child in enumerate(nodes[node]):
        if child == ".":
            continue
        elif visited.get(child, True):
            if is_right:
                answer.append(node)
            inorder(child)
            visited[child] = False
    if node not in answer:
        answer.append(node)

def postorder(node):
    for child in nodes[node]:
        if child == ".":
            continue
        elif visited.get(child, True):
            postorder(child)
            visited[child] = False
    answer.append(node)

order = [preorder, inorder, postorder]

for f in order:
    f("A")
    print("".join(answer) + "\n")
    answer, visited = [], dict()