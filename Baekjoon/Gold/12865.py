import sys

input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(k + 1)]

for weight, value in items:
    for i in range(k, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[k])