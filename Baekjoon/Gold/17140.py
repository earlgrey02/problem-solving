import sys
from collections import Counter

input = sys.stdin.readline

def sort(matrix: list[list[int]], is_row: bool = True) -> list[list[int]]:
    sorted_matrix = [row[:] for row in matrix] if is_row else list(map(list, zip(*matrix)))
    size = 0

    for i in range(len(sorted_matrix)):
        counter = Counter(j for j in sorted_matrix[i] if j != 0)
        sorted_matrix[i] = [j for pair in sorted(counter.items(), key = lambda x: (x[1], x[0])) for j in pair][:100]
        size = max(size, len(sorted_matrix[i]))

    for row in sorted_matrix:
        row.extend(0 for _ in range(100 - len(row)))

    if is_row:
        sizes[1] = size
    else:
        sorted_matrix = list(map(list, zip(*sorted_matrix)))
        sizes[0] = size

    return sorted_matrix

r, c, k = map(int, input().split())
matrix = [[0 for _ in range(100)] for _ in range(100)]
sizes = [3, 3]
time = 0

for i in range(3):
    matrix[i][:3] = list(map(int, input().split()))

while time < 100 and matrix[r - 1][c - 1] != k:
    matrix = sort(matrix, sizes[0] >= sizes[1])
    time += 1

print(time if matrix[r - 1][c - 1] == k else -1)