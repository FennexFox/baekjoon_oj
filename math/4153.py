while True:
    lines = list(map(int, input().split()))
    if lines == [0, 0, 0]:
        break
    
    sqr_sum = sum([x**2 for x in lines])
    sqr_max = max(lines)**2
    answer = "right" if 2*sqr_max == sqr_sum else "wrong"
    
    print(answer)