import sys
from math import inf

input = sys.stdin.readline

n = int(input())
dp = [inf for _ in range(n + 1)]
dp[0] = 0

if n >= 2:
    dp[2] = 2

for i in range(2, n + 1):
    dp[i] = min(dp[i - 2], dp[i - 5] if i >= 5 else inf) + 1

print(dp[-1] if dp[-1] != inf else -1)