import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(v: tuple[int, int]) -> int:
    visited[v[0]][v[1]] = True
    dp[v[0]][v[1]] = matrix[v[0]][v[1]]

    for i in range(3):
        next_v = (v[0] + dy[i], v[1] + dx[i])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
            dp[v[0]][v[1]] = max(dp[v[0]][v[1]], (dp[next_v[0]][next_v[1]] if visited[next_v[0]][next_v[1]] else dfs(next_v)) + matrix[v[0]][v[1]])

    return dp[v[0]][v[1]]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dy = (1, 0, 1)
dx = (0, 1, 1)

dfs((0, 0))

print(dp[0][0])