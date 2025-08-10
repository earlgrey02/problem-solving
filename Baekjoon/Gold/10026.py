import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]):
    queue = deque([v])
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[v[0]][v[1]] == matrix[next_v[0]][next_v[1]] and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

n = int(input())
matrices = [
    matrix := [list(input().strip()) for _ in range(n)],
    [[matrix[i][j] if matrix[i][j] != "G" else "R" for j in range(n)] for i in range(n)]
]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for matrix in matrices:
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs((i, j))
                count += 1

    print(count, end = ' ')