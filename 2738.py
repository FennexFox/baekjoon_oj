n, m = map(int, input().split())

mat1 = [[0]*m for _ in range(n)]
mat2 = [[0]*m for _ in range(n)]
mat3 = [[0]*m for _ in range(n)]

for row in range(n):
    mat1[row] = list(map(int, input().split()))

for row in range(n):
    mat2[row] = list(map(int, input().split()))

for row in range(n):
    for cell in range(m):
        mat3[row][cell] = mat1[row][cell] + mat2[row][cell]
    print(" ".join(map(str, mat3[row])))