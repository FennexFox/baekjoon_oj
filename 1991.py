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
    nodes[parent] = (left, right)

def preorder(node):
    if node == ".":
        return
    answer.append(node)
    left, right = nodes[node]
    preorder(left)
    preorder(right)

def inorder(node):
    if node == ".":
        return
    left, right = nodes[node]
    inorder(left)
    answer.append(node)
    inorder(right)

def postorder(node):
    if node == ".":
        return
    left, right = nodes[node]
    postorder(left)
    postorder(right)
    answer.append(node)

order = [preorder, inorder, postorder]

for f in order:
    f("A")
    print("".join(answer) + "\n")
    answer, visited = [], dict()