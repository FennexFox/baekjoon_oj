total_cost = int(input())
recognizable_cost = sum(int(input()) for _ in range(9))
print(total_cost - recognizable_cost)