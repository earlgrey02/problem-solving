import sys
from collections import deque

input = sys.stdin.readline

def waters_bfs(waters: deque[tuple[int, int]]) -> deque[tuple[int, int]]:
    next_waters = deque()

    while waters:
        v = waters.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] == 'X':
                matrix[next_v[0]][next_v[1]] = '.'
                next_waters.append(next_v)

    return next_waters

def swans_bfs(swans: deque[tuple[int, int]]) -> deque[tuple[int, int]]:
    next_swans = deque()

    while swans:
        v = swans.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and not visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = True

                if matrix[next_v[0]][next_v[1]] == '.':
                    swans.append(next_v)
                else:
                    next_swans.append(next_v)

    return next_swans

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
swans, waters = (deque() for _ in range(2))
day = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'L':
            if swans:
                swan = (i, j)
            else:
                swans.append((i, j))

            waters.append((i, j))
            matrix[i][j] = '.'
        elif matrix[i][j] == '.':
            waters.append((i, j))

while True:
    swans = swans_bfs(swans)

    if visited[swan[0]][swan[1]]:
        break

    waters = waters_bfs(waters)
    day += 1

print(day)