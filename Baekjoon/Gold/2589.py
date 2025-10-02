import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> int:
    queue = deque([v])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 'L' and visited[next_v[0]][next_v[1]] == -1:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)

    return max(map(max, visited))

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]
distance = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L' and (distance := max(distance, bfs((i, j)))) == n + m - 2:
            break

print(distance)