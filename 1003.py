import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

fibonacci = [1, 0, 1, 1]

for _ in range(n):
    f = int(input())
    while len(fibonacci) <= f+1:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    print(f"{fibonacci[f]} {fibonacci[f+1]}\n")