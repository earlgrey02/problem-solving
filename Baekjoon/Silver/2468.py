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

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] > h and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
h = 0
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and matrix[i][j] > h:
                bfs((i, j))
                count += 1

    if count == 0:
        break

    answer = max(answer, count)
    h += 1

print(answer)