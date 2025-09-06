import sys
from copy import deepcopy
from math import inf

input = sys.stdin.readline

def monitoring(matrix: list[list[int]], camera: tuple[int, int], direction: tuple[int, ...]):
    for i in direction:
        v = camera

        while True:
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if not (0 <= next_v[0] < n and 0 <= next_v[1] < m) or matrix[next_v[0]][next_v[1]] == 6:
                break

            if matrix[next_v[0]][next_v[1]] == 0:
                matrix[next_v[0]][next_v[1]] = -1

            v = next_v

def backtracking(matrix: list[list[int]], depth: int = 0):
    global count

    if depth == len(cameras):
        count = min(count, sum(matrix[i][j] == 0 for i in range(n) for j in range(m)))
    else:
        v = cameras[depth]

        for direction in directions[matrix[v[0]][v[1]]]:
            monitored_matrix = deepcopy(matrix)
            monitoring(monitored_matrix, v, direction)
            backtracking(monitored_matrix, depth + 1)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cameras = [(i, j) for i in range(n) for j in range(m) if 0 < matrix[i][j] < 6]
count = inf
directions = {
    1: ((0,), (1,), (2,), (3,)),
    2: ((0, 1), (2, 3)),
    3: ((1, 2), (0, 2), (0, 3), (1, 3)),
    4: ((0, 2, 3), (0, 1, 2), (1, 2, 3), (0, 1, 3)),
    5: ((0, 1, 2, 3),)
}
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

backtracking(matrix)

print(count)