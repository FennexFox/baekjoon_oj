n = int(input())
w = 2*n-1

out = ""
for i in range(n-1):
    temp = "".join("*" if abs(n-(j+1)) == i else " " for j in range(w))
    out += temp.rstrip() + "\n"

print(out + "*" * w)