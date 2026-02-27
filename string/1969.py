import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
n_seqs = [input() for _ in range(n)]
seq, h_dist = [], 0

for i in range(m):
    candids = Counter(n_seq[i] for n_seq in n_seqs)
    h = candids.most_common(1)[0][1]
    s = min(ch for ch, cnt in candids.items() if cnt == h)
    
    seq.append(s)
    h_dist += n-h

print("".join(seq))
print(h_dist)