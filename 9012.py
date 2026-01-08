n = int(input())

for i in range(n):
    string = input()
    num, vps = 0, False
    for ch in string:
        num += 1 if ch == "(" else -1
        if num < 0:
            break
    else:
        if not num:
            vps = True
    print("YES" if vps else "NO")