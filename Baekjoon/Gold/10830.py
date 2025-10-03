import sys

input = sys.stdin.readline

def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix[i][j] += a[i][k] * b[k][j]

            matrix[i][j] %= mod

    return matrix

def pow(a: list[list[int]], n: int) -> list[list[int]]:
    if n == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= mod

        return a
    else:
        b = pow(a, n // 2)

        if n % 2 == 0:
            return multiply(b, b)
        else:
            return multiply(a, multiply(b, b))

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
mod = 1000

print(*(' '.join(map(str, row)) for row in pow(matrix, b)), sep = '\n')