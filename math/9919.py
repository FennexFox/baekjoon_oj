n = int(input())
poles = [int(input()) for _ in range(n)]
answer = [0, 0, 0]

last = poles[-1]

if poles[0] > poles[-1]:
    last_direction = 1
elif poles[0] < poles[-1]:
    last_direction = 2
else:
    last_direction = 0

answer[last_direction] += 1

for pole in poles:
    if pole > last:
        direction = 1
    elif pole < last:
        direction = 2
    else:
        direction = 0

    if direction != last_direction:
        answer[direction] += 1

    last = pole
    last_direction = direction

pole = poles[0]
if pole > last:
    direction = 1
elif pole < last:
    direction = 2
else:
    direction = 0

if direction != last_direction:
    answer[direction] += 1

print(" ".join(map(str, answer)))