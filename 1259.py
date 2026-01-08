import sys
input = sys.stdin.readline
print = sys.stdout.write

while True:
    num = input().rstrip()
    if num == "0":
        break
    elif num == num[::-1]:
        print("yes\n")
    else:
        print("no\n")