import sys

input = sys.stdin.readline
n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

if n >= 1:
    dp[1] = stairs[1]

    if n >= 2:
        dp[2] = sum(stairs[:3])

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + sum(stairs[i - 1:i + 1]))

print(dp[-1])