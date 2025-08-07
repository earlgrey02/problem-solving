import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dice = (x, y)
sides = [0 for _ in range(6)]
commands = list(map(lambda x: int(x) - 1, input().split()))
positions = [
    (3, 1, 0, 5, 4, 2),
    (2, 1, 5, 0, 4, 3),
    (1, 5, 2, 3, 0, 4),
    (4, 0, 2, 3, 5, 1)
]
dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)

for command in commands:
    next_dice = (dice[0] + dy[command], dice[1] + dx[command])

    if 0 <= next_dice[0] < n and 0 <= next_dice[1] < m:
        sides = [sides[i] for i in positions[command]]
        dice = next_dice

        if matrix[next_dice[0]][next_dice[1]] == 0:
            matrix[next_dice[0]][next_dice[1]] = sides[-1]
        else:
            sides[-1], matrix[next_dice[0]][next_dice[1]] = matrix[next_dice[0]][next_dice[1]], 0

        print(sides[0])