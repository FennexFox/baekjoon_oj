import sys
input = sys.stdin.readline


rows, columns = map(int, input().split())
table = [[0 if ch=="B" else 1 for ch in input().strip()] for _ in range(rows)]

target_0 = [[0 if (i+j)%2 == 0 else 1 for i in range(8)] for j in range(8)]
score_0 = [[0 for _ in range(columns-7)] for _ in range(rows-7)]

min_global = 64
for row in range(rows-7):
    for column in range(columns-7):
        score_ij = score_0[row][column]
        for i in range(8):
            for j in range(8):
                cell = table[row+i][column+j]
                target = target_0[i][j]
                if cell==target:
                    score_ij += 1
        min_ij = min(score_ij, 64-score_ij)
        if min_ij == 0:
            print(0)
            exit()
        else:
            min_global = min(min_global, min_ij)

print(min_global)