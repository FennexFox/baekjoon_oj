import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
myheap = []

for _ in range(n):
    num = int(input())
    if not num:
        if myheap:
            print(str(heapq.heappop(myheap))+"\n")
        else:
            print("0\n")
    else:
        heapq.heappush(myheap, num)