import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: tuple[int, int]) -> int:
    if dp[v[0]][v[1]] != 0:
        return dp[v[0]][v[1]]
    else:
        dp[v[0]][v[1]] = 1

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[v[0]][v[1]] < matrix[next_v[0]][next_v[1]]:
                dp[v[0]][v[1]] = max(dp[v[0]][v[1]], dfs(next_v) + 1)

    return dp[v[0]][v[1]]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            dfs((i, j))

print(max(map(max, dp)))