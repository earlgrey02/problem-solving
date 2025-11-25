import sys
from math import inf

input = sys.stdin.readline

n = int(input())
dp = [0 if i == 1 else inf for i in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = min(dp[i // 3] if i % 3 == 0 else inf, dp[i // 2] if i % 2 == 0 else inf, dp[i - 1]) + 1

print(dp[-1])