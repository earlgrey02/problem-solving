import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]

dp[0] = 1
if n >= 2:
    dp[2] = 3

for i in range(4, n + 1, 2):
    dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2:2]) * 2

print(dp[-1])