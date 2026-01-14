n = int(input())
o, p = n, 0

while not o%2:
    o//=2
    p+=1

print(o, p)