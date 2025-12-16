# 나머지 합 (https://www.acmicpc.net/problem/10986)
# Gold 3
# Math, Prefix Sum

num_counter, denom = map(int, input().split())
num = [int(x) for x in input().split()]

count = [1] + [0] * (denom - 1)
result = sum = 0

# 나머지가 n인 누적합을 리스트에 담기
for i in range(1, num_counter + 1):
    sum = (sum + num[i - 1]) % denom
    count[sum] += 1

# 누적합의 나머지가 같은 인덱스 중 2개를 뽑기
for remain in count:
    result += remain * (remain-1) // 2

print(result)