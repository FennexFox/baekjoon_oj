# 곱셈  (https://www.acmicpc.net/problem/11053)
# Silver 2
# Dynamic Programming, Longest Increasing Subsequence

_ = int(input())
array = [int(i) for i in input().split()]
sub_array = [array[0]]

for i in array:
    if i > sub_array[-1]:
        sub_array.append(i)

print(len(sub_array))