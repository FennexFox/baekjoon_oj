import sys
input = sys.stdin.readline
print = sys.stdout.write

n, s = int(input()), set()
for _ in range(n):
    com = input().split()
    if len(com) > 1:
        com[1] = int(com[1])

    if com[0] == "add":
        s.add(com[1])
    elif com[0] == "remove":
        if com[1] in s:
            s.remove(com[1])
    elif com[0] == "check":
        print("1\n" if com[1] in s else "0\n")
    elif com[0] == "toggle":
        if com[1] in s:
            s.remove(com[1])
        else:
            s.add(com[1])
    elif com[0] == "all":
        s = {i+1 for i in range(20)}
    elif com[0] == "empty":
        s = set()