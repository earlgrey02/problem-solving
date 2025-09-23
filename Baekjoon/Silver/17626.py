import sys
from math import inf, isqrt

input = sys.stdin.readline

n = int(input())
dp = [inf if i != 0 else 0 for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, isqrt(i) + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)

print(dp[-1])