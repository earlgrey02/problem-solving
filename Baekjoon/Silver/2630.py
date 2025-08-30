import sys

input = sys.stdin.readline

def check_count(matrix: list[list[int]]):
    if all(i == (first := matrix[0][0]) for row in matrix for i in row):
        counts[first] += 1
    else:
        n = len(matrix)
        div = n // 2

        for i in range(0, n, div):
            for j in range(0, n, div):
                sub_matrix = [row[j:j + div] for row in matrix[i:i + div]]
                check_count(sub_matrix)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
counts = [0 for _ in range(2)]

check_count(matrix)

print(*counts, sep = '\n')