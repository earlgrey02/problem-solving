import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> int:
    queue = deque([v])
    visited[v[0]][v[1]] = True
    count = 1

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < m and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                count += 1
                queue.append(next_v)

    return count

m, n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
areas = []
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            matrix[i][j] = 1

for i in range(m):
    for j in range(n):
        if not visited[i][j] and matrix[i][j] == 0:
            areas.append(bfs((i, j)))

print(len(areas))
print(*sorted(areas))