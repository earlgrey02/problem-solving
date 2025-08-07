import sys
from math import inf

input = sys.stdin.readline

def get_square_count(x_range: range, y_range: range) -> int:
    first = {'B': 0, 'W': 0}

    for i in x_range:
        for j in y_range:
            if (i + j) % 2 == 0:
                if board[i][j] == 'B':
                    first['W'] += 1
                else:
                    first['B'] += 1
            else:
                if board[i][j] == 'B':
                    first['B'] += 1
                else:
                    first['W'] += 1

    return min(first.values())

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
answer = inf

for i in range(n - 7):
    for j in range(m - 7):
        answer = min(answer, get_square_count(range(i, i + 8), range(j, j + 8)))

print(answer)