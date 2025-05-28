import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
dp = [[1 for _ in range(n)] for _ in range(2)]

for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, - 1):
        if sequence[i] > sequence[j]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

print(max(map(lambda x: sum(x) - 1, zip(*dp))))