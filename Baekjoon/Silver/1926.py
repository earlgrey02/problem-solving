import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> int:
    queue = deque([v])
    visited[v[0]][v[1]] = True
    area = 1

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 1 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                area += 1
                queue.append(next_v)

    return area

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
count = area = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            count += 1
            area = max(area, bfs((i, j)))

print(count, area, sep = '\n')