n = int(input())
start = max(1, n - 9*len(str(n)))
answer = 0

for num in range(start, 1000001): 
    digitsum = num + sum(int(x) for x in str(num))
    if digitsum == n:
        answer = num
        break

print(answer)