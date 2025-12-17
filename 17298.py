# 오큰수 (https://www.acmicpc.net/problem/17298)
# Gold 4
# Data Structure, Stack

import sys
input = sys.stdin.readline
print = sys.stdout.write

len = int(input())
list = list(map(int, input().split()))

for i in range(len):
    now, temp = list[i], list[-1:i:-1]
    
    while temp and temp[-1] <= now:
        temp.pop()
        pass
    
    nge = str(temp[-1]) if temp else "-1"
    nge += " "
    
    print(nge)