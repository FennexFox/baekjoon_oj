import sys
input = sys.stdin.readline
print = sys.stdout.write

length = int(input())

def change_base(num_str, base):
    out = 0
    for digit in num_str:
        digit = int(digit)

        if digit >= base:
            out = 0
            break

        out = out * base + digit
    return out
    
out = ""
for _ in range(length):
    i, num = input().split()
    num_8, num_16 = change_base(num, 8), change_base(num, 16)
    out += f"{i} {num_8} {int(num)} {num_16}\n"
print(out)