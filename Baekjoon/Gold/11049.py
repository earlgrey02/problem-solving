import sys
from math import inf

input = sys.stdin.readline

n = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[inf if i != j else 0 for j in range(n)] for i in range(n)]

for i in range(1, n):
    for j in range(n - i):
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + (matrices[j][0] * matrices[k][1] * matrices[j + i][1]))

print(dp[0][-1])