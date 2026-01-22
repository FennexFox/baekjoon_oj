import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
stack = []

for _ in range(n):
    com = input().split()
    out = ""
    if com[0] == "push":
        stack.append(com[1])
    elif com[0] == "pop":
        if stack:
            out = stack.pop()
        else:
            out = "-1"
    elif com[0] == "size":
        out = str(len(stack))
    elif com[0] == "empty":
        if stack:
            out = "0"
        else:
            out = "1"
    elif com[0] == "top":
        if stack:
            out = stack[-1]
        else:
            out = "-1"
    print(out+"\n") if out else print(out)