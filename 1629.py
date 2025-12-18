# 곱셈  (https://www.acmicpc.net/problem/1629)
# Silver 1
# Math, Divide and Conquer

num1, num2, num3 = map(int, input().split())
num1 %= num3
num4 = 1

while num2:
    if num2 % 2 != 0:
        num4 = (num4 * num1) % num3
    num1 *= num1
    num1 %= num3
    num2 //= 2

print(num4)