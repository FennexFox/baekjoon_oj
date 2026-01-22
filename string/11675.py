n = int(input())
bins = list(map(lambda x: bin(int(x))[2:], input().split()))

out = []
for x in bins:
    x = x.zfill(8)
    unscrambled, last = "", 0
    for digit in x[::-1]:
        this = not last if int(digit) else last
        unscrambled = str(int(this)) + unscrambled
        last = this
    out.append(unscrambled)

print(" ".join(map(lambda x: str(int(x, 2)), out)))