import sys
from math import inf, isqrt

input = sys.stdin.readline

n = int(input())
dp = [inf for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, isqrt(i) + 1):
        dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)

print(dp[-1])