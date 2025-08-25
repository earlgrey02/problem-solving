import sys

input = sys.stdin.readline

n = int(input())
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n + 1)]
mod = 10 ** 9

for j in range(1, 10):
    dp[1][j][1 << j] = 1

for i in range(2, n + 1):
    for j in range(10):
        for mask in range(1 << 10):
            if j == 0:
                dp[i][j][mask | (1 << j)] += dp[i - 1][j + 1][mask]
            elif j == 9:
                dp[i][j][mask | (1 << j)] += dp[i - 1][j - 1][mask]
            else:
                dp[i][j][mask | (1 << j)] += dp[i - 1][j - 1][mask] + dp[i - 1][j + 1][mask]

            dp[i][j][mask | (1 << j)] %= mod

print(sum(dp[n][i][(1 << 10) - 1] % mod for i in range(10)) % mod)