import sys
from itertools import groupby

input = sys.stdin.readline

def check() -> int:
    max_count = 1

    for i in range(n):
        count = 1

        for j in range(1, n):
            if matrix[i][j] == matrix[i][j - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    for i in range(n):
        count = 1

        for j in range(1, n):
            if matrix[j][i] == matrix[j - 1][i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    return max_count

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]
count = 0

for i in range(n):
    for j in range(n):
        if i + 1 < n and matrix[i][j] != matrix[i + 1][j]:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            count = max(count, check())
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
        if j + 1 < n and matrix[i][j] != matrix[i][j + 1]:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            count = max(count, check())
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]

print(count)