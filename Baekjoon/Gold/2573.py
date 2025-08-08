import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> set[tuple[tuple[int, int], int]]:
    queue = deque([v])
    icebergs = set()
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()
        melt = 0

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]]:
                if matrix[next_v[0]][next_v[1]] > 0:
                    visited[next_v[0]][next_v[1]] = True
                    queue.append(next_v)
                else:
                    melt += 1

        icebergs.add((v, melt))

    return icebergs

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0 and not visited[i][j]:
                count += 1

                for iceberg, melt in bfs((i, j)):
                    matrix[iceberg[0]][iceberg[1]] -= melt

    if count == 0:
        answer = 0
        break
    elif count > 1:
        break
    else:
        answer += 1

print(answer)