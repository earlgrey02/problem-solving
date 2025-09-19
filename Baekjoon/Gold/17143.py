import sys

input = sys.stdin.readline

def move() -> list[list[tuple[int, int, int]]]:
    moved_matrix = [[(0, 0, 0) for _ in range(c)] for _ in range(r)]
    sharks = [(i, j) for i in range(r) for j in range(c) if matrix[i][j] != (0, 0, 0)]
    periods = (2 * (r - 1), 2 * (c - 1))

    for y, x in sharks:
        s, z, d = matrix[y][x]

        if d <= 1:
            if (y := ((y if d == 1 else periods[0] - y) + s) % periods[0]) >= r:
                y = periods[0] - y
                d = 0
            else:
                d = 1
        else:
            if (x := ((x if d == 2 else periods[1] - x) + s) % periods[1]) >= c:
                x = periods[1] - x
                d = 3
            else:
                d = 2

        if moved_matrix[y][x][1] < z:
            moved_matrix[y][x] = (s, z, d)

    return moved_matrix

r, c, m = map(int, input().split())
matrix = [[(0, 0, 0) for _ in range(c)] for _ in range(r)]
position = -1
total_size = 0
dy = (-1, 1, 0, 0)
dx = (0, 0, 1, -1)

for _ in range(m):
    y, x, s, d, z = map(int, input().split())
    matrix[y - 1][x - 1] = (s, z, d - 1)

while (position := position + 1) < c:
    if (v := next(((i, position) for i in range(r) if matrix[i][position] != (0, 0, 0)), None)):
        total_size += matrix[v[0]][v[1]][1]
        matrix[v[0]][v[1]] = (0, 0, 0)

    matrix = move()

print(total_size)