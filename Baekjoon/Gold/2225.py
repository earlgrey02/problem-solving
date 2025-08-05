import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1 if j == 1 else 0 for j in range(k + 1)] for _ in range(n + 1)]
dp[1] = [i for i in range(k + 1)]

for i in range(2, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1_000_000_000

print(dp[n][k])