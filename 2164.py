from collections import deque

n = int(input())
cards = deque([i+1 for i in range(n)])

while len(cards)>2:
    cards.popleft()
    cards.rotate(-1)

print(cards.pop())