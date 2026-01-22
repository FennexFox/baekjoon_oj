import sys
input = sys.stdin.readline

words = {input().strip() for _ in range(int(input()))}
print("\n".join(sorted(words, key=lambda x: (len(x), x))))