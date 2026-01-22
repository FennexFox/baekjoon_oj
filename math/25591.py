num1, num2 = map(int, input().split())

a = 100 - num1
b = 100 - num2
c = 100 - (a + b)
d = a * b
q, r = divmod(d, 100)

print(a, b, c, d, q, r)
print(c + q, r)