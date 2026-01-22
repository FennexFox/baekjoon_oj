n = int(input())

out = ""
while n != 0:
    m = n ** 2 - (n-1)
    out += f"{n} => {m}\n"
    n = int(input())

print(out)