import sys
from itertools import combinations
from math import inf

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
houses = [(i, j) for j in range(n) for i in range(n) if matrix[i][j] == 1]
chickens = [(i, j) for j in range(n) for i in range(n) if matrix[i][j] == 2]
answer = inf

for chickens in combinations(chickens, m):
    total = 0

    for house in houses:
        distance = inf

        for chicken in chickens:
            distance = min(distance, sum(abs(chicken[i] - house[i]) for i in range(2)))

        total += distance

    answer = min(answer, total)

print(answer)