length = int(input())
temp = map(lambda x: int(x)%2, input().split())

print(1 if sum(temp) == (length+1)//2 else 0)