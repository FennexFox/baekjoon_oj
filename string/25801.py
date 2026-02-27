from collections import Counter

counter = Counter(input())
even = 0

for count in counter.values():
    if not count%2:
        even += 1

if not even:
    print("1")
elif even == len(counter):
    print("0")
else:
    print("0/1")