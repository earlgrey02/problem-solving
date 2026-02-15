import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

dp = [[i for i in sequence] for _ in range(2)]

for i in range(1, n):
    dp[0][i] = max(dp[0][i], dp[0][i - 1] + sequence[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + sequence[i])

print(max(map(max, dp)))