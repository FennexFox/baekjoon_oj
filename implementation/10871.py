len, criteria = map(int, input().split())
array = [i for i in input().split() if int(i) < criteria]
print(" ".join(array))