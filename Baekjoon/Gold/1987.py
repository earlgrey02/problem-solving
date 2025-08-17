import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: tuple[int, int], visited: int) -> int:
    if visited in dp[v[0]][v[1]]:
        return dp[v[0]][v[1]][visited]
    else:
        dp[v[0]][v[1]][visited] = 1

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c:
                if visited & (next_visited := 1 << (ord(matrix[next_v[0]][next_v[1]]) - ord('A'))) == 0:
                    dp[v[0]][v[1]][visited] = max(dp[v[0]][v[1]][visited], dfs(next_v, visited | next_visited) + 1)

    return dp[v[0]][v[1]][visited]

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
dp = [[dict() for _ in range(c)] for _ in range(r)]
visited = 1 << (ord(matrix[0][0]) - ord('A'))
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

print(dfs((0, 0), visited))