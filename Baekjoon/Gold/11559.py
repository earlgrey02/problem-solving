import sys
from collections import deque

input = sys.stdin.readline

def get_puyos(v: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque([v])
    puyos = [v]
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < 12 and 0 <= next_v[1] < 6 and matrix[v[0]][v[1]] == matrix[next_v[0]][next_v[1]] and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                puyos.append(next_v)
                queue.append(next_v)

    return puyos

def boom(groups: list[list[tuple[int, int]]]):
    for group in groups:
        for puyo in group:
            matrix[puyo[0]][puyo[1]] = '.'

    for i in range(6):
        puyos = [matrix[j][i] for j in range(12) if matrix[j][i] != '.']
        puyos[:0] = ['.' for _ in range(12 - len(puyos))]

        for j in range(12):
            matrix[j][i] = puyos[j]

matrix = [list(input().strip()) for _ in range(12)]
count = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    groups = []

    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.' and not visited[i][j]:
                if len(puyos := get_puyos((i, j))) >= 4:
                    groups.append(puyos)

    if groups:
        boom(groups)
        count += 1
    else:
        break

print(count)