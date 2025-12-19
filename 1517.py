# ATM (https://www.acmicpc.net/problem/11399)
# tier: Platinum 5
# tags: Data Structure, Sort, Segment Tree, Divide and Conquer

_ = int(input())
array = list(map(int, input().split()))
count = 0

def split_and_merge(array):
    midpoint = len(array)//2
    
    if midpoint == 0:
        return array
    else:
        left = split_and_merge(array[:midpoint])
        right = split_and_merge(array[midpoint:])
        return sort(left, right)

def sort(left, right):
    array = []
    global count
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
            count += len(left) - i
    
    array += right[j:] if i == len(left) else left[i:]
    return array

array = split_and_merge(array)
print(count)