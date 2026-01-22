available = list(map(int, input().split()))
requested = list(map(int, input().split()))
deficit = 0

for a, r in zip(available, requested):
    deficit += max(0, r-a)

print(deficit)