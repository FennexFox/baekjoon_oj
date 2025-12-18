# 곱셈  (https://www.acmicpc.net/problem/1629)
# Silver 1
# Math, Divide and Conquer

num1, num2, num3 = map(int, input().split())
num1 %= num3
num4, record = num1, []

for i in range(num2):
    num4 %= num3
    if record and num4 in record:
        break
    
    record.append(num4)
    num4 *= num1

loop_start = 0

try:
    loop_start = record.index(num4)
except:
    pass

record = record[loop_start:]
num2 -= loop_start
cycle_len = len(record)

print(record[(num2 - 1)%cycle_len])