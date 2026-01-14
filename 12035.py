t = int(input())

for x in range(1, t+1):
    d, k, n = map(int, input().split())
    dancers = [(i+n*(-1)**(n%2))%d+1 if i%2 else (i-n*(-1)**(n%2))%d+1 for i in range(d)]
    k_i = dancers.index(k)
        
    print(f"Case #{x}: {dancers[(k_i+1)%d]} {dancers[(k_i-1)%d]}")