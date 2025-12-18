# ATM (https://www.acmicpc.net/problem/11399)
# tier: Platinum 5
# tags: Data Structure, Sort, Segment Tree, Divide and Conquer

length = int(input())
array = list(map(int, input().split()))
count = 0

for i in range(length-1, -1, -1):
    for j in range(i):
        if array[j] > array[j+1]:
            count += 1
            array[j], array[j+1] = array[j+1], array[j]
            
print(count)