import sys
from copy import deepcopy

input = sys.stdin.readline

def spread_dusts(matrix: list[list[int]]) -> list[list[int]]:
    spreaded_matrix = deepcopy(matrix)
    dusts = [(i, j) for i in range(r) for j in range(c) if matrix[i][j] > 0]

    for dust in dusts:
        count = 0
        ammount = matrix[dust[0]][dust[1]] // 5

        for i in range(4):
            next_v = (dust[0] + dy[i], dust[1] + dx[i])

            if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] != -1:
                spreaded_matrix[next_v[0]][next_v[1]] += ammount
                count += 1

        spreaded_matrix[dust[0]][dust[1]] -= count * ammount

    return spreaded_matrix

def clean_dusts(matrix: list[list[int]]):
    air_cleaners = [(i, 0) for i in range(r) if matrix[i][0] == -1]

    for is_clockwise, air_cleaner in zip((False, True), air_cleaners):
        dy = (0, 1 if is_clockwise else -1, 0, -1 if is_clockwise else 1)
        dx = (1, 0, -1, 0)
        v = air_cleaner
        prev = 0

        for i in range(4):
            while True:
                next_v = (v[0] + dy[i], v[1] + dx[i])

                if not (0 <= next_v[0] < r and 0 <= next_v[1] < c) or next_v == air_cleaner:
                    break

                matrix[next_v[0]][next_v[1]], prev = prev, matrix[next_v[0]][next_v[1]]
                v = next_v

r, c, t = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for _ in range(t):
    matrix = spread_dusts(matrix)
    clean_dusts(matrix)

print(sum(map(sum, matrix)) + 2)