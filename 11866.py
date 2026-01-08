from collections import deque

n, k = map(int, input().split())
circle, answer = deque([str(i+1) for i in range(n)]), []

for i in range(n):
    circle.rotate(-k+1)
    answer.append(circle.popleft())

print(f"<{", ".join(answer)}>")