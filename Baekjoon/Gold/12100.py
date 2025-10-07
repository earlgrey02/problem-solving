import sys

input = sys.stdin.readline

def slice(matrix: list[list[int]], d: int):
    if d == 0:
        for j in range(n):
            p = 0

            for i in range(n):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[p][j] == 0:
                        matrix[p][j] = temp
                    elif matrix[p][j] == temp:
                        matrix[p][j] <<= 1
                        p += 1
                    else:
                        matrix[p := p + 1][j] = temp
    elif d == 1:
        for i in range(n):
            p = n - 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[i][p] == 0:
                        matrix[i][p] = temp
                    elif matrix[i][p] == temp:
                        matrix[i][p] <<= 1
                        p -= 1
                    else:
                        matrix[i][p := p - 1] = temp
    elif d == 2:
        for j in range(n):
            p = n - 1

            for i in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[p][j] == 0:
                        matrix[p][j] = temp
                    elif matrix[p][j] == temp:
                        matrix[p][j] <<= 1
                        p -= 1
                    else:
                        matrix[p := p - 1][j] = temp
    elif d == 3:
        for i in range(n):
            p = 0

            for j in range(n):
                if matrix[i][j] != 0:
                    temp = matrix[i][j]
                    matrix[i][j] = 0

                    if matrix[i][p] == 0:
                        matrix[i][p] = temp
                    elif matrix[i][p] == temp:
                        matrix[i][p] <<= 1
                        p += 1
                    else:
                        matrix[i][p := p + 1] = temp

def backtracking(matrix: list[list[int]], depth: int):
    global max_value

    max_value = max(max_value, value := max(map(max, matrix)))

    if value * (2 ** (5 - depth)) > max_value and depth < 5:
        for d in range(4):
            slice(next_matrix := [row[:] for row in matrix], d)

            if next_matrix != matrix:
                backtracking(next_matrix, depth + 1)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_value = 0

backtracking(matrix, 0)

print(max_value)