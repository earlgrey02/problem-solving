import sys

input = sys.stdin.readline

t = int(input())
numbers = [int(input()) for _ in range(t)]
n = max(numbers)
dp = [[0 for _ in range(3)] for _ in range(n + 1)]
mod = 1_000_000_009

dp[1] = [1, 0, 0]
if n >= 2:
    dp[2] = [0, 1, 0]
if n >= 3:
    dp[3] = [1, 1, 1]

for i in range(4, n + 1):
    dp[i][0] = sum(dp[i - 1][1:]) % mod
    dp[i][1] = sum(dp[i - 2][::2]) % mod
    dp[i][2] = sum(dp[i - 3][:2]) % mod

print(*(sum(dp[i]) % mod for i in numbers), sep = '\n')