import sys
from collections import deque

input = sys.stdin.readline

def waters_bfs(waters: list[tuple[int, int]]):
    queue = deque(waters)

    for v in waters:
        water_visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] == '.' and water_visited[next_v[0]][next_v[1]] == -1:
                water_visited[next_v[0]][next_v[1]] = water_visited[v[0]][v[1]] + 1
                queue.append(next_v)

def hadgehog_bfs(v: tuple[int, int]) -> int:
    queue = deque([v])
    hadgehog_visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        if v == nest:
            return hadgehog_visited[v[0]][v[1]]

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and ((matrix[next_v[0]][next_v[1]] == '.' and (water_visited[next_v[0]][next_v[1]] == -1 or water_visited[next_v[0]][next_v[1]] > hadgehog_visited[v[0]][v[1]] + 1)) or matrix[next_v[0]][next_v[1]] == 'D') and hadgehog_visited[next_v[0]][next_v[1]] == -1:
                hadgehog_visited[next_v[0]][next_v[1]] = hadgehog_visited[v[0]][v[1]] + 1
                queue.append(next_v)

    return -1

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
water_visited, hadgehog_visited = ([[-1 for _ in range(c)] for _ in range(r)] for _ in range(2))
waters = []
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(r):
    for j in range(c):
        if matrix[i][j] == '*':
            waters.append((i, j))
        elif matrix[i][j] == 'D':
            nest = (i, j)
        elif matrix[i][j] == 'S':
            hadgehog = (i, j)

waters_bfs(waters)

print(time if (time := hadgehog_bfs(hadgehog)) > 0 else "KAKTUS")