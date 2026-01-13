import sys
input = sys.stdin.readline
print = sys.stdout.write

n, h, w = map(int, input().split())
answer = ["?"]*n

for _ in range(h):
    string = input()
    for i in range(n):
        temp = string[w*i:w*(i+1)].replace("?", "")
        if temp:
            answer[i] = temp[0]

print("".join(answer))