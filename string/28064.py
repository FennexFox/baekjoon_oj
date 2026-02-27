n = int(input())
names = [input() for _ in range(n)]
count = 0

for i in range(n):
    name_a = names[i]
    len_a = len(name_a)
    for j in range(i+1, n):
        name_b = names[j]
        len_b = len(name_b)
        len_min = min(len_a, len_b)
        
        for k in range(1, len_min+1):
            head_a, tail_a = name_a[:k], name_a[len_a-k:]
            head_b, tail_b = name_b[:k], name_b[len_b-k:]
            
            if head_a == tail_b or tail_a == head_b:
                count += 1
                break

print(count)