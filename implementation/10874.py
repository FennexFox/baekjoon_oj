n = int(input())
answers = [(num)%5+1 for num in range(10)]

for i in range(n):
    hands_in = list(map(int, input().split()))
    if answers == hands_in:
        print(i+1)