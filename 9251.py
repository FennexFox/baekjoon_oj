# LCS (https://www.acmicpc.net/problem/9251)
# tier: Gold 5
# tags: Dynamic Programming, String, Longest Common Subsequence

string1 = input()
string2 = input()

dp = [[0] * (len(string2)+1) for _ in range(len(string1)+1)]

for i in range(len(string1)):
    for j in range(len(string2)):
       if string1[i] == string2[j]:
           dp[i+1][j+1] = dp[i][j] + 1
       else:
           dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[-1][-1])