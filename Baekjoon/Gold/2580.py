import sys

input = sys.stdin.readline

def backtracking(depth: int):
    if depth == len(blanks):
        for row in matrix:
            print(*row)
        exit()
    else:
        y, x = blanks[depth]

        for i in range(1, 10):
            check = 1 << i

            if not (rows[y] & check or columns[x] & check or squares[y // 3 + (x // 3) * 3] & check):
                matrix[y][x] = i
                rows[y] |= check
                columns[x] |= check
                squares[y // 3 + (x // 3) * 3] |= check
                backtracking(depth + 1)
                matrix[y][x] = 0
                rows[y] &= ~check
                columns[x] &= ~check
                squares[y // 3 + (x // 3) * 3] &= ~check

matrix = [list(map(int, input().split())) for _ in range(9)]
rows, columns, squares = ([0 for _ in range(9)] for _ in range(3))
blanks = []

for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            blanks.append((i, j))
        else:
            check = 1 << matrix[i][j]
            rows[i] |= check
            columns[j] |= check
            squares[i // 3 + (j // 3) * 3] |= check

backtracking(0)