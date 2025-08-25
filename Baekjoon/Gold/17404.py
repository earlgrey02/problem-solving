import sys
from copy import deepcopy
from math import inf

input = sys.stdin.readline

n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]
cost = inf

for i in range(3):
    dp = deepcopy(houses)

    dp[0] = [dp[0][j] if i == j else inf for j in range(3)]

    for j in range(1, n):
        dp[j][0] += min(dp[j - 1][1:])
        dp[j][1] += min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] += min(dp[j - 1][:2])

    cost = min(cost, *(dp[n - 1][j] for j in range(3) if i != j))

print(cost)