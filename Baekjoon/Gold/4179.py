import sys
from collections import deque
from math import inf

input = sys.stdin.readline

def fires_bfs(fires: set[tuple[int, int]], visited: list[list[float]]):
    queue = deque(fires)

    for fire in fires:
        visited[fire[0]][fire[1]] = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] == '.' and visited[next_v[0]][next_v[1]] == inf:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)

def escape_bfs(v: tuple[int, int], visited: list[list[int]]) -> int:
    queue = deque([v])
    visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c:
                if matrix[next_v[0]][next_v[1]] == '.' and visited[next_v[0]][next_v[1]] == -1 and visited[v[0]][v[1]] + 1 < fire_visited[next_v[0]][next_v[1]]:
                    visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                    queue.append(next_v)
            else:
                return visited[v[0]][v[1]] + 1

    return -1

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
escape_visited = [[-1 for _ in range(c)] for _ in range(r)]
fire_visited = [[inf for _ in range(c)] for _ in range(r)]
fires = set()
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'F':
            fires.add((i, j))
            matrix[i][j] = '.'
        elif matrix[i][j] == 'J':
            start = (i, j)
            matrix[i][j] = '.'

fires_bfs(fires, fire_visited)

print(time if (time := escape_bfs(start, escape_visited)) > 0 else "IMPOSSIBLE")