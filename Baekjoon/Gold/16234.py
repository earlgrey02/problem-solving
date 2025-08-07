import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> set[tuple[int, int]]:
    queue = deque([v])
    visited[v[0]][v[1]] = True
    union = {v}

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and not visited[next_v[0]][next_v[1]] and l <= abs(matrix[v[0]][v[1]] - matrix[next_v[0]][next_v[1]]) <= r:
                visited[next_v[0]][next_v[1]] = True
                queue.append(next_v)
                union.add(next_v)

    return union

n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    has_union = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs((i, j))

                if len(union) > 1:
                    has_union = True
                    population = sum(map(lambda x: matrix[x[0]][x[1]], union)) // len(union)

                    for v in union:
                        matrix[v[0]][v[1]] = population

    if has_union:
        answer += 1
    else:
        break

print(answer)