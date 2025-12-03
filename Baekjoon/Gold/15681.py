import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: int):
    visited[v] = True

    if dp[v] > 0:
        return dp[v]
    else:
        dp[v] = 1

    for next_v in adjacencies[v]:
        if not visited[next_v]:
            dp[v] += dfs(next_v)

    return dp[v]


n, r, q = map(int, input().split())
adjacencies = [[] for _ in range(n)]
visited = [False for _ in range(n)]
dp = [0 for _ in range(n)]

for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    adjacencies[u].append(v)
    adjacencies[v].append(u)

dfs(r - 1)

for _ in range(q):
    u = int(input()) - 1

    print(dp[u])