import sys

input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(9)]
maximums = [max(row) for row in matrix]
maximum = max(maximums)
max_y = maximums.index(maximum)

print(maximum)
print(max_y + 1, matrix[max_y].index(maximum) + 1)