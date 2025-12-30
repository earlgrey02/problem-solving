import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(min(n, m) // 2):
    layer = []
    top, right, bottom, left = i, m - 1 - i, n - 1 - i, i

    for j in range(left, right + 1):
        layer.append(matrix[top][j])

    for j in range(top + 1, bottom):
        layer.append(matrix[j][right])

    for j in range(right, left - 1, -1):
        layer.append(matrix[bottom][j])

    for j in range(bottom - 1, top, -1):
        layer.append(matrix[j][left])

    mid = r % len(layer)
    layer = layer[mid:] + layer[:mid]
    index = 0

    for j in range(left, right + 1):
        matrix[top][j] = layer[index]
        index += 1

    for j in range(top + 1, bottom):
        matrix[j][right] = layer[index]
        index += 1

    for j in range(right, left - 1, -1):
        matrix[bottom][j] = layer[index]
        index += 1

    for j in range(bottom - 1, top, -1):
        matrix[j][left] = layer[index]
        index += 1

for row in matrix:
    print(*row)