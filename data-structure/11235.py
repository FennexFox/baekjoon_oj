import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
votes = Counter([input().strip() for _ in range(n)])
max_vote = max(votes.values())
most_votes = [name for name, count in votes.items() if count == max_vote]

print("\n".join(sorted(most_votes)))