n = int(input())

for _ in range(n):
    r, s = input().split()
    r, out = int(r), ""
    for ch in s:
        out += ch * r
    print(out)