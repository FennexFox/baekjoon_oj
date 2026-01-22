import sys
input = sys.stdin.readline

n, H = map(int, input().split())
answer = 0

for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    if a > H:
        print("impossible")
        exit()
    if b <= H:
        answer += a
    else:
        answer += b
        
print(answer)