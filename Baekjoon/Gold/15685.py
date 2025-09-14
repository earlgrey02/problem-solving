import sys

input = sys.stdin.readline

n = int(input())
matrix = [[False for _ in range(101)] for _ in range(101)]
count = 0
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

for _ in range(n):
    x, y, d, g = map(int, input().split())
    matrix[y][x] = True
    directions = [d]

    for _ in range(g):
        for i in range(len(directions) - 1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    for direction in directions:
        matrix[y := y + dy[direction]][x := x + dx[direction]] = True

for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j + 1] and matrix[i + 1][j] and matrix[i + 1][j + 1]:
            count += 1

print(count)