import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(lambda x: x[1], sorted((tuple(map(int, input().split())) for _ in range(n)), key = lambda x: x[0])))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))