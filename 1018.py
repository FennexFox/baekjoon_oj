import sys
input = sys.stdin.readline

rows, columns = map(int, input().split())
table = [[0 if ch=="B" else 1 for ch in input().strip()] for _ in range(rows)]

min_global = 64
for row in range(rows-7):
    for column in range(columns-7):
        score_ij = 0
        for i in range(8):
            for j in range(8):
                cell = table[row+i][column+j]
                target = 0 if (i+j)%2 == 0 else 1
                score_ij += (cell != target)
        min_ij = min(score_ij, 64-score_ij)
        min_global = min(min_global, min_ij)
        if min_global == 0:
            print(0)
            sys.exit()

print(min_global)