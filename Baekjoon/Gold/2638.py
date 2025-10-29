import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> set[tuple[int, int]]:
    visited = [[False for _ in range(m)] for _ in range(n)]
    cheeses = {}
    queue = deque([v])
    visited[v[0]][v[1]] = True

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
                if matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]]:
                    visited[next_v[0]][next_v[1]] = True
                    queue.append(next_v)
                elif matrix[next_v[0]][next_v[1]] == 1:
                    cheeses[next_v] = cheeses.get(next_v, 0) + 1

    return set(v for v, count in cheeses.items() if count > 1)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cheeses = set((i, j) for j in range(m) for i in range(n) if matrix[i][j] == 1)
time = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while cheeses:
    cheeses -= (melted_cheeses := bfs((0, 0)))

    for cheese in melted_cheeses:
        matrix[cheese[0]][cheese[1]] = 0

    time += 1

print(time)