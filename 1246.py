n, m = map(int, input().split())
prices = sorted([int(input()) for _ in range(m)])

revs = [(price, price * min(n, m - i)) for i, price in enumerate(prices)]
revs = map(str, sorted(revs, key=lambda x: x[1])[-1])
print(" ".join(revs))