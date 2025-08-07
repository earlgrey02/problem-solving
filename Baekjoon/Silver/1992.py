import sys

input = sys.stdin.readline

def compress(matrix: list[list[int]]) -> str:
    result = ""

    if all(i == (first := matrix[0][0]) for row in matrix for i in row):
        result += str(first)
    else:
        result += '('
        n = len(matrix)
        div = n // 2

        for i in range(0, n, div):
            for j in range(0, n, div):
                sub_matrix = [row[j:j + div] for row in matrix[i:i + div]]
                result += compress(sub_matrix)

        result += ')'

    return result

n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]

print(compress(matrix))