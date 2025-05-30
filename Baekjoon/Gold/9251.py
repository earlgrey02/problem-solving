import sys

input = sys.stdin.readline

sequences = tuple(input().strip() for _ in range(2))
dp = [[0 for _ in range(len(sequences[1]) + 1)] for _ in range(len(sequences[0]) + 1)]

for i in range(1, len(sequences[0]) + 1):
    for j in range(1, len(sequences[1]) + 1):
        if sequences[0][i - 1] == sequences[1][j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])