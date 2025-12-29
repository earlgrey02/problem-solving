import sys
from math import inf

input = sys.stdin.readline

c, n = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(n)]
maximum = c + 101
dp = [inf for _ in range(maximum)]
dp[0] = 0

for i in range(1, maximum):
    for cost, population in cities:
        if i - population >= 0:
            dp[i] = min(dp[i], dp[i - population] + cost)

print(min(dp[c:]))