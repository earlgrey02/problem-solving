import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> tuple[int, int] | None:
    queue = deque([v])
    fishes = set()
    visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and visited[next_v[0]][next_v[1]] == -1 and matrix[next_v[0]][next_v[1]] <= level:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)

                if 1 <= matrix[next_v[0]][next_v[1]] < level:
                    fishes.add(next_v)

    return next(iter(sorted(fishes, key = lambda x: (visited[x[0]][x[1]], x[0], x[1]))), None)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
shark = next((i, j) for i in range(n) for j in range(n) if matrix[i][j] == 9)
matrix[shark[0]][shark[1]] = 0
level = 2
exp = 0
answer = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while True:
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    if (fish := bfs(shark)) == None:
        break

    shark = fish
    matrix[fish[0]][fish[1]] = 0
    answer += visited[fish[0]][fish[1]]

    if (exp := exp + 1) == level:
        level += 1
        exp = 0

print(answer)