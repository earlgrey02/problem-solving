import sys
from collections import deque

input = sys.stdin.readline

def rolling(v: tuple[int, int], d: int) -> tuple[tuple[int, int], int]:
    distance = 0

    while matrix[v[0]][v[1]] != 'O':
        next_v = (v[0] + dy[d], v[1] + dx[d])

        if matrix[next_v[0]][next_v[1]] == '#':
            break
        else:
            v = next_v
            distance += 1

    return (v, distance)

def bfs(red: tuple[int, int], blue: tuple[int, int]) -> int:
    queue = deque([(red, blue)])
    visited[red[0]][red[1]][blue[0]][blue[1]] = 0

    while queue:
        red, blue = queue.popleft()

        if visited[red[0]][red[1]][blue[0]][blue[1]] > 10:
            return -1
        elif matrix[red[0]][red[1]] == 'O':
            return visited[red[0]][red[1]][blue[0]][blue[1]]

        for i in range(4):
            next_red, red_distance = rolling(red, i)
            next_blue, blue_distance = rolling(blue, i)

            if matrix[next_blue[0]][next_blue[1]] != 'O':
                if next_red == next_blue:
                    if red_distance < blue_distance:
                        next_blue = (next_blue[0] - dy[i], next_blue[1] - dx[i])
                    else:
                        next_red = (next_red[0] - dy[i], next_red[1] - dx[i])

                if visited[next_red[0]][next_red[1]][next_blue[0]][next_blue[1]] == -1:
                    visited[next_red[0]][next_red[1]][next_blue[0]][next_blue[1]] = visited[red[0]][red[1]][blue[0]][blue[1]] + 1
                    queue.append((next_red, next_blue))

    return -1

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
visited = [[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            red = (i, j)
        elif matrix[i][j] == 'B':
            blue = (i, j)

print(bfs(red, blue))