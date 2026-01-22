n, m = map(int, input().split())

first = "".join(input() for _ in range(n))
second = "".join(input() for _ in range(n))

if first == second[::2] and first == second[1::2]:
    print("Eyfa")
else:
    print("Not Eyfa")