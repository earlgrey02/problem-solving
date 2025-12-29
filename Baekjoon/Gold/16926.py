import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
layers = []

for i in range(min(n, m) // 2):
    layer = []

    for j in range(i, m - i):
        layer.append(matrix[i][j])

    for j in range(i + 1, n - i):
        layer.append(matrix[j][m - i - 1])

    for j in range(m - i - 2, i - 1, -1):
        layer.append(matrix[n - i - 1][j])

    for j in range(n - i - 2, i, -1):
        layer.append(matrix[j][i])

    mid = r % len(layer)
    layers.append(layer[mid:] + layer[:mid])

for i in range(len(layers)):
    layer = layers[i]
    index = 0

    for j in range(i, m - i):
        matrix[i][j] = layer[index]
        index += 1

    for j in range(i + 1, n - i):
        matrix[j][m - i - 1] = layer[index]
        index += 1

    for j in range(m - i - 2, i - 1, -1):
        matrix[n - i - 1][j] = layer[index]
        index += 1

    for j in range(n - i - 2, i, -1):
        matrix[j][i] = layer[index]
        index += 1

for row in matrix:
    print(*row)