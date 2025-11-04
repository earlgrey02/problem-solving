import sys

input = sys.stdin.readline

def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    matrix = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
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

def fibonacci(n: int) -> int:
    matrix = [[1, 1], [1, 0]]

    return pow(matrix, n)[0][1]

n = int(input())
mod = int(1e6)

print(fibonacci(n))