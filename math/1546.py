n = int(input())
scores = list(map(int, input().split()))
score_max = max(scores)
print(sum([x/score_max*100 for x in scores])/n)