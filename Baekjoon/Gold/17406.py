import sys
from itertools import permutations
from math import inf

input = sys.stdin.readline

def rotate(matrix: list[list[int]], operation: tuple[int, int, int]):
    r, c, s = operation

    for i in range(1, s + 1):
        layer = []
        top, right, bottom, left = r - i, c + i, r + i, c - i

        for j in range(left, right):
            layer.append(matrix[top][j])

        for j in range(top, bottom):
            layer.append(matrix[j][right])

        for j in range(right, left, -1):
            layer.append(matrix[bottom][j])

        for j in range(bottom, top, -1):
            layer.append(matrix[j][left])

        layer = [layer[-1]] + layer[:-1]
        index = 0

        for j in range(left, right):
            matrix[top][j] = layer[index]
            index += 1

        for j in range(top, bottom):
            matrix[j][right] = layer[index]
            index += 1

        for j in range(right, left, -1):
            matrix[bottom][j] = layer[index]
            index += 1

        for j in range(bottom, top, -1):
            matrix[j][left] = layer[index]
            index += 1

n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
operations = [tuple(map(int, input().split())) for _ in range(k)]
minimum = inf

for case in permutations(operations):
    rotated_matrix = [row[:] for row in matrix]

    for r, c, s in case:
        rotate(rotated_matrix, (r - 1, c - 1, s))

    minimum = min(minimum, min(map(sum, rotated_matrix)))

print(minimum)