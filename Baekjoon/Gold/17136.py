import sys
from math import inf

input = sys.stdin.readline

def backtracking(depth: int):
    global count

    if count <= depth:
        return

    if not (v := next(((i, j) for i in range(10) for j in range(10) if matrix[i][j] == 1), None)):
        count = min(count, depth)
        return

    for size in range(1, 6):
        if papers[size] > 0 and all(i + size <= 10 for i in v) and all(matrix[v[0] + i][v[1] + j] == 1 for i in range(size) for j in range(size)):
            attach(v, size, 1)
            papers[size] -= 1
            backtracking(depth + 1)
            attach(v, size, 0)
            papers[size] += 1

def attach(v: tuple[int, int], size: int, value: int):
    for i in range(size):
        for j in range(size):
            matrix[v[0] + i][v[1] + j] = value

matrix = [list(map(int, input().split())) for _ in range(10)]
papers = [5 if i > 0 else 0 for i in range(6)]
count = inf

backtracking(0)

print(count if count != inf else -1)