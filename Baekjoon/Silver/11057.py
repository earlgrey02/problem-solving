import sys

input = sys.stdin.readline

n = int(input())
dp = [[1 if i == 1 else 0 for _ in range(10)] for i in range(n + 1)]
mod = 10007

for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][:j + 1]) % mod

print(sum(dp[n]) % mod)