import sys
from math import inf

input = sys.stdin.readline

def gerrymandering(v: tuple[int, int], d: tuple[int, int]) -> int:
    populations = [0 for _ in range(5)]
    boundary = v[1]

    for i in range(v[0] + d[0]):
        if i >= v[0]:
            boundary -= 1

        populations[0] += sum(matrix[i][:boundary + 1])

    boundary = v[1]

    for i in range(v[0] + d[1] + 1):
        if i > v[0]:
            boundary += 1

        populations[1] += sum(matrix[i][boundary + 1:])

    boundary = v[1] - d[0]

    for i in range(v[0] + d[0], n):
        populations[2] += sum(matrix[i][:boundary])

        if i < v[0] + sum(d):
            boundary += 1

    boundary = v[1] + d[1]

    for i in range(v[0] + d[1] + 1, n):
        populations[3] += sum(matrix[i][boundary:])

        if i <= v[0] + sum(d):
            boundary -= 1

    populations[4] = summation - sum(populations)

    return max(populations) - min(populations)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
summation = sum(map(sum, matrix))
diff = inf

for d1 in range(1, n):
    for d2 in range(1, n):
        for y in range(n - (d1 + d2)):
            for x in range(d1, n - d2):
                diff = min(diff, gerrymandering((y, x), (d1, d2)))

print(diff)