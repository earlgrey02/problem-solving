import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]):
    queue = deque([v])

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 1 and visited[next_v[0]][next_v[1]] == 0:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
destination = next((i, j) for j in range(m) for i in range(n) if matrix[i][j] == 2)
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

bfs(destination)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

print(*(' '.join(map(str, row)) for row in visited), sep = '\n')