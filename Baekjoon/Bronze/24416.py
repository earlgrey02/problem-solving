import sys

input = sys.stdin.readline

n = int(input())
dp = [1 if i in (1, 2) else 0 for i in range(n + 1)]

for i in range(3, n + 1):
    dp[i] = sum(dp[i - 2:i])

print(dp[-1], n - 2)