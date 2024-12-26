import sys

input = sys.stdin.readline

n = int(input())
dp = [int(i in (1, 2)) for i in range(n + 1)]

for i in range(3, n + 1):
    dp[i] = sum(dp[i - 2:i])

print(dp[n])