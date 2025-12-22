import sys

input = sys.stdin.readline

t = int(input())
queries = [int(input()) for _ in range(t)]
n = max(queries)
dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in (1, 2, 3):
    for j in range(i, n + 1):
        dp[j] += dp[j - i]

print(*(dp[i] for i in queries), sep = '\n')