# A → B (https://www.acmicpc.net/problem/16953)
# tier: Silver 2
# tags: Graph Theory, Graph Search, Greedy, BFS

num1, num2 = map(int, input().split())
i = 1

while num1 < num2:
    if num2 % 2 == 0:
        num2 //= 2
    elif num2 % 10 == 1:
        num2 //= 10
    else:
        break
    i += 1

print(i if num1 == num2 else -1)