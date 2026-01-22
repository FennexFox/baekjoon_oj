from collections import deque

INF, MAX = 10**9, 10**5
n, k = map(int, input().split())
count = [INF] * 100001
count[n] = 0
q = deque([n])

if n >= k:
    print(n-k)
else:
    while q:
        node = q.popleft()
        steps = count[node]

        if node == k:
            print(count[node])
            break

        for step in (node-1, node+1, 2*node):
            if 0<=step and step<=MAX and count[step] > steps+1:
                q.append(step)
                count[step] = steps+1