import sys

input = sys.stdin.readline

n, m = map(int, input().split())
apps = list(zip(*(list(map(int, input().split())) for _ in range(2))))
max_cost = sum(map(lambda x: x[1], apps))
dp = [0 for _ in range(max_cost + 1)]

for memory, cost in apps:
    for i in range(max_cost, cost - 1, -1):
        dp[i] = max(dp[i], dp[i - cost] + memory)

print(next(i for i in range(max_cost + 1) if dp[i] >= m))