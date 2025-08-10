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

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 1 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

t = int(input())
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs((i, j))
                count += 1

    print(count)