import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

def martian_math(num, operand):
    if operand == "@":
        return num*3
    elif operand == "%":
        return num+5
    elif operand == "#":
        return num-7

for _ in range(n):
    formular = input().split()
    num, operands = float(formular[0]), formular[1:]
    
    for operand in operands:
        num = martian_math(num, operand)
    
    print(f"{num:.2f}\n")