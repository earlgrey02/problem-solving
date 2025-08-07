import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(v: tuple[int, int]) -> int:
    if v == (m - 1, n - 1):
        return 1
    else:
        visited[v[0]][v[1]] = True

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < m and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] < matrix[v[0]][v[1]]:
                dp[v[0]][v[1]] += dp[next_v[0]][next_v[1]] if visited[next_v[0]][next_v[1]] else dfs(next_v)

    return dp[v[0]][v[1]]

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
dp = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

dfs((0, 0))

print(dp[0][0])