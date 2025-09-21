import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs(v: tuple[int, int], matrix: list[list[int]]):
    queue = deque([v])

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True
                matrix[next_v[0]][next_v[1]] = 2
                queue.append(next_v)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
blanks = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 0]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
answer = 0

for case in combinations(blanks, 3):
    copied_matrix = [row[:] for row in matrix]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i, j in case:
        copied_matrix[i][j] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                bfs((i, j), copied_matrix)

    answer = max(sum(map(lambda x: x.count(0), copied_matrix)), answer)

print(answer)