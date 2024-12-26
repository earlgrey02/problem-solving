import sys

input = sys.stdin.readline

def backtracking(depth: int, columns: int, left_diag: int, right_diag: int):
    global count

    if depth == n:
        count += 1
    else:
        possible_positions = ~ (columns | left_diag | right_diag) & ((1 << n) - 1)

        while possible_positions:
            position = possible_positions & -possible_positions
            possible_positions -= position
            backtracking(depth + 1, columns | position, (left_diag | position) << 1, (right_diag | position) >> 1)

n = int(input())
count = 0

backtracking(0, 0, 0, 0)

print(count)