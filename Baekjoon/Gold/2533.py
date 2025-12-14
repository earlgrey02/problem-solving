import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: int):
    visited[v] = True
    dp[v][1] = 1

    for next_v in adjacencies[v]:
        if not visited[next_v]:
            dfs(next_v)
            dp[v][0] += dp[next_v][1]
            dp[v][1] += min(dp[next_v])

n = int(input())
adjacencies = [[] for _ in range(n)]
dp = [[0 for _ in range(2)] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(n - 1):
    v1, v2 = map(lambda x: int(x) - 1, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

dfs(0)

print(min(dp[0]))