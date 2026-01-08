import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
queue = deque([])

for _ in range(n):
    com = input().split()
    out = ""
    if com[0] == "push":
        queue.append(com[1])
    elif com[0] == "pop":
        if queue:
            out = queue.popleft()
        else:
            out = "-1"
    elif com[0] == "size":
        out = str(len(queue))
    elif com[0] == "empty":
        if queue:
            out = "0"
        else:
            out = "1"
    elif com[0] == "front":
        if queue:
            out = queue[0]
        else:
            out = "-1"
    elif com[0] == "back":
        if queue:
            out = queue[-1]
        else:
            out = "-1"
    print(out+"\n") if out else print(out)