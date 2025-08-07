import sys
from itertools import combinations

input = sys.stdin.readline

def dfs(v: tuple[int, int], total: int, depth: int):
    global answer

    if depth == 4:
        answer = max(answer, total)
    else:
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                dfs(next_v, total + matrix[next_v[0]][next_v[1]], depth + 1)
                visited[next_v[0]][next_v[1]] = False

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
answer = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs((i, j), matrix[i][j], 1)
        visited[i][j] = False

        for directions in combinations(range(4), 3):
            total = matrix[i][j]

            for k in directions:
                next_v = (i + dy[k], j + dx[k])

                if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
                    total += matrix[next_v[0]][next_v[1]]

            answer = max(answer, total)

print(answer)