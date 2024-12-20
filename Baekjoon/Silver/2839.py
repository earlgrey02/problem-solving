import sys

input = sys.stdin.readline

n = int(input())
dp = [1 if i in (3, 5) else -1 for i in range(n + 1)]

for i in range(6, n + 1):
    if dp[i - 3] != -1 and dp[i - 5] != -1:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    elif dp[i - 3] != -1 or dp[i - 5] != -1:
        dp[i] = max(dp[i - 3], dp[i - 5]) + 1

print(dp[n])