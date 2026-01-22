s = input()

for i in range(10):
    s = s.replace(str(i), "")

print(1 if input() in s else 0)