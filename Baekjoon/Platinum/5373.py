import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
sides = ('U', 'D', 'F', 'B', 'L', 'R')
colors = ('w', 'y', 'r', 'o', 'g', 'b')

for _ in range(t):
    n = int(input())
    cube = {side: [[color for _ in range(3)] for _ in range(3)] for side, color in zip(sides, colors)}

    for side, direction in map(tuple, input().split()):
        if side == 'U' or side == 'D':
            i = 0 if side == 'U' else 2

            lines = deque(cube[j][i] for j in ('F', 'L', 'B', 'R'))
            lines.rotate(1 if (direction == '+' and side == 'U') or (direction == '-' and side == 'D') else -1)

            cube['F'][i], cube['L'][i], cube['B'][i], cube['R'][i] = lines
        elif side == 'F' or side == 'B':
            i = 0 if side == 'F' else 2

            if (side == 'F' and direction == '-') or (side == 'B' and direction == '+'):
                lines = deque([
                    cube['U'][2 - i][::-1],
                    [cube['L'][j][2 - i] for j in range(3)],
                    cube['D'][i][::-1],
                    [cube['R'][j][i] for j in range(3)]
                ])
                lines.rotate()

                for j in range(3):
                    cube['U'][2 - i][j], cube['L'][j][2 - i], cube['D'][i][j], cube['R'][j][i] = (lines[k][j] for k in range(4))
            else:
                lines = deque([
                    cube['U'][2 - i],
                    [cube['R'][j][i] for j in range(3)][::-1],
                    cube['D'][i],
                    [cube['L'][j][2 - i] for j in range(3)][::-1]
                ])
                lines.rotate()

                for j in range(3):
                    cube['U'][2 - i][j], cube['R'][j][i], cube['D'][i][j], cube['L'][j][2 - i] = [lines[k][j] for k in range(4)]
        elif side == 'L' or side == 'R':
            i = 0 if side == 'L' else 2

            if (side == 'L' and direction == '-') or (side == 'R' and direction == '+'):
                lines = deque([
                    [cube['U'][j][i] for j in range(3)][::-1],
                    [cube['B'][j][2 - i] for j in range(3)][::-1],
                    [cube['D'][j][i] for j in range(3)],
                    [cube['F'][j][i] for j in range(3)],
                ])
                lines.rotate()

                for j in range(3):
                    cube['U'][j][i], cube['B'][j][2 - i], cube['D'][j][i], cube['F'][j][i] = [lines[k][j] for k in range(4)]
            else:
                lines = deque([
                    [cube['U'][j][i] for j in range(3)],
                    [cube['F'][j][i] for j in range(3)],
                    [cube['D'][j][i] for j in range(3)][::-1],
                    [cube['B'][j][2 - i] for j in range(3)][::-1]
                ])
                lines.rotate()

                for j in range(3):
                    cube['U'][j][i], cube['F'][j][i], cube['D'][j][i], cube['B'][j][2 - i] = [lines[k][j] for k in range(4)]

        if direction == '+':
            cube[side] = list(map(list, zip(*cube[side][::-1])))
        else:
            cube[side] = list(map(list, zip(*cube[side])))[::-1]

    print(*map(''.join, cube['U']), sep = '\n')