import sys
input = sys.stdin.readline

n = int(input())
ppl = [input().split() for _ in range(n)]
ppl = sorted(ppl, key=lambda x:int(x[0]))

print("\n".join(map(lambda x: " ".join(x), ppl)))