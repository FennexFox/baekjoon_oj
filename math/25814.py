a, b = input().split()

def get_weight(num_string):
    return len(num_string) * sum(int(x) for x in num_string)

aw, bw = get_weight(a), get_weight(b)

if aw>bw:
    print(1)
elif aw<bw:
    print(2)
else:
    print(0)