_ = input()
ns = map(int, input().split())
_ = input()
ms = map(int, input().split())

n_dict = dict()
for n in ns:
    n_dict[n] = n_dict.get(n, 0) + 1

answer = [str(n_dict.get(m, 0)) for m in ms]
print(" ".join(answer))