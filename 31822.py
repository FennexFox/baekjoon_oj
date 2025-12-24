to_retake = input()[:5]
num, answer = int(input()), 0

for _ in range(num):
    answer += 1 if input()[:5] == to_retake else 0

print(answer)