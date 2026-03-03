s = input()
out = 0

def get_num(ch):
    return ord(ch) - (ord("A") - 1)

for ch in s:
    out *= 26
    out += get_num(ch)

print(out)