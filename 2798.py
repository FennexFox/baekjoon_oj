n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())), reverse=True)
max_sum = 0

for i in range(n):
    card_i = cards[i]
    for j in range(i+1, n):
        card_j = cards[j]
        for k in range(j+1, n):
            sum = card_i + card_j + cards[k]
            if sum <= m:
                max_sum = max(max_sum, sum)

print(max_sum)