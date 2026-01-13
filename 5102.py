import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
while n+m>0:
    pairs, is_odd = divmod((n-m), 2)
    if is_odd:
        if pairs:
            pairs -= 1
        else:
            is_odd -= 1
    print(f"{pairs} {is_odd}\n")
    n, m = map(int, input().split())