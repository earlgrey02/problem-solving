import sys

input = sys.stdin.readline

def slice(matrix: list[list[int]], d: int):
    if d == 0:
        for j in range(n):
            top = 0

            for i in range(n):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[top][j] == 0:
                        matrix[top][j] = temp
                    elif matrix[top][j] == temp:
                        matrix[top][j] <<= 1
                        top += 1
                    else:
                        top += 1
                        matrix[top][j] = temp
    elif d == 1:
        for i in range(n):
            top = n - 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[i][top] == 0:
                        matrix[i][top] = temp
                    elif matrix[i][top] == temp:
                        matrix[i][top] <<= 1
                        top -= 1
                    else:
                        top -= 1
                        matrix[i][top] = temp
    elif d == 2:
        for j in range(n):
            top = n - 1

            for i in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[top][j] == 0:
                        matrix[top][j] = temp
                    elif matrix[top][j] == temp:
                        matrix[top][j] <<= 1
                        top -= 1
                    else:
                        top -= 1
                        matrix[top][j] = temp

    elif d == 3:
        for i in range(n):
            top = 0

            for j in range(n):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[i][top] == 0:
                        matrix[i][top] = temp
                    elif matrix[i][top] == temp:
                        matrix[i][top] <<= 1
                        top += 1
                    else:
                        top += 1
                        matrix[i][top] = temp

def backtracking(matrix: list[list[int]], depth: int = 0):
    global max_value

    max_value = max(max_value, value := max(map(max, matrix)))

    if value <= values[depth]:
        return

    if depth == 5:
        if values[depth] < value:
            for i in range(5, 0, -1):
                values[i] = value
                value //= 2
    else:
        for d in range(4):
            slice(next_matrix := [row[:] for row in matrix], d)

            if next_matrix != matrix:
                backtracking(next_matrix, depth + 1)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_value = 0
values = [0 for _ in range(6)]

backtracking(matrix)

print(max_value)