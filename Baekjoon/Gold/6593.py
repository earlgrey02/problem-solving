import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int, int]) -> int:
    queue = deque([v])
    visited[v[0]][v[1]][v[2]] = 0

    while queue:
        v = queue.popleft()

        if v == destination:
            return visited[v[0]][v[1]][v[2]]

        for i in range(6):
            next_v = (v[0] + dz[i], v[1] + dy[i], v[2] + dx[i])

            if 0 <= next_v[0] < l and 0 <= next_v[1] < r and 0 <= next_v[2] < c and matrix[next_v[0]][next_v[1]][next_v[2]] == '.' and visited[next_v[0]][next_v[1]][next_v[2]] == -1:
                visited[next_v[0]][next_v[1]][next_v[2]] = visited[v[0]][v[1]][v[2]] + 1
                queue.append(next_v)

    return -1

dz = (1, -1, 0, 0, 0, 0)
dy = (0, 0, 1, -1, 0, 0)
dx = (0, 0, 0, 0, 1, -1)

while (dimensions := tuple(map(int, input().split()))) != (0, 0, 0):
    l, r, c = dimensions
    matrix = []
    visited = [[[-1 for _ in range(c)] for _ in range(r)] for _ in range(l)]

    for _ in range(l):
        matrix.append([list(input().strip()) for _ in range(r)])
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if matrix[i][j][k] == 'S':
                    start = (i, j, k)
                    matrix[i][j][k] = '.'
                elif matrix[i][j][k] == 'E':
                    destination = (i, j, k)
                    matrix[i][j][k] = '.'

    print(f"Escaped in {time} minute(s)." if (time := bfs(start)) >= 0 else "Trapped!")