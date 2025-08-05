import sys
from math import floor, inf, sqrt

input = sys.stdin.readline

n = int(input())
dp = [inf for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, floor(sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)

print(dp[n])