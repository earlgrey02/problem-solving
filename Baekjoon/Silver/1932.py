import sys

input = sys.stdin.readline

n = int(input())
dp = [0] + [list(map(int, input().split())) for _ in range(n)]

for i in range(2, n + 1):
    for j in range(i):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i - 1:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1:j + 1])

print(max(dp[n]))