_ = input()
ns = set(map(int, input().split()))
_ = input()
ms = list(map(int, input().split()))
out = ["1" if m in ns else "0" for m in ms]

print("\n".join(out))