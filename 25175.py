n, m, k = map(int, input().split())
next = ((m-3)+k)%n
print(next if next != 0 else n)