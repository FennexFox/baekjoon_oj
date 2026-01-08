n = int(input())
applicants = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum([(a-1)//t + 1 for a in applicants]))
print(" ".join(map(str, divmod(sum(applicants), p))))