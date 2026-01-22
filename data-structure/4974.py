n = int(input())

while n:
    scores = sorted([int(input()) for _ in range(n)])[1:-1]
    print(int(sum(scores)/len(scores)))
    n = int(input())